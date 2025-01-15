from pathlib import Path
import shutil
from fastapi import FastAPI,  UploadFile, HTTPException
from utils.validation import validate_document_type
from fastapi.middleware.cors import CORSMiddleware
from models.enhance_model import enhance_image
import sys
from schemas.file import FilePath

app = FastAPI()
sys.path.append('D:\projects\Real-ESRGAN')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the directory where files will be saved
UPLOAD_DIR = Path("static/uploads")
ENHANCED_DIR = Path("static/enhanced")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
ENHANCED_DIR.mkdir(parents=True, exist_ok=True) # Ensure the directory exists


@app.post("/upload_files/")
async def create_upload_files(files: list[UploadFile]):
    file_paths = []

    valid_files = validate_document_type(files)

    # Map validated file names back to `UploadFile` objects
    valid_files = [file for file in files if file.filename in valid_files]

    for file in valid_files:
        try:
            # Define the path to save the file
            file_path = UPLOAD_DIR / file.filename

            # Save the file to the directory
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            file_paths.append(str(file_path))
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to save file '{file.filename}': {str(e)}"
            )
        finally:
            # Ensure file is closed
            file.file.close()

    return {"file_paths": file_paths}


@app.post("/enhanced/")
async def enhanced(file: FilePath):
    """
    Enhance a specific image provided in the request body.

    Parameters:
    - file (FilePath): A Pydantic model containing the path of the file to enhance.

    Returns:
    - dict: A dictionary with the enhanced image path.
    """
    try:
        # Enhance the specified image
        enhanced_file_path = enhance_image(file.file_path, ENHANCED_DIR)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to enhance file '{file.file_path}': {str(e)}"
        )

    return {"enhanced_path": enhanced_file_path}

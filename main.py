from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/health")
def read_root():
    return {"Hello": "World"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.content_type for file in files]}

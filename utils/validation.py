from fastapi import HTTPException


def validate_document_type(files):
    # Define allowed MIME types
    ALLOWED_MIME_TYPES = {"image/png", "image/jpeg", "application/pdf"}

    validated_files = []

    for file in files:
        # Validate file type
        if file.content_type not in ALLOWED_MIME_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"File type '{file.content_type}' is not allowed."
            )
        # Reset file pointer for further use
        file.file.seek(0)
        validated_files.append(file.filename)

    return validated_files

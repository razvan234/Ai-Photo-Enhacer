def validate_document_type(file):
    accepted_file_types = ["image/png", "image/jpeg", "image/jpg", "image/heic", "image/heif", "image/heics", "png",
                           "jpeg", "jpg", "heic", "heif", "heics"
                           ]

    return file.mimetype in accepted_file_types

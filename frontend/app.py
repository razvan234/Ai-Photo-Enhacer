# import module
import streamlit as st
import requests

UPLOAD_API_URL = 'http://127.0.0.1:8000/upload_files/'
ENHANCE_API_URL = "http://localhost:8000/enhanced/"

# Title
st.title("AI Photo Enhancer")

# Upload Files
images = st.file_uploader('Upload Image', accept_multiple_files=True)

col1, col2 = st.columns(2)

# Button
if st.button('Upload and Enhance'):
    if images:
        # Upload files to FastAPI
        files = [
            ("files", (file.name, file.getvalue(), file.type))
            for file in images
        ]
        try:
            # Step 1: Upload the image
            upload_response = requests.post(UPLOAD_API_URL, files=files)

            if upload_response.status_code == 200:
                file_path = upload_response.json()['file_paths'][0]
                with col1:
                    st.title('Original Picture')
                    st.image(file_path, caption=file_path)

                # Step 2: Enhance the uploaded image
                enhance_response = requests.post(
                    ENHANCE_API_URL,
                    json={"file_path": file_path}
                )

                if enhance_response.status_code == 200:
                    enhanced_path = enhance_response.json()['enhanced_path']
                    with col2:
                        st.title('Enhanced Picture')
                        st.image(enhanced_path, caption=enhanced_path)
                else:
                    st.error(f"Failed to enhance the file: {enhance_response.text}")
            else:
                st.error(f"Failed to upload the file: {upload_response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload an image.")




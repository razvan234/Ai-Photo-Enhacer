# import module
import streamlit as st

# Title
st.title("AI Photo Enhancer")

# Upload Files
image = st.file_uploader('Upload Image')

# Preview Section
st.title('Preview')
if image is not None:
    st.image(image)
else:
    st.subheader('No Image')



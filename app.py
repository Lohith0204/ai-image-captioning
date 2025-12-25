import streamlit as st
from ai_engine.model import generate_caption
import tempfile

st.title("Image Caption Generator")

image_file = st.file_uploader("Upload an image",type=["jpg", "png", "jpeg"])

if image_file is not None:
    st.image(image_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption... Please wait ⏳"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
                temp_image.write(image_file.read())
                caption = generate_caption(temp_image.name)

        st.success("Caption generated successfully!")
        st.subheader("Generated Caption")
        st.write(caption)

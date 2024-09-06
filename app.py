

import streamlit as st
from PIL import Image
import io

# Function to resize the image
def resize_image(input_image, max_width):
    original_width, original_height = input_image.size
    
    # Resize the image
    if original_width > max_width:
        ratio = max_width / original_width
        new_height = int(original_height * ratio)
        resized_image = input_image.resize((max_width, new_height), Image.Resampling.LANCZOS)
        return resized_image
    else:
        return input_image

# Streamlit app settings
st.title("Image Resizer App")
max_width = st.number_input("Enter the maximum width:", min_value=1, value=224)
uploaded_file = st.file_uploader("Select an image file", type=["jpg", "jpeg", "png"])

# When an image is uploaded
if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    
    # Resize the image
    resized_image = resize_image(image, max_width)
    
    # Save the resized image to an in-memory buffer
    buffer = io.BytesIO()
    resized_image.save(buffer, format=resized_image.format)
    buffer.seek(0)
    
    # Create the new filename
    original_filename = uploaded_file.name
    new_filename = f"{max_width}_{original_filename}"
    
    # Display the resized image
    st.image(resized_image, caption=f"Resized Image (Width: {max_width}px)", use_column_width=True)
    
    # Add a download button for the resized image
    st.download_button(
        label="Download Resized Image",
        data=buffer,
        file_name=new_filename,
        mime=f"image/{resized_image.format.lower()}"
    )
    
    st.success(f"The resized image is ready for download.")



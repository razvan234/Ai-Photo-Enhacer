import os

import torch
from PIL import Image
from RealESRGAN import RealESRGAN


def enhance_image(url, output_folder):
    """
    Enhance an image using the RealESRGAN model and save it to the specified folder.

    Parameters:
    - url (str): The file path or URL of the image to be enhanced.
    - output_folder (str): The folder where the enhanced image will be saved.

    Returns:
    - str: The file path of the enhanced image.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Check device availability
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Initialize the model
    model = RealESRGAN(device, scale=4)
    model.load_weights('models/weights/RealESRGAN_x4.pth', download=True)

    # Load the image
    try:
        image = Image.open(url).convert('RGB')
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

    # Enhance the image
    sr_image = model.predict(image)

    # Generate output file path
    output_file = os.path.join(output_folder, os.path.basename(url))

    # Save the enhanced image
    sr_image.save(output_file)

    return output_file

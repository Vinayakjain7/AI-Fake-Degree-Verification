from PIL import Image, ImageChops, ImageEnhance
import os
import numpy as np


def perform_ela(image_path, quality=70):

    # Create output folder if not exists
    output_folder = "static/ela_output"
    os.makedirs(output_folder, exist_ok=True)

    # Open original image
    original = Image.open(image_path).convert("RGB")

    # Save compressed copy
    temp_path = "temp_compressed.jpg"
    original.save(temp_path, "JPEG", quality=quality)

    compressed = Image.open(temp_path)

    # Calculate difference
    ela_image = ImageChops.difference(original, compressed)

    # Get max pixel difference
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])

    if max_diff == 0:
        max_diff = 1

    # Scale brightness
    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    # Save ELA image
    output_path = os.path.join(output_folder, "ela_result.jpg")
    ela_image.save(output_path)

    # Convert to numpy array
    ela_array = np.array(ela_image)

    # Stronger tampering detection:
    # Combine mean and variance
    mean_diff = np.mean(ela_array)
    variance = np.var(ela_array)

    tampering_score = mean_diff + (variance / 1000)

    return tampering_score, output_path
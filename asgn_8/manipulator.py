from PIL import Image, ImageDraw

def manipulate_image(image_path, output_path):
    with Image.open(image_path) as img:
        # Create a new image with the same size and mode
        manipulated_img = Image.new(img.mode, img.size)

        # Copy the pixels from the original image to the new image
        manipulated_img.paste(img)

        # Apply a red overlay on the new image
        red_overlay = Image.new("RGBA", img.size, (255, 0, 0, 100))
        manipulated_img = Image.alpha_composite(manipulated_img.convert("RGBA"), red_overlay)

        # Save the manipulated image
        manipulated_img.save(output_path)

if __name__ == "__main__":
    input_image_path = "logo.png"
    output_image_path = "manipulated_image.png"

    # Manipulate the input image
    manipulate_image(input_image_path, output_image_path)

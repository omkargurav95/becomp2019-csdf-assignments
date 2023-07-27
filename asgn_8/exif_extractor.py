from PIL import Image


def extract_exif_data(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data is not None:
            print("EXIF Data:")
            for tag_id, value in exif_data.items():
                print(f"Tag ID: {tag_id}, Value: {value}")
        else:
            print("No EXIF data found.")

# if __name__ == "__main__":
#     input_image_path = "img_1771.jpg"
#     extract_exif_data(input_image_path)

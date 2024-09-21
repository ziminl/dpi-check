from PIL import Image

image_path = "your_image.jpg"  # replace with your image path
img = Image.open(image_path)
dpi = img.info.get('dpi')

if dpi:
    print(f"DPI of the image: {dpi}")
else:
    print("No DPI information available in the image.")

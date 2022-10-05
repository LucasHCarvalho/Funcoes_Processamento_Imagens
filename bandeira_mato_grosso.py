from PIL import Image, ImageDraw

def polygon(output_path):
    image = Image.new("RGB", (300, 210), "blue")

    draw = ImageDraw.Draw(image)
    draw.polygon(((25.5, 105), (150, 25.5), (274.5, 105), (150, 174.5)), fill="white")
    draw.ellipse((100, 50, 200, 150), width=5, fill="green", outline="green")
    draw.polygon(((150, 50), (164, 84), (198, 84), (171, 106), (181, 140), (150, 120), (120, 140), (131, 106), (102, 84), (139, 84)), outline="yellow", fill="yellow")

    image.save(output_path)

if __name__ == "__main__":
    polygon("band_mato_grosso.jpg")
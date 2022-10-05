from PIL import Image, ImageDraw

def polygon(output_path):
    image = Image.new("RGB", (300, 210), "white")

    draw = ImageDraw.Draw(image)
    draw.polygon(((100, 50), (200, 50), (200, 90), (150, 160), (100, 90) ), outline="black")
    draw.polygon(((110, 60), (190, 60), (190, 80), (110, 80)), fill="black")
    draw.polygon(((110, 90), (145, 90), (145, 140)), fill="red")
    draw.polygon(((155, 90), (190, 90), (155, 140)), fill="black")

    image.save(output_path)

if __name__ == "__main__":
    polygon("band_sao_paulo.jpg")
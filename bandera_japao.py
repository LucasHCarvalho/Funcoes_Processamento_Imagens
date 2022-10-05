from PIL import Image, ImageDraw

def ellipse(output_path):
    image = Image.new("RGB", (300, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((90, 40, 210, 160), width=5, fill="red", outline="red")

    image.save(output_path)

if __name__ == "__main__":
    ellipse("band_japao.jpg")
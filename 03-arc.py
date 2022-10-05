from PIL import Image, ImageDraw

def arc(output_path):
    image = Image.new("RGB", (500, 500), "white")
    draw = ImageDraw.Draw(image)
    draw.arc((25, 50, 175, 200), start=0, end=360, width=10, fill="green")
    draw.arc((100, 150, 275, 300), start=20, end=180, width=5, fill="purple")
    draw.arc((185, 50, 335, 200), start=0, end=360, width=10, fill="green")

    image.save(output_path)

if __name__ == "__main__":
    arc("arc.jpg")
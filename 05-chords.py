from PIL import Image, ImageDraw

def chord(output_path):
    image = Image.new("RGB", (500, 500), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((25, 50, 175, 200), width=5, fill="green", outline="black")
    draw.chord((100, 150, 275, 300), start=0, end=180, width=5, fill="purple")
    draw.ellipse((185, 50, 335, 200), width=5, fill="green", outline="black")

    image.save(output_path)

if __name__ == "__main__":
    chord("chords.jpg")
from PIL import Image, ImageDraw

def line(output_path):
    image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    points = [(150, 150), (200, 200), (200, 50), (400, 400)]
    draw.line(points, width=15, fill="green", joint="curve")
    image.save(output_path)
    

if __name__ == "__main__":
    line("jointed_lines.jpg")
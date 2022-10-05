import random
from PIL import Image, ImageDraw

def line(output_path):
    image = Image.new("RGBA", (400, 300), 'White')
    draw = ImageDraw.Draw(image)

    draw.line((200, 300) + (200, 0), width=70, fill='blue')
    draw.line((400, 150) + (0, 150), width=70, fill='blue')
    
    image.save(output_path)

if __name__ == "__main__":
    line("lines.png")
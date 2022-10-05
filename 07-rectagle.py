from PIL import Image, ImageDraw

def rectangle(output_path):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((200, 100, 300, 200), fill="purple")
    draw.rectangle((100, 50, 200, 150), fill="green", outline="yellow",width=3)
    image.save(output_path)

if __name__ == "__main__":
    rectangle("retangulo.jpg")
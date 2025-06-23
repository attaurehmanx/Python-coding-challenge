from PIL import Image, ImageDraw, ImageFont

image = Image.open("WhatsApp Image 2025-04-27 at 23.31.40_f1eb13b3.jpg").convert("RGBA")

watermark = Image.new("RGBA", image.size, (0,0,0,0))
draw = ImageDraw.Draw(watermark)

text = "ART BY ATTA"
font = ImageFont.truetype("arial.ttf", 30)

textbox = draw.textbbox((0,0),text, font)
text_width = textbox[2] - textbox[0]
text_height = textbox[3] - textbox[1]


x = image.width - text_width - 10
y = image.height - text_height - 10

draw.text((x, y), text, font= font, fill= (0, 0, 0,))

combined = Image.alpha_composite(image, watermark)

combined.convert("RGB").save("WhatsApp Image 2025-04-27 at 23.31.40_f1eb13b3.jpg", "JPEG")
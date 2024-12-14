from PIL import Image

backgroundUnit = Image.open("./background.png")
image = Image.new("RGB",(2160,1640),color="black")
for i in range(0,3):
    image.paste(backgroundUnit,(0+i*720,0))
image.save("background.png")
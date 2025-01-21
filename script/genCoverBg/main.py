from PIL import Image
import random

def putGround(base:Image.Image) -> Image.Image :
    groundUnit = Image.open("./groundUnit.png")
    for i in range(0,5):
        base.paste(groundUnit,(0+280*i,870))
    return base
def putMushroom(base:Image.Image) -> Image.Image :
    for i in range(0,5):
        mushroomDown = Image.open("./mushroom/mushroom"+str(random.randrange(10))+".png")
        mushroomUp = Image.open("./mushroom/mushroom"+str(random.randrange(10))+".png")
        mushroomUp = mushroomUp.rotate(180)
        postionRandomFix = random.randrange(0,4)*70
        base.paste(mushroomDown,(-19+i*280,760-postionRandomFix))
        base.paste(mushroomUp,(-19+i*280,-560-postionRandomFix))
    return base


entireImage = Image.new("RGB",(1360,1080))
entireImage = putMushroom(entireImage)
entireImage = putGround(entireImage)
entireImage.save("./coverBg.png")

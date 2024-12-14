from PIL import Image

def addBackground(base: Image.Image) -> Image.Image:
    forest = Image.open("./backgroundColorForest.png")
    forest = forest.resize((720, int(forest.size[1] * 720 / forest.size[0])))
    base.paste(forest,(0,420))
    return base

def addGround(base: Image.Image) -> Image.Image:
    grassMid = Image.open("./grassMid.png")
    grassCentre = Image.open("./grassCenter.png")
    for i in range(0,11):
        base.paste(grassMid,(i*70,940))
        for j in range(0,9):
            base.paste(grassCentre,(i*70,1010+j*70))
    return base


entireBackground = Image.new("RGB",(720,1640),color=(207,239,252))
entireBackground = addBackground(entireBackground)
entireBackground = addGround(entireBackground)
entireBackground.save("background.png")
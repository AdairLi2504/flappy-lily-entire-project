from PIL import Image
import random

def shroomKind():
    shroom = ["Brown","Tan"]
    alt = "Alt" if random.random() < 0.5 else ""
    return "shroom" + shroom[random.randrange(len(shroom))] + alt 

def genShroom(base:Image.Image) -> Image.Image:
    shroomName = shroomKind()
    alt = "Alt" if random.random() < 0.5 else ""
    Left = Image.open("./Mushroom expansion/PNG/"+shroomName+"Left.png")
    Mid = Image.open("./Mushroom expansion/PNG/"+shroomName+"Mid"+alt+".png")
    Right = Image.open("./Mushroom expansion/PNG/"+shroomName+"Right.png")
    base.paste(Left,(0,0))
    base.paste(Right,(38,0))
    base.paste(Mid,(19,0))
    return base

def genMushroom() -> Image.Image:
    mushroomBase = Image.new("RGB",(108,950),color="black")
    mushroomBase = genShroom(mushroomBase)
    topName = "stemTop.png" if random.random() < 0.5 else "stemTopAlt.png"
    top = Image.open("./Mushroom expansion/PNG/"+topName)
    mushroomBase.paste(top,(19,40))
    stemNames = ["Crown","Shroom","Vine"]
    for i in range(0,12):
        name = "stem.png" if  random.random() < 0.6 else ("stem"+stemNames[random.randrange(len(stemNames))]+".png")
        j = Image.open("./Mushroom expansion/PNG/"+name)
        mushroomBase.paste(j,(19,110+i*70))
    return mushroomBase

def convertTransparent(datas):
    newData = [] 
    for item in datas:
        if (item[0] == 0 and item[1] == 0 and item[2] == 0) or (item[0] == 255 and item[1] == 255 and item[2] == 255): 
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item) 
    return newData

for i in range(0,12):
    mushroom = genMushroom()
    mushroom_res = mushroom.convert("RGBA")
    mushroom_datas = mushroom_res.getdata()
    mushroom_datas = convertTransparent(mushroom_datas)
    mushroom_res.putdata(mushroom_datas)
    mushroom_res.save("mushroom"+str(i)+".png","PNG")

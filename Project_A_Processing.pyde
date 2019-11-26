add_library("sound")

def setup():
    global bgs
    
    size(1500, 900)
    bgs = SoundFile(this, "Ancient Egyptian Music - Prince of Egypt.mp3")
    

def draw():
    global bgs
    
    img = loadImage("pyramid.png")
    
    img.resize(width, height)
    background(img)
    

    font = createFont("blackcherry.TTF", 100)
    textFont(font)
    textAlign(CENTER, CENTER)
    text("Dunes & Deserts", width / 2, height / 2)

    
    textSize(50)
    text("{                    }", width / 2, 770)
    text("Start Game", width / 2, 775)
    
    bgs.play()
    bgs.loop()

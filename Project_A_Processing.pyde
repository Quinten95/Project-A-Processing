add_library("sound")
frames = []

def setup():
    global bgs, isMouseWithinSpace, gifWidth, gifHeight, value
    gifWidth = 400
    gifHeight = 200
    value = 255
    
    for i in range(0, 74):
        frames.append(loadImage("frame_" + (str(i) if i >= 10 else "0" + str(i)) + "_delay-0.03s.jpg"))
            
    backgroundMusic()

    size(1500,900)
    frameRate(60)
    
    global images
    images = list()
    images.append(loadImage("pyramid.png"))
    
def backgroundMusic():
    bgs = SoundFile(this, "Ancient Egyptian Music - Prince of Egypt.mp3")
    bgs.play()
    bgs.loop()

def draw():
    global bgs, isMouseWithinSpace, gifWidth, gifHeight, images
    
    
    # img = loadImage("pyramid.png")
    images[0].resize(width, height)
    background(images[0])
    
    # gif = loadImage("fallingstar.gif")
    # gif.resize(gifWidth, gifHeight)
    # image(gif, 0, 0)
    
    # gif2 = loadImage("fallingstar.gif")
    # gif2.resize(gifWidth, gifHeight)
    # image(gif2, 1100, 0)
    
    
    image(frames[frameCount%74], 0, 0, 200, 200) #8 veranderen in aantal afbeeldingen 73 or 74.
    image(frames[frameCount%74], 1000, 10, 150, 100)
    image(frames[frameCount%74], 500, 0, 500, 100)
    image(frames[frameCount%74], 1300, 40, 500, 100)

    font = createFont("blackcherry.TTF", 100)
    textFont(font)
    textAlign(CENTER, CENTER)
    fill(255)
    text("Dunes & Deserts", width / 2, height / 2)

    textSize(50)
    text("{                    }", width / 2, 770)
    text("Start Game", width / 2, 775)
    
    textSize(38)
    text("Exit", 1425, 850)
    textFont(font)
    
    textSize(70)
    fill(value)
    text(">", 60, 840)
    
    
    if value == 0:
        textSize(70)
        fill(255)
        text("^", 60, 840)
        textSize(50)
        
        fill(35)
        rect(32, 700, 55, 125, 7)
        noStroke()
        
        fill(255)
        text("+", 60, 720)
        text("-", 60, 790)
        

    
    def isMouseWithinSpace(x, y, breedte, hoogte):
        if x < mouseX < x + breedte and y < mouseY < y + hoogte:
            return True
        else:
            return False
    
    
    #fill(255)
    #text(str(millis()) + "  " + str(millis()//62%8), 100, 100)
    
def mousePressed():
    global isMouseWithinSpace, value, bgs

    if isMouseWithinSpace(1390, 850, 70, 18):
        exit()                                   #Exit Button
        
    if isMouseWithinSpace(625, 770, 275, 20):
        pass                                     #Start Game Button
    if isMouseWithinSpace(50, 850, 25, 20):
        if value == 0:
            value = 255
        else:
            value = 0
    
    if value == 0:
        if isMouseWithinSpace(60, 720, 10, 10):
            pass
        if isMouseWithinSpace(60, 690, 10, 10):
            pass
        

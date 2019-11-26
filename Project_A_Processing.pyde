card_select_screen = True
screenWidth = 1500 
screenHeight = 900
def setup():
    global screenWidth, screenHeight
    size(screenWidth, screenHeight)

def draw():
    global card_select_screen
    
    background(230, 230, 230)
    
    if card_select_screen == True:
        card_select()
    else:
        pass

def card_select():
    
    

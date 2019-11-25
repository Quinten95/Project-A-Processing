number_of_players = 3
show_how_many_players = True

def setup():
    size(1000, 800)

def draw():
    global show_how_many_players
    background(230, 230, 230)
    
    if show_how_many_players == True:
        how_many_players()

#Asks the user how many players are playing the game at the moment and stores that in a variable.
def how_many_players():
    global question, number_of_players, show_how_many_players
    question = "Met hoeveel spelers speelt u?"
    
    font1 = createFont("Arial", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(0,0,0)
    text(question, 500, 100)
    
    init_buttons()
    
    
#creates the buttons for the how_many_players screen
def init_buttons():
    global number_of_players
    
    fill(255,255,255)
    rect(470, 550, 60, 40)    
    fill(0,0,0)
    text(str(number_of_players), 500, 582)
    
    fill(200, 0, 0)
    rect(400, 600, 60, 40)    
    fill(0,0,0)
    text("-", 430, 630)
    
    fill(0, 200, 0)
    rect(540, 600, 60, 40)    
    fill(0,0,0)
    text("+", 570, 632)
    
    fill(255,255,255)
    rect(470, 600, 60, 40)    
    fill(0,0,0)
    text("OK", 500, 632)

#Creates textboxes for the players from the amount of players variable, to input their names and store them in a player variable
def initiate_textbox():    
    background(230, 230, 230)
    text("Player 1:", 20, 100)
    fill(0,0,0)

#Handles all the clicking of buttons in the program
def mousePressed():
    global number_of_players, show_how_many_players
    if show_how_many_players == True:
        if (mouseX >= 400 and mouseX <= 460) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players > 3:
                number_of_players -= 1
        elif (mouseX >= 540 and mouseX <= 600) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players < 6:
                number_of_players += 1
        elif (mouseX >= 470 and mouseX <= 530) and (mouseY >= 600 and mouseY <= 640):
            show_how_many_players = False

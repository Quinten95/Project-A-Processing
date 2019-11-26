number_of_players = 3
name_input_screen_display = False
how_many_players_screen = True

def setup():    
    size(1000, 800)
    
    
def draw():
    global how_many_players_screen, name_input_screen_display
    
    background(230, 230, 230)
    
    if how_many_players_screen == True:
        how_many_players()
    elif name_input_screen_display == True:
        name_input_screen()
    else:
        pass
        

#Asks the user how many players are playing the game at the moment and stores that in a variable.
def how_many_players():
    global question, number_of_players, how_many_players_screen
    question = "Met hoeveel spelers speelt u?"
    
    font1 = createFont("Arial", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(0,0,0)
    text(question, 500, 100)
    
    initiate_buttons()
    
    
#creates the buttons for the how_many_players screen
def initiate_buttons():
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
def name_input_screen():
    global number_of_players, name_input_screen_display
    font1 = createFont("Arial", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(0,0,0)
    text("Number of players: " + str(number_of_players), 500, 300)
    

#Handles all the clicking of buttons in the program
def mousePressed():
    global number_of_players, how_many_players_screen, name_input_screen_display
    if how_many_players_screen == True:
        if (mouseX >= 400 and mouseX <= 460) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players > 3:
                number_of_players -= 1
        elif (mouseX >= 540 and mouseX <= 600) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players < 6:
                number_of_players += 1
        elif (mouseX >= 470 and mouseX <= 530) and (mouseY >= 600 and mouseY <= 640):
            name_input_screen_display = True
            how_many_players_screen = False

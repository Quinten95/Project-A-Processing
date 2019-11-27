number_of_players = 3

how_many_players_screen = True
name_input_screen_display = False
main_screen_display = False

screenWidth = 1500
screenHeight = 900

player1_box_selected = False
player2_box_selected = False
player3_box_selected = False
player4_box_selected = False
player5_box_selected = False
player6_box_selected = False

player1_name = ''
player2_name = ''
player3_name = ''
player4_name = ''
player5_name = ''
player6_name = ''

def setup():
    global screenWidth, screenHeight 
    size(screenWidth, screenHeight)
    
    
def draw():
    global how_many_players_screen, name_input_screen_display
    
    background(229, 180, 73)
    
    #Checks which screen should be active atm
    if how_many_players_screen == True:
        how_many_players()
    elif name_input_screen_display == True:
        name_input_screen()
    elif main_screen_display == True:
        main_screen()
        

#Asks the user how many players are playing the game at the moment and stores that in a variable.
def how_many_players():
    global question, number_of_players, how_many_players_screen
    question = "Met hoeveel spelers speelt u?"
    
    font1 = createFont("Arial", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(0,0,0)
    text(question, screenWidth/2, 100)
    
    initiate_buttons()
    
    
#creates the buttons for the how_many_players screen
def initiate_buttons():
    global number_of_players, screenWidth, screenHeight
    
    fill(255,255,255)
    rect(720, 550, 60, 40)    
    fill(0,0,0)
    text(str(number_of_players), 750, 582)
    
    fill(200, 0, 0)
    rect(650, 600, 60, 40)    
    fill(0,0,0)
    text("-", 680, 630)
    
    fill(0, 200, 0)
    rect(790, 600, 60, 40)    
    fill(0,0,0)
    text("+", 820, 632)
    
    fill(255,255,255)
    rect(720, 600, 60, 40)    
    fill(0,0,0)
    text("OK", 750, 632)

#Creates textboxes for the players from the amount of players variable, to input their names and store them in a player variable
def name_input_screen():
    global number_of_players, name_input_screen_display
    global player1_name, player2_name, player3_name, player4_name, player5_name, player6_name
    
    font1 = createFont("Arial", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(0,0,0)
    text("Number of players: " + str(number_of_players), screenWidth/2, 100)
    
    x = number_of_players
    YPositionRect = 200
    YPositionText = 232
    y = player_number = 1
    
    while x > 0:        
        fill(255,255,255)
        rect(690, YPositionRect, 250, 40)    
        fill(0,0,0)
        text("Player "+ str(y)+": ", 610, YPositionText)
        x -= 1
        YPositionRect += 100
        YPositionText += 100
        y += 1
        
    if player1_box_selected == True:
        fill(230, 230, 230)
        rect(690, 200, 250, 40)
    elif player2_box_selected == True:
        fill(230, 230, 230)
        rect(690, 300, 250, 40)
    elif player3_box_selected == True:
        fill(230, 230, 230)
        rect(690, 400, 250, 40)
    elif player4_box_selected == True:
        fill(230, 230, 230)
        rect(690, 500, 250, 40)
    elif player5_box_selected == True:
        fill(230, 230, 230)
        rect(690, 600, 250, 40)
    elif player6_box_selected == True:
        fill(230, 230, 230)
        rect(690, 700, 250, 40)
    
    font1 = createFont("Arial", 30)
    textFont(font1)
    fill(0, 0, 0)    
    textAlign(LEFT)
    text(player1_name, 700, 232)    
    text(player2_name, 700, 332)    
    text(player3_name, 700, 432)    
    text(player4_name, 700, 532)    
    text(player5_name, 700, 632)    
    text(player6_name, 700, 732)
    
    textAlign(CENTER)
    fill(255,255,255)
    rect(720, 800, 60, 40)    
    fill(0,0,0)
    text("OK", 750, 832)
    

def main_screen():    
    font1 = createFont("Arial", 30)
    textFont(font1)
    fill(0, 0, 0)    
    textAlign(CENTER)
    
    x = 0
    YPositionText = 80
    y = player_number = 1
    
    player_names = [player1_name, player2_name, player3_name, player4_name, player5_name, player6_name]
    
    while x < 3:
        text("Player "+ str(y)+": " + player_names[x], 200, YPositionText)
        x += 1
        y += 1
        YPositionText += 250
    
    YPositionText = 80
    while x < 6:
        text("Player "+ str(y)+": " + player_names[x], 1000, YPositionText)
        x += 1
        y += 1
        YPositionText += 250
        
    
    
#Handles all the clicking of buttons in the program
def mousePressed():
    global number_of_players, how_many_players_screen, name_input_screen_display, main_screen_display
    global player1_box_selected, player2_box_selected, player3_box_selected
    global player4_box_selected, player5_box_selected, player6_box_selected
    if how_many_players_screen == True:
        if (mouseX >= 650 and mouseX <= 710) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players > 3:
                number_of_players -= 1
        elif (mouseX >= 790 and mouseX <= 850) and (mouseY >= 600 and mouseY <= 640):
            if number_of_players < 6:
                number_of_players += 1
        elif (mouseX >= 720 and mouseX <= 780) and (mouseY >= 600 and mouseY <= 640):
            name_input_screen_display = True
            how_many_players_screen = False
    
    elif name_input_screen_display == True:
        #Checks if the user has clicked on a certain textbox to begin input
        if (mouseX >= 690 and mouseX <= 940) and (mouseY >= 200 and mouseY <= 240):
            player1_box_selected = True
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False        
        elif (mouseX >= 690 and mouseX <= 940) and (mouseY >= 300 and mouseY <= 340):
            player1_box_selected = False
            player2_box_selected = True
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False            
        elif (mouseX >= 690 and mouseX <= 940) and (mouseY >= 400 and mouseY <= 440):
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = True
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False        
        elif ((mouseX >= 690 and mouseX <= 940) and (mouseY >= 500 and mouseY <= 540)) and number_of_players > 3:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = True
            player5_box_selected = False
            player6_box_selected = False        
        elif ((mouseX >= 690 and mouseX <= 940) and (mouseY >= 600 and mouseY <= 640)) and number_of_players > 4:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = True
            player6_box_selected = False            
        elif ((mouseX >= 690 and mouseX <= 940) and (mouseY >= 700 and mouseY <= 740)) and number_of_players > 5:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = True
            
        #Detects wheter the OK button has been pressed
        elif (mouseX >= 720 and mouseX <= 780) and (mouseY >= 800 and mouseY <= 840):
            name_input_screen_display = False
            main_screen_display = True                        
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False
            
        else:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False
            

def keyPressed():
    global player1_name, player2_name, player3_name, player4_name, player5_name, player6_name
    global player1_box_selected, player2_box_selected, player3_box_selected
    global player4_box_selected, player5_box_selected, player6_box_selected
    
    #Checks if the key pressed is a letter and if so adds it to the player whose textbox is currently selected
    if (key == 'a' or key == 'A' 
        or key == 'b' or key == 'B' 
        or key == 'c' or key == 'C'
        or key == 'd' or key == 'D'
        or key == 'e' or key == 'E' 
        or key == 'f' or key == 'F' 
        or key == 'g' or key == 'G'
        or key == 'h' or key == 'H'
        or key == 'i' or key == 'I' 
        or key == 'j' or key == 'J' 
        or key == 'k' or key == 'K'
        or key == 'l' or key == 'L'
        or key == 'm' or key == 'M' 
        or key == 'n' or key == 'N' 
        or key == 'o' or key == 'O'
        or key == 'p' or key == 'P'
        or key == 'q' or key == 'Q' 
        or key == 'r' or key == 'R' 
        or key == 's' or key == 'S'
        or key == 't' or key == 'T'
        or key == 'u' or key == 'U' 
        or key == 'v' or key == 'V' 
        or key == 'w' or key == 'W'
        or key == 'x' or key == 'X' 
        or key == 'y' or key == 'Y' 
        or key == 'z' or key == 'Z' 
        or key =='\b' or keyCode == 32):
        
        if (player1_box_selected == True) and (key != '\b'):
            player1_name += key
        elif (player1_box_selected == True) and (key == '\b'):
            player1_name = player1_name[:-1]
        
        elif (player2_box_selected == True) and (key != '\b'):
            player2_name += key
        elif (player2_box_selected == True) and (key == '\b'):
            player2_name = player2_name[:-1]
        
        elif (player3_box_selected == True) and (key != '\b'):
            player3_name += key
        elif (player3_box_selected == True) and (key == '\b'):
            player3_name = player3_name[:-1]
        
        elif (player4_box_selected == True) and (key != '\b'):
            player4_name += key
        elif (player4_box_selected == True) and (key == '\b'):
            player4_name = player4_name[:-1]
        
        elif (player5_box_selected == True) and (key != '\b'):
            player5_name += key
        elif (player5_box_selected == True) and (key == '\b'):
            player5_name = player5_name[:-1]
        
        elif (player6_box_selected == True) and (key != '\b'):
            player6_name += key
        elif (player6_box_selected == True) and (key == '\b'):
            player6_name = player6_name[:-1]
    

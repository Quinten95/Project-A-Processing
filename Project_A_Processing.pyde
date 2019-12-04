number_of_players = 3

show_start_screen = True
how_many_players_screen = False
name_input_screen_display = False
main_screen_display = False
show_cards_display = False

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

player1_fieldcards = []
player2_fieldcards = []
player3_fieldcards = []
player4_fieldcards = []
player5_fieldcards = []
player6_fieldcards = []

player1_trapcards = []
player2_trapcards = []
player3_trapcards = []
player4_trapcards = []
player5_trapcards = []
player6_trapcards = []

fieldcard_list = []
trapcard_list = []

player_card_list_g = []
player_name_g = ''

add_library("sound")
frames = []


def setup():
    global screenWidth, screenHeight, frame_count_main    
    global bgs, isMouseWithinSpace, gifWidth, gifHeight, value
    
    size(screenWidth, screenHeight)
    init_field_cards()
    frame_count_main = 0
    
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
    
    
def draw():
    global how_many_players_screen, name_input_screen_display, main_screen_display, show_cards_display
    global player_name_g, player_card_list_g
    
    background(148, 120, 214)
    
    #Checks which screen should be active atm
    if show_start_screen == True:
        start_screen()
    elif how_many_players_screen == True:
        how_many_players()
    elif name_input_screen_display == True:
        name_input_screen()
    elif main_screen_display == True:
        main_screen()
    elif show_cards_display == True:
        show_cards()
        

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
    
#Creates the main playing screen in which players can choose to draw a random card
#the cards per player are shown
#and players can use a card in their posession
def main_screen():
    global player_starting, frame_count_main
    font1 = createFont("Arial", 30)    
    font2 = createFont("Arial", 75)
    font3 = createFont("Arial", 20)
    font4 = createFont("Arial", 35)
    
    x = 0
    YPositionText = 150
    YPositionRect = 180
    y = player_number = 1
    
    player_names = [player1_name, player2_name, player3_name, player4_name, player5_name, player6_name]
    
    
    
    if frame_count_main < 900:
        fill(0, 0, 0)
        textAlign(CENTER)
        textFont(font4) 
        text(player_names[player_starting] + " begint!", screenWidth/2, 100)
    
    
    while x < 3:
        fill(0, 0, 0)
        textAlign(LEFT)
        textFont(font1) 
        text("Player "+ str(y)+": " + player_names[x], 100, YPositionText)
        
        textFont(font2)
        textAlign(CENTER)    
        fill(230,230,230)
        rect(100, YPositionRect, 80, 80)
        fill(0,0,0)
        text("?", 140, YPositionRect+65)
        
        fill(230,230,230)
        rect(190, YPositionRect, 80, 80)
        fill(0,0,0)
        text("!", 230, YPositionRect+65)
        
        fill(230,230,230)
        rect(290, YPositionRect, 80, 80)
        fill(0,0,0)
        textFont(font3)
        text("Kaarten", 331, YPositionRect+44)
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233        
        frame_count_main += 1
    
    YPositionText = 150
    YPositionRect = 180
    
    while x < number_of_players:
        fill(0,0,0)        
        textAlign(LEFT)
        textFont(font1)
        text("Player "+ str(y)+": " + player_names[x], 750, YPositionText)
        
        textFont(font2)
        textAlign(CENTER)        
        fill(230,230,230)
        rect(750, YPositionRect, 80, 80)
        fill(0,0,0)
        text("?", 790, YPositionRect+65)
        
        fill(230,230,230)
        rect(840, YPositionRect, 80, 80)
        fill(0,0,0)
        text("!", 880, YPositionRect+65)
        
        fill(230,230,230)
        rect(930, YPositionRect, 80, 80)
        fill(0,0,0)
        textFont(font3)
        text("Kaarten", 971, YPositionRect+44)
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233


def show_cards():
    global player_card_list_g, player_name_g
    font1 = createFont("Arial", 30)
    font2 = createFont("Arial", 20)
    textAlign(CENTER)
    fill(0,0,0)
    textFont(font1)
    text("Kaarten van " + player_name_g + ":", screenWidth/2, 100) 
    
    textX = 100
    textY = 200
    buttonX = 1100
    buttonY = 220
    x = 1
    
    fill(230,230,230)
    rect(1300, 90, 140, 40)
    fill(0,0,0)
    text("Terug", 1370, 122)
    
    for i in player_card_list_g:
        textAlign(LEFT)
        fill(0,0,0)
        textFont(font1)
        text("Kaart " + str(x) + ":", textX, textY)
        
        textFont(font2)
        text(i, textX, textY + 30)
        
        fill(230,230,230)
        rect(buttonX, buttonY, 160, 40)   
        fill(0,0,0)
        textAlign(CENTER)     
        textFont(font1)
        text("Gebruik!", buttonX + 80, buttonY + 31)
    
        
        
        
        buttonY += 180
        textY += 180
        x += 1
        
    
#Handles all the clicking of buttons in the program
def mousePressed():
    global show_start_screen, number_of_players, how_many_players_screen, name_input_screen_display, main_screen_display
    global player1_box_selected, player2_box_selected, player3_box_selected
    global player4_box_selected, player5_box_selected, player6_box_selected
    global player1_fieldcards, player2_fieldcards, player3_fieldcards, player4_fieldcards, player5_fieldcards, player6_fieldcards
    global fieldcard_list, fieldCard1, fieldCard2, fieldCard3, fieldCard4, fieldCard5, fieldCard6
    global duelCard7, duelCard8, duelCard9, duelCard10, duelCard11, duelCard12
    global trapCard_list, trapCard1, trapCard2, trapCard3, trapCard4, trapCard5
    global player_card_list_g, player_name_g, show_cards_display, player_starting
    global isMouseWithinSpace, value, bgs
    
    if show_start_screen == True:
        if isMouseWithinSpace(1390, 850, 70, 18):
            exit()                                   #Exit Button
        
        if isMouseWithinSpace(625, 770, 275, 20):
            how_many_players_screen = True
            show_start_screen = False                                    #Start Game Button
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
    
    elif how_many_players_screen == True:
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
            player_starting = int(random(0,number_of_players-1))
            
        else:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False
    
    elif main_screen_display == True:
        if (mouseX >= 100 and mouseX <= 180) and (mouseY >= 180 and mouseY <= 260):
            if len(fieldcard_list) > 0:
                player1_fieldcards.append(generate_field_card())        
        
        elif (mouseX >= 100 and mouseX <= 180) and (mouseY >= 413 and mouseY <= 493):
            if len(fieldcard_list) > 0:
                player2_fieldcards.append(generate_field_card())
                
        elif (mouseX >= 100 and mouseX <= 180) and (mouseY >= 646 and mouseY <= 726):
            if len(fieldcard_list) > 0:
                player3_fieldcards.append(generate_field_card())
            
        elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
            if len(fieldcard_list) > 0:
                player4_fieldcards.append(generate_field_card())
        
        elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
            if len(fieldcard_list) > 0:
                player5_fieldcards.append(generate_field_card())
        
        elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
            if len(fieldcard_list) > 0:
                player6_fieldcards.append(generate_field_card())
                
        elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 180 and mouseY <= 260):
            if len(trapcard_list) > 0:
                player1_trapcards.append(generate_trap_card())
                
        elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 413 and mouseY <= 493):
            if len(trapcard_list) > 0:
                player2_trapcards.append(generate_trap_card())
                
        elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 646 and mouseY <= 726):
            if len(trapcard_list) > 0:
                player3_trapcards.append(generate_trap_card())
                
        elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
            if len(trapcard_list) > 0:
                player4_trapcards.append(generate_trap_card())
        
        elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
            if len(trapcard_list) > 0:
                player5_trapcards.append(generate_trap_card())
        
        elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
            if len(trapcard_list) > 0:
                player6_trapcards.append(generate_trap_card())
                
        elif (mouseX >= 280 and mouseX <= 370) and (mouseY >= 180 and mouseY <= 260):  
            player_card_list_g = player1_fieldcards + player1_trapcards 
            player_name_g = player1_name
                  
            show_cards_display = True
            main_screen_display = False
              
        elif (mouseX >= 280 and mouseX <= 370) and (mouseY >= 413 and mouseY <= 493):  
            player_card_list_g = player2_fieldcards + player2_trapcards 
            player_name_g = player2_name
                  
            show_cards_display = True
            main_screen_display = False
              
        elif (mouseX >= 280 and mouseX <= 370) and (mouseY >= 646 and mouseY <= 726):  
            player_card_list_g = player3_fieldcards + player3_trapcards 
            player_name_g = player3_name
                  
            show_cards_display = True
            main_screen_display = False
              
        elif ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
            player_card_list_g = player4_fieldcards + player4_trapcards 
            player_name_g = player4_name
                  
            show_cards_display = True
            main_screen_display = False
        
        elif ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
            player_card_list_g = player5_fieldcards + player5_trapcards 
            player_name_g = player5_name
            
            show_cards_display = True
            main_screen_display = False
        
        elif ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
            player_card_list_g = player6_fieldcards + player6_trapcards 
            player_name_g = player6_name
            
            show_cards_display = True
            main_screen_display = False
    
    elif show_cards_display == True:
        if (mouseX >= 1300 and mouseX <= 1440) and (mouseY >= 90 and mouseY <= 130):
            main_screen_display = True
            show_cards_display = False
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 220 and mouseY <= 260) and len(player_card_list_g) > 0:
            if player_card_list_g[0] in player1_fieldcards:                
                player1_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player1_trapcards:                
                player1_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[0] in player2_fieldcards:                
                player2_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player2_trapcards:                
                player2_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[0] in player3_fieldcards:                
                player3_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player3_trapcards:                
                player3_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[0] in player4_fieldcards:                
                player4_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player4_trapcards:                
                player4_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[0] in player5_fieldcards:                
                player5_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player5_trapcards:                
                player5_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[0] in player6_fieldcards:                
                player6_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[0] in player6_trapcards:                
                player6_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 400 and mouseY <= 440) and len(player_card_list_g) > 1:
            if player_card_list_g[1] in player1_fieldcards:                
                player1_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player1_trapcards:                
                player1_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))            
            elif player_card_list_g[1] in player2_fieldcards:                
                player2_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player2_trapcards:                
                player2_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))            
            elif player_card_list_g[1] in player3_fieldcards:                
                player3_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player3_trapcards:                
                player3_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))            
            elif player_card_list_g[1] in player4_fieldcards:                
                player4_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player4_trapcards:                
                player4_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))            
            elif player_card_list_g[1] in player5_fieldcards:                
                player5_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player5_trapcards:                
                player5_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))            
            elif player_card_list_g[1] in player6_fieldcards:                
                player6_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
            elif player_card_list_g[1] in player6_trapcards:                
                player6_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 580 and mouseY <= 620) and len(player_card_list_g) > 2:
            if player_card_list_g[2] in player1_fieldcards:                
                player1_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player1_trapcards:                
                player1_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[2] in player2_fieldcards:                
                player2_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player2_trapcards:                
                player2_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[2] in player3_fieldcards:                
                player3_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player3_trapcards:                
                player3_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[2] in player4_fieldcards:                
                player4_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player4_trapcards:                
                player4_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[2] in player5_fieldcards:                
                player5_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player5_trapcards:                
                player5_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[2] in player6_fieldcards:                
                player6_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[2] in player6_trapcards:                
                player6_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 760 and mouseY <= 800) and len(player_card_list_g) > 3:
            if player_card_list_g[3] in player1_fieldcards:                
                player1_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player1_trapcards:                
                player1_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player2_fieldcards:                
                player2_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player2_trapcards:                
                player2_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player3_fieldcards:                
                player3_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player3_trapcards:                
                player3_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player4_fieldcards:                
                player4_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player4_trapcards:                
                player4_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player5_fieldcards:                
                player5_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player5_trapcards:                
                player5_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player6_fieldcards:                
                player6_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
            elif player_card_list_g[3] in player6_trapcards:                
                player6_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))
            
              

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
            if len(player1_name) < 10:
                player1_name += key
        elif (player1_box_selected == True) and (key == '\b'):
            player1_name = player1_name[:-1]
        
        elif (player2_box_selected == True) and (key != '\b'):
            if len(player2_name) < 10:
                player2_name += key
        elif (player2_box_selected == True) and (key == '\b'):
            player2_name = player2_name[:-1]
        
        elif (player3_box_selected == True) and (key != '\b'):
            if len(player3_name) < 10:
                player3_name += key
        elif (player3_box_selected == True) and (key == '\b'):
            player3_name = player3_name[:-1]
        
        elif (player4_box_selected == True) and (key != '\b'):
            if len(player4_name) < 10:
                player4_name += key
        elif (player4_box_selected == True) and (key == '\b'):
            player4_name = player4_name[:-1]
        
        elif (player5_box_selected == True) and (key != '\b'):
            if len(player5_name) < 10:
                player5_name += key
        elif (player5_box_selected == True) and (key == '\b'):
            player5_name = player5_name[:-1]
        
        elif (player6_box_selected == True) and (key != '\b'):
            if len(player6_name) < 10:
                player6_name += key
        elif (player6_box_selected == True) and (key == '\b'):
            player6_name = player6_name[:-1]

#generates all the cards for the game and puts them in the correct list
def init_field_cards():
    global fieldcard_list, fieldCard1, fieldCard2, fieldCard3, fieldCard4, fieldCard5, fieldCard6
    global duelCard7, duelCard8, duelCard9, duelCard10, duelCard11, duelCard12
    global trapcard_list, trapCard1, trapCard2, trapCard3, trapCard4, trapCard5
    
    fieldCard1 = "Het is monsoon seizoen en door het regen zijn alle wegen versperd door drijfzand.\nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard2 = "Door gebruik te maken van een magische spreuk vallen alle tegenstanders in slaap.\nEen bijwerking van de spreuk zorgt ervoor dat wanneer de tegenstanders wakker worden, \nde gebruiker ook in slaap valt. \nDe tegenstanders slaan een beurt over, volgende beurt slaat de gebruiker een beurt over."
    fieldCard3 = "Je bent met je goede been uit bed gestapt. \nJe hebt het gevoel dat je meer kunt bewegen dan normaal. \nVoor deze beurt gebruik je een extra dobbelsteen om te bewegen. "
    fieldCard4 = "Door een magische spreuk ruil je plaatsen met een van je tegenstanders. \nJe tegenstander landt precies waar jij was, maar jij valt van 10 meter boven de grond. \nJe landt op een pijnlijke manier en moet uitrusten om verder te gaan. \nRuil plaats met gekozen tegenstander en sla een beurt over. "
    fieldCard5 = "Door een vloek hebben alle spelers een rot humeur. \nNiemand heeft zin om verder te gaan. \nZe doen het minimale van wat hun verwacht wordt. \nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard6 = "Door een magische spreuk kun je door een spiegel de kaarten van je tegenstander bekijken. \nHet nadeel is dat je tegenstander ook jouw kaarten kan zien, omdat de spiegel van beide kanten werkt. \nGebruiker en tegenstander tonen hun kaarten aan elkaar."
    duelCard7 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. \nDe aanvaller mag maar een dobbelsteen gebruiken."
    duelCard8 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. \nHierdoor zul je niet makkelijk verliezen. \nDe verdediger mag twee dobbelstenen gebruiken."
    duelCard9 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. \nDe aanvaller en de verdediger gebruiken een extra dobbelsteen."
    duelCard10 = "Tijdens het gevecht gooi je zand in het gezicht van je tegenstander. \nJe tegenstander kan je moeilijk zien, waardoor zijn kans van winnen minder wordt. \nVerminder het uiteindelijke getal van je tegenstander met 1."
    duelCard11 = "Tijdens het gevecht maakt je tegenstander een misstap en zit tijdelijk vast in drijfzand. \nJe tegenstander kan zich moeilijk bewegen, waardoor je kans van winnen groter wordt. \nVerhoog het uiteindelijke getal van de gebruiker met 1."
    duelCard12 = "Je vindt dat het gevecht niet was gegaan zoals je wilde. \nJe vraagt je tegenstander voor nog een gevecht. \nJe blijft zeuren totdat je tegenstander met tegenzin accepteert, \nmet als conditie dat 2 voorwerpen worden terug gelegd. \nForceer een rematch met 2 voorwerpen als prijs."
    
    fieldcard_list = [fieldCard1, fieldCard2, fieldCard3, fieldCard4, fieldCard5, fieldCard6, duelCard7, duelCard8, duelCard9, duelCard10, duelCard11, duelCard12]
    
    trapCard1 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. \nSla een beurt over."
    trapCard2 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard3 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, \nmaar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. \nNa een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. \nEen hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard4 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. \nJe komt erachter dat een van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
    trapCard5 = "Door een magische spreuk ruilen alle spelers plaatsen met elkaar. \nJe tegenstanders landen veilig op hun plaats, maar jij valt van 20 meter boven de grond. \nJe landt op je hoofd en bent buiten bewustzijn. Je wordt pas na een hele dag wakker. \nAlle spelers ruilen plaatsen met elkaar en sla twee beurten over."
    
    trapcard_list = [trapCard1, trapCard2, trapCard3, trapCard4, trapCard5]

#when this function is called it returns a card from the list of field cards and then removes it, so it can't be picked by another player
def generate_field_card():    
    chosenFieldNumber = int(random(0, len(fieldcard_list) - 1))
    
    if len(fieldcard_list) > 0:
        chosenFieldCard = fieldcard_list[chosenFieldNumber]
        fieldcard_list.pop(chosenFieldNumber)    
        return chosenFieldCard
    else:
        pass
    
#when this function is called it returns a card from the list of trap cards and then removes it, so it can't be picked by another player
def generate_trap_card():
    chosenTrapNumber = int(random(0, len(trapcard_list) - 1))
    
    if len(trapcard_list) > 0:
        chosenTrapCard = trapcard_list[chosenTrapNumber]
        trapcard_list.pop(chosenTrapNumber)    
        return chosenTrapCard
    else:
        pass

    
def backgroundMusic():
    bgs = SoundFile(this, "Ancient Egyptian Music - Prince of Egypt.mp3")
    bgs.play()
    bgs.loop()

def start_screen():
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

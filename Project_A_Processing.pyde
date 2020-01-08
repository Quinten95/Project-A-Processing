number_of_players = 3

show_start_screen = True
how_many_players_screen = False
name_input_screen_display = False
main_screen_display = False
show_cards_display = False

begin_ok_button = False
show_manual_display = False
show_empty_name_error = False


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

player_names = []
player_starting = 0

add_library("sound")
frames = []
side = -1
side2 = -1
number_of_dices = 1

player1millis = -3001
player2millis = -3001
player3millis = -3001
player4millis = -3001
player5millis = -3001
player6millis = -3001

player1_cardtotal = 0
player2_cardtotal = 0
player3_cardtotal = 0
player4_cardtotal = 0
player5_cardtotal = 0
player6_cardtotal = 0


def setup():
    global screenWidth, screenHeight
    global bgs, bgsVolume, isMouseWithinSpace, gifWidth, gifHeight, value, s

    size(screenWidth, screenHeight)
    init_field_cards()
    
    side = int(random(1,7))
    
    gifWidth = 400
    gifHeight = 200
    value = 255
    
    for i in range(0, 74):
        frames.append(loadImage("frame_" + (str(i) if i >= 10 else "0" + str(i)) + "_delay-0.03s.jpg"))

    s = Sound(this)
            
    bgs = SoundFile(this, "Ancient Egyptian Music - Prince of Egypt.mp3")
    bgs.play()
    bgs.loop()
    bgsVolume = 1.0

    size(1500,900)
    frameRate(60)
    
    global images
    images = list()
    images.append(loadImage("pyramid.png"))
    images.append(loadImage("Player_Input.jpg"))
    images.append(loadImage("Name_Input.jpg"))
    images.append(loadImage("MainScreen.jpg"))
    images.append(loadImage("onlinehandleiding.png"))
    images.append(loadImage("sound_button.jpg"))
    images.append(loadImage("mute_button.jpg"))
    
    global dice1
    dice1 = list()
    dice1.append(loadImage("dice1.jpg"))
    dice1.append(loadImage("dice2.jpg"))
    dice1.append(loadImage("dice3.jpg"))
    dice1.append(loadImage("dice4.jpg"))
    dice1.append(loadImage("dice5.jpg"))
    dice1.append(loadImage("dice6.jpg"))
    
    global dice2
    dice2 = list()
    dice2.append(loadImage("dice1.jpg"))
    dice2.append(loadImage("dice2.jpg"))
    dice2.append(loadImage("dice3.jpg"))
    dice2.append(loadImage("dice4.jpg"))
    dice2.append(loadImage("dice5.jpg"))
    dice2.append(loadImage("dice6.jpg"))
    
def draw():
    global how_many_players_screen, name_input_screen_display, main_screen_display, show_cards_display
    global player_name_g, player_card_list_g
    global player1millis, player2millis, player3millis, player4millis, player5millis, player6millis
    
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
    elif show_manual_display == True:
        show_manual()

        
    
    if millis() < player1millis + 1500: 
        cardLimitText()
        text(str(player1_name) + " heeft al drie kaarten.", screenWidth/2, 850)
    if millis() < player2millis + 1500:  
        cardLimitText()
        text(str(player2_name) + " heeft al drie kaarten.", screenWidth/2, 850)
    if millis() < player3millis + 1500:
        cardLimitText() 
        text(str(player3_name) + " heeft al drie kaarten.", screenWidth/2, 850)
    if millis() < player4millis + 1500:
        cardLimitText() 
        text(str(player4_name) + " heeft al drie kaarten.", screenWidth/2, 850)
    if millis() < player5millis + 1500:
        cardLimitText()
        text(str(player5_name) + " heeft al drie kaarten.", screenWidth/2, 850)
    if millis() < player6millis + 1500:
        cardLimitText() 
        text(str(player6_name) + " heeft al drie kaarten.", screenWidth/2, 850)

#Asks the user how many players are playing the game at the moment and stores that in a variable.
def how_many_players():
    global question, number_of_players, how_many_players_screen    
    images[1].resize(width, height)
    background(images[1])
    question = "Met hoeveel spelers speelt u?"
    
    font1 = createFont("Courier", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(255,255,255)
    text(question, screenWidth/2, 100)

    text("Minimaal 3 spelers en maximaal 6 spelers", 750, 700)
    
    initiate_buttons()
    
    
#creates the buttons for the how_many_players screen
def initiate_buttons():
    global number_of_players, screenWidth, screenHeight
    
    fill(255,255,255)
    rect(720, 550, 60, 40, 6)    
    fill(0,0,0)
    text(str(number_of_players), 750, 582)
    
    fill(200, 0, 0)
    rect(650, 550, 60, 40, 6)       
    fill(0,0,0)
    text("-", 680, 580)
    
    fill(0, 200, 0)
    rect(790, 550, 60, 40, 6)      
    fill(0,0,0)
    text("+", 820, 580)
    
    fill(255,255,255)
    rect(720, 600, 60, 40, 6)    
    fill(0,0,0)
    text("OK", 750, 632)

#Creates textboxes for the players from the amount of players variable, to input their names and store them in a player variable
def name_input_screen():
    global number_of_players, name_input_screen_display, show_empty_name_error
    global player1_name, player2_name, player3_name, player4_name, player5_name, player6_name

    images[2].resize(width, height)
    background(images[2])
    
    font1 = createFont("Courier", 30)    
    font2 = createFont("Courier", 35)
    
    textFont(font1)
    textAlign(CENTER)
    fill(255,255,255)
    text("Number of players: " + str(number_of_players), screenWidth/2, 100)
    
    x = number_of_players
    YPositionRect = 200
    YPositionText = 232
    y = player_number = 1
    
    while x > 0:        
        fill(255,255,255)
        rect(690, YPositionRect, 250, 40, 6)

        text("Player "+ str(y)+": ", 610, YPositionText)
        x -= 1
        YPositionRect += 100
        YPositionText += 100
        y += 1
        
    if player1_box_selected == True:
        fill(230, 230, 230)
        rect(690, 200, 250, 40, 6)
    elif player2_box_selected == True:
        fill(230, 230, 230)
        rect(690, 300, 250, 40, 6)
    elif player3_box_selected == True:
        fill(230, 230, 230)
        rect(690, 400, 250, 40, 6)
    elif player4_box_selected == True:
        fill(230, 230, 230)
        rect(690, 500, 250, 40, 6)
    elif player5_box_selected == True:
        fill(230, 230, 230)
        rect(690, 600, 250, 40, 6)
    elif player6_box_selected == True:
        fill(230, 230, 230)
        rect(690, 700, 250, 40, 6)
    
    font1 = createFont("Courier", 30)
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
    rect(720, 800, 60, 40, 6)    
    fill(0,0,0)
    text("OK", 750, 832)
    
    if show_empty_name_error == True:            
        fill(155, 155, 155) 
        rect(screenWidth/2 - 450, screenHeight/2 - 40, 900, 80, 6)
        fill(255,255,255)
        rect(screenWidth/2 + 360, screenHeight/2 - 20, 60, 40, 6)
        textAlign(CENTER)
        textFont(font2) 
        fill(0,0,0)
        text("Voer voor alle spelers een naam in!", screenWidth/2 - 40, screenHeight/2 + 10)
        text("OK", screenWidth/2 + 390, screenHeight/2 + 10)
    
#Creates the main playing screen in which players can choose to draw a random card
#the cards per player are shown
#and players can use a card in their posession
def main_screen():
    global player_starting, begin_ok_button, show_empty_name_error, player_names, dice1, side, side2, number_of_dice
    
    images[3].resize(width, height)
    background(images[3])
    font1 = createFont("Courier", 30)    
    font2 = createFont("Courier", 75)
    font3 = createFont("Courier", 17)
    font4 = createFont("Courier", 35)
    
    x = 0
    YPositionText = 150
    YPositionRect = 180
    y = player_number = 1
    
    player_names = [player1_name, player2_name, player3_name, player4_name, player5_name, player6_name]

    fill(255, 255, 255)
    #handleiding
    textFont(font1)
    textAlign(CENTER)
    fill(230,230,230)
    rectMode(CENTER)
    rect(1370, 110, 220, 40, 6)
    fill(0,0,0)
    text("Handleiding", 1370, 122)
    rectMode(CORNER)
    
    while x < 3:
        fill(255,255,255)
        textAlign(LEFT)
        textFont(font1) 
        text("Player "+ str(y)+": " + player_names[x], 100, YPositionText)
        
        textFont(font2)
        textAlign(CENTER)    
        fill(230,230,230)
        rect(100, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        text("?", 140, YPositionRect+65)
        
        fill(230,230,230)
        rect(190, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        text("!", 230, YPositionRect+65)
        
        fill(230,230,230)
        rect(290, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        textFont(font3)
        text("Kaarten", 331, YPositionRect+44)
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233     
    
    YPositionText = 150
    YPositionRect = 180
    
    while x < number_of_players:
        fill(255,255,255)        
        textAlign(LEFT)
        textFont(font1)
        text("Player "+ str(y)+": " + player_names[x], 750, YPositionText)
        
        textFont(font2)
        textAlign(CENTER)        
        fill(230,230,230)
        rect(750, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        text("?", 790, YPositionRect+65)
        
        fill(230,230,230)
        rect(840, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        text("!", 880, YPositionRect+65)
        
        fill(230,230,230)
        rect(930, YPositionRect, 80, 80, 6)
        fill(0,0,0)
        textFont(font3)
        text("Kaarten", 971, YPositionRect+44)
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233
        
    if begin_ok_button == False:            
        fill(155, 155, 155) 
        rect(screenWidth/2 - 250, screenHeight/2 - 40, 500, 80, 6)
        fill(255,255,255)
        rect(screenWidth/2 + 160, screenHeight/2 - 20, 60, 40, 6)
        textAlign(CENTER)
        textFont(font4) 
        fill(0,0,0)
        text(player_names[player_starting] + " begint!", screenWidth/2 - 40, screenHeight/2 + 10)
        text("OK", screenWidth/2 + 190, screenHeight/2 + 10)

    textFont(font1)
    fill(255, 255, 255)
    rect(1280, 240, 40, 40, 6) #diceoption1  
    rect(1350, 240, 40, 40, 6) #diceoption2  
    rect(1260, 420, 150, 150, 6) #dice1
    if number_of_dices == 2:
        rect(1260, 670, 150, 150, 6) #dice2 
        
    rect(1274, 603, 120, 35, 6) #rolldice
    fill(255)
    textSize(18)
    text("Aantal dobbelstenen:", 1330, 220)
    textFont(font1)
    fill(0,0,0)
    text("1", 1300, 270)
    text("2", 1370, 270)
    text("Roll!", 1335, 630)
    
    if side == 1:
        d1 = dice1[0]
        image(d1, 1264, 420)
    if side == 2:
        d2 = dice1[1]
        image(d2, 1264, 420)
    if side == 3:
        d3 = dice1[2]
        image(d3, 1264, 420)
    if side == 4:
        d4 = dice1[3]
        image(d4, 1264, 420)
    if side == 5:
        d5 = dice1[4]
        image(d5, 1264, 420)
    if side == 6:
        d6 = dice1[5]
        image(d6, 1264, 420)
        
    #dice2
    if number_of_dices == 2:
        if side2 == 1:
            d1 = dice2[0]
            image(d1, 1264, 670)
        if side2 == 2:
            d2 = dice2[1]
            image(d2, 1264, 670)
        if side2 == 3:
            d3 = dice2[2]
            image(d3, 1264, 670)
        if side2 == 4:
            d4 = dice2[3]
            image(d4, 1264, 670)
        if side2 == 5:
            d5 = dice2[4]
            image(d5, 1264, 670)
        if side2 == 6:
            d6 = dice2[5]
            image(d6, 1264, 670)

def show_cards():
    global player_card_list_g, player_name_g
    
    images[3].resize(width, height)
    background(images[3])
    
    font1 = createFont("Courier", 30)
    font2 = createFont("Arial", 20)
    
    textAlign(CENTER)
    fill(255,255,255)

    textFont(font1)
    text("Kaarten van " + player_name_g + ":", screenWidth/2, 100) 
    
    textX = 100
    textY = 200
    buttonX = 1100
    buttonY = 220
    x = 0
    
    fill(250, 250, 250)
    rect(1300, 90, 140, 40, 6)
    fill(0,0,0)
    text("Terug", 1370, 122)
    
    for i in player_card_list_g:
        textAlign(LEFT)
        fill(255,255,255)

        textFont(font1)
        text("Kaart " + str(x + 1) + ":", textX, textY)
        
        textFont(font2)
        text(i, textX, textY + 30)
        
        fill(230,230,230)
        rect(buttonX, buttonY, 160, 40, 6)   
        fill(0,0,0)
        textAlign(CENTER)     
        textFont(font1)
        text("Gebruik!", buttonX + 80, buttonY + 31)
    
        
        
        
        buttonY += 180
        textY += 180
        x += 1
        
        text("Aantal Kaarten = " + "0 / 3", screenWidth/2, 850)
        if x == 1:
            cardLimitText() 
            text("Aantal Kaarten = " + str(x) + " / 3", screenWidth/2, 850)
        elif x == 2:
            cardLimitText() 
            text("Aantal Kaarten = " + str(x) + " / 3", screenWidth/2, 850)
        elif x == 3:
            cardLimitText() 
            text("Aantal Kaarten = " + str(x) + " / 3", screenWidth/2, 850)
        else:
            cardLimitText() 
            text("Aantal Kaarten = " + str(x) + " / 3", screenWidth/2, 850)


def show_manual():
    global images
    images[4].resize(width, height)
    background(images[4])
    
    font1 = createFont("Courier", 30)
    textFont(font1)
    textAlign(CENTER)
    fill(230,230,230)
    rect(1300, 90, 140, 40, 6)
    fill(0,0,0)
    text("Terug", 1370, 122)
        
    

def cardLimitText():
    fill(148, 120, 214)
    noStroke()
    rect(450, 800, 600, 200)
    fill(0) 
    stroke(0)
    textSize(30)
    
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
    global player1millis, player2millis, player3millis, player4millis, player5millis, player6millis
    global player1_cardtotal, player2_cardtotal, player3_cardtotal, player4_cardtotal, player5_cardtotal, player6_cardtotal
    global isMouseWithinSpace, value, bgs, bgsVolume, begin_ok_button, font, dice1, dice2
    global show_manual_display, show_empty_name_error, side, side2, number_of_dices

    
    if show_start_screen == True:
        if (mouseX >= 1390 and mouseX <= 1460) and (mouseY >= 850 and mouseY <= 868):
            exit_button_effect = True
            font = createFont("blackcherry.TTF", 100)
            if exit_button_effect == True:
                fill(50, 50, 50)
                textSize(38)
                text("Exit", 1425, 850)
                textFont(font)
                noStroke()
                if isMouseWithinSpace(1390, 850, 70, 18):
                    exit()                                   #Exit Button
            
        if (mouseX >= 625 and mouseX <= 900) and (mouseY >= 770 and mouseY <= 790):
            if how_many_players_screen == False:                                    #start game button effect
                fill(50, 50, 50)
                textSize(50)
                text("{                    }", width / 2, 770)
                text("Start Game", width / 2, 775)
                noStroke()
                start = True
                if start == True:
                    if isMouseWithinSpace(625, 770, 275, 20):
                        how_many_players_screen = True
                        show_start_screen = False                                    #Start Game Button
                        
        if isMouseWithinSpace(50, 850, 25, 20):
            if value == 0:
                value = 255
            else:
                value = 0
        
        if value == 0:
            if isMouseWithinSpace(40, 720, 35, 35):
                if bgsVolume == 0.0:
                    bgsVolume = 1.0
                print(bgsVolume)
                s.volume(bgsVolume)
            if isMouseWithinSpace(45, 780, 35, 35):
                if bgsVolume == 1.0:
                    bgsVolume = 0.0
                print(bgsVolume)
                s.volume(bgsVolume)
    
    elif how_many_players_screen == True:
        if (mouseX >= 650 and mouseX <= 710) and (mouseY >= 550 and mouseY <= 590):
            red_button = True
            if red_button == True:
                fill(100, 0, 0)
                rect(650, 550, 60, 40, 6)       
                fill(0,0,0)
                text("-", 680, 580)
                if (mouseX >= 650 and mouseX <= 710) and (mouseY >= 550 and mouseY <= 590):        #-1 player button
                    if number_of_players > 3:
                        number_of_players -= 1
        if (mouseX >= 790 and mouseX <= 850) and (mouseY >= 550 and mouseY <= 590):
            blue_button = True
            if blue_button == True:
                fill(0, 100, 0)
                rect(790, 550, 60, 40, 6)      
                fill(0,0,0)
                text("+", 820, 580)
                if (mouseX >= 790 and mouseX <= 850) and (mouseY >= 550 and mouseY <= 590):      #+1 player button
                    if number_of_players < 6:
                        number_of_players += 1
        if (mouseX >= 720 and mouseX <= 780) and (mouseY >= 600 and mouseY <= 640):
            if name_input_screen_display == False:
                fill(155, 155, 155)
                rect(720, 600, 60, 40, 6)    
                fill(0,0,0)
                text("OK", 750, 632)
                ok_button = True
                if ok_button == True:
                    if (mouseX >= 720 and mouseX <= 780) and (mouseY >= 600 and mouseY <= 640):
                        name_input_screen_display = True
                        how_many_players_screen = False
            
    
    elif name_input_screen_display == True:
        if show_empty_name_error == True:
            if (mouseX >= screenWidth/2 + 360 and mouseX <= screenWidth/2 + 420) and (mouseY >= screenHeight/2 - 20 and mouseY <= screenHeight/2 + 20):
                    show_empty_name_error = False
        #Checks if the user has clicked on a certain textbox to begin input
        else:
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
                if player1_name == '' or player2_name == '' or player3_name == '':
                    show_empty_name_error = True
                elif number_of_players > 3 and player4_name == '':
                    show_empty_name_error = True
                elif number_of_players > 4 and player5_name == '':
                    show_empty_name_error = True
                elif number_of_players > 5 and player6_name == '':
                    show_empty_name_error = True                                
                else:
                    show_empty_name_error = False
                    name_input_screen_display = False
                    main_screen_display = True                        
                    player1_box_selected = False
                    player2_box_selected = False
                    player3_box_selected = False
                    player4_box_selected = False
                    player5_box_selected = False
                    player6_box_selected = False
                    player_starting = int(random(0,number_of_players-1))
                        
            
    elif show_manual_display == True:
        if (mouseX >= 1300 and mouseX <= 1440) and (mouseY >= 90 and mouseY <= 130):
            font1 = createFont("Courier", 30)
            textFont(font1)
            textAlign(CENTER)
            fill(35, 35, 35)
            rect(1300, 90, 140, 40, 6)
            fill(0,0,0)
            text("Terug", 1370, 122)
            back_button = True
            if back_button == True:
                if (mouseX >= 1300 and mouseX <= 1440) and (mouseY >= 90 and mouseY <= 130):
                    main_screen_display = True
                    show_manual_display = False
    
    elif main_screen_display == True: 
        
        if begin_ok_button == False:
            if (mouseX >= screenWidth/2 + 160 and mouseX <= screenWidth/2 + 220) and (mouseY >= screenHeight/2 - 20 and mouseY <= screenHeight/2 + 20):
                begin_ok_button = True
        else:
            if (mouseX >= 100 and mouseX <= 180) and (mouseY >= 180 and mouseY <= 260):
                if len(fieldcard_list) > 0:
                    player1_fieldcards.append(generate_field_card())        
        #Handleiding Knop
            elif (mouseX >= 1250 and mouseX < 1470) and (mouseY >=90 and mouseY <=130):
                print("X : " + str(mouseX) + ", " + "Y: " + str(mouseY) + str(" IN SQUARE"))
                show_manual_display = True
                main_screen_display = False
        
            elif (mouseX >= 100 and mouseX <= 180) and (mouseY >= 180 and mouseY <= 260):
                if len(fieldcard_list) > 0:
                    player1_cardtotal += 1
                    if player1_cardtotal > 3:
                        player1millis = millis()
                        player1_cardtotal -= 1
                    else: 
                        player1_fieldcards.append(generate_field_card())                   
            if (mouseX >= 1250 and mouseX < 1470) and (mouseY >=90 and mouseY <=130):
                if show_manual_display == False:
                    font1 = createFont("Courier", 30)
                    textFont(font1)
                    textAlign(CENTER)
                    fill(35, 35, 35)
                    rectMode(CENTER)
                    rect(1370, 110, 220, 40, 6)
                    fill(0,0,0)
                    text("Handleiding", 1370, 122)
                    rectMode(CORNER)
                    manual_button = True
                    if manual_button == True:
                        if (mouseX >= 1250 and mouseX < 1470) and (mouseY >=90 and mouseY <=130):
                            # print("X : " + str(mouseX) + ", " + "Y: " + str(mouseY) + str(" IN SQUARE"))
                            show_manual_display = True
                            main_screen_display = False
            
            if (mouseX >= 1280 and mouseX <= 1320) and (mouseY >= 240 and mouseY <= 280):
                fill(150, 150, 150)
                rect(1280, 240, 40, 40, 6)
                fill(0,0,0)
                text("1", 1300, 270)
                if (mouseX >= 1280 and mouseX <= 1320) and (mouseY >= 240 and mouseY <= 280):
                    number_of_dices = 1
            
            if (mouseX >= 1350 and mouseX <= 1390) and (mouseY >= 240 and mouseY <= 280):
                fill(150, 150, 150)
                rect(1350, 240, 40, 40, 6)
                fill(0,0,0)
                text("2", 1370, 270)
                if (mouseX >= 1350 and mouseX <= 1390) and (mouseY >= 240 and mouseY <= 280):
                    number_of_dices = 2
                            
            if (mouseX >= 1274 and mouseX <= 1394) and (mouseY >= 603 and mouseY <= 638):
                fill(150, 150, 150)
                rect(1274, 603, 120, 35, 6) #rolldice
                fill(0,0,0)
                text("Roll!", 1335, 630)
                if (mouseX >= 1274 and mouseX <= 1394) and (mouseY >= 603 and mouseY <= 638):
                    font1 = createFont("Courier", 30)                
                    side = int(random(1,7))
                    side2 = int(random(1,7))
                    
                    #dice1
                
                
            elif (mouseX >= 100 and mouseX <= 180) and (mouseY >= 413 and mouseY <= 493):
                if len(fieldcard_list) > 0:
                    player2_cardtotal += 1
                    if player2_cardtotal > 3:
                        player2millis = millis()
                        player2_cardtotal -= 1
                    else:
                        player2_fieldcards.append(generate_field_card())
                    
            elif (mouseX >= 100 and mouseX <= 180) and (mouseY >= 646 and mouseY <= 726):
                if len(fieldcard_list) > 0:
                    player3_cardtotal += 1
                    if player3_cardtotal > 3:
                        player3millis = millis()
                        player3_cardtotal -= 1
                    else:
                        player3_fieldcards.append(generate_field_card())
                
            elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
                if len(fieldcard_list) > 0:
                    player4_cardtotal += 1
                    if player4_cardtotal > 3:
                        player4millis = millis()
                        player4_cardtotal -= 1
                    else:
                        player4_fieldcards.append(generate_field_card())
            
            elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
                if len(fieldcard_list) > 0:
                    player5_cardtotal += 1
                    if player5_cardtotal > 3:
                        player5millis = millis()
                        player5_cardtotal -= 1
                    else:
                        player5_fieldcards.append(generate_field_card())
            
            elif ((mouseX >= 750 and mouseX <= 830) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
                if len(fieldcard_list) > 0:
                    player6_cardtotal += 1
                    if player6_cardtotal > 3:
                        player6millis = millis()
                        player6_cardtotal -= 1
                    else:
                        player6_fieldcards.append(generate_field_card())
                    
            elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 180 and mouseY <= 260):
                if len(trapcard_list) > 0:
                    player1_cardtotal += 1
                    if player1_cardtotal > 3:
                        player1millis = millis()
                        player1_cardtotal -= 1
                    else:
                        player1_trapcards.append(generate_trap_card())
                    
            elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 413 and mouseY <= 493):
                if len(trapcard_list) > 0:
                    player2_cardtotal += 1
                    if player2_cardtotal > 3:
                        player2millis = millis()
                        player2_cardtotal -= 1
                    else:
                        player2_trapcards.append(generate_trap_card())
                    
            elif (mouseX >= 190 and mouseX <= 270) and (mouseY >= 646 and mouseY <= 726):
                if len(trapcard_list) > 0:
                    player3_cardtotal += 1
                    if player3_cardtotal > 3:
                        player3millis = millis()
                        player3_cardtotal -= 1
                    else:
                        player3_trapcards.append(generate_trap_card())
                    
            elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
                if len(trapcard_list) > 0:
                    player4_cardtotal += 1
                    if player4_cardtotal > 3:
                        player4millis = millis()
                        player4_cardtotal -= 1
                    else:
                        player4_trapcards.append(generate_trap_card())
            
            elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
                if len(trapcard_list) > 0:
                    player5_cardtotal += 1
                    if player5_cardtotal > 3:
                        player5millis = millis()
                        player5_cardtotal -= 1
                    else:
                        player5_trapcards.append(generate_trap_card())
            
            elif ((mouseX >= 840 and mouseX <= 920) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
                if len(trapcard_list) > 0:
                    player6_cardtotal += 1
                    if player6_cardtotal > 3:
                        player6millis = millis()
                        player6_cardtotal -= 1
                    else:
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
            
            if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 180 and mouseY <= 260):
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten1_button = True
                if kaarten1_button == True:
                    if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 180 and mouseY <= 260):  
                        player_card_list_g = player1_fieldcards + player1_trapcards 
                        player_name_g = player1_name
                        
                        show_cards_display = True
                        main_screen_display = False
            
            
            if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 413 and mouseY <= 493):
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten2_button = True
                if kaarten2_button == True:
                    if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 413 and mouseY <= 493):  
                        player_card_list_g = player2_fieldcards + player2_trapcards 
                        player_name_g = player2_name
                            
                        show_cards_display = True
                        main_screen_display = False
                
            if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 646 and mouseY <= 726):
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten2_button = True
                if kaarten2_button == True:
                    if (mouseX >= 280 and mouseX <= 370) and (mouseY >= 646 and mouseY <= 726):
                        player_card_list_g = player3_fieldcards + player3_trapcards 
                        player_name_g = player3_name
                            
                        show_cards_display = True
                        main_screen_display = False
            
            if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten3_button = True
                if kaarten3_button == True:
                    if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 180 and mouseY <= 260)) and number_of_players > 3:
                        player_card_list_g = player4_fieldcards + player4_trapcards 
                        player_name_g = player4_name
                            
                        show_cards_display = True
                        main_screen_display = False
            
            if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten4_button = True
                if kaarten4_button == True:
                    if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 413 and mouseY <= 493)) and number_of_players > 4:
                        player_card_list_g = player5_fieldcards + player5_trapcards 
                        player_name_g = player5_name
                        
                        show_cards_display = True
                        main_screen_display = False
                        
            if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
                fill(35, 35, 35)
                rect(290, 200, 80, 80, 6)
                fill(0,0,0)
                font3 = createFont("Courier", 17)
                textFont(font3)
                text("Kaarten", 331, 200+44)
                kaarten5_button = True
                if kaarten5_button == True:
                    if ((mouseX >= 940 and mouseX <= 1020) and (mouseY >= 646 and mouseY <= 726)) and number_of_players > 5:
                        player_card_list_g = player6_fieldcards + player6_trapcards 
                        player_name_g = player6_name
                        
                        show_cards_display = True
                        main_screen_display = False
    
    elif show_cards_display == True:
        if (mouseX >= 1300 and mouseX <= 1440) and (mouseY >= 90 and mouseY <= 130):
            fill(100, 100, 100)
            rect(1300, 90, 140, 40, 6)
            fill(0,0,0)
            text("Terug", 1370, 122)
            if (mouseX >= 1300 and mouseX <= 1440) and (mouseY >= 90 and mouseY <= 130):
                main_screen_display = True
                show_cards_display = False
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 220 and mouseY <= 260) and len(player_card_list_g) > 0:
            if player_card_list_g[0] in player1_fieldcards and player_name_g == player1_name:                
                player1_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player1_cardtotal -= 1
            elif player_card_list_g[0] in player1_trapcards and player_name_g == player1_name:                
                player1_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player1_cardtotal -= 1            
            elif player_card_list_g[0] in player2_fieldcards and player_name_g == player2_name:                
                player2_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player2_cardtotal -= 1
            elif player_card_list_g[0] in player2_trapcards and player_name_g == player2_name:                
                player2_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player2_cardtotal -= 1            
            elif player_card_list_g[0] in player3_fieldcards and player_name_g == player3_name:                
                player3_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player3_cardtotal -= 1
            elif player_card_list_g[0] in player3_trapcards and player_name_g == player3_name:                
                player3_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player3_cardtotal -= 1            
            elif player_card_list_g[0] in player4_fieldcards and player_name_g == player4_name:                
                player4_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player4_cardtotal -= 1
            elif player_card_list_g[0] in player4_trapcards and player_name_g == player4_name:                
                player4_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player4_cardtotal -= 1            
            elif player_card_list_g[0] in player5_fieldcards and player_name_g == player5_name:                
                player5_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player5_cardtotal -= 1
            elif player_card_list_g[0] in player5_trapcards and player_name_g == player5_name:                
                player5_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player5_cardtotal -= 1            
            elif player_card_list_g[0] in player6_fieldcards and player_name_g == player6_name:                
                player6_fieldcards.remove(player_card_list_g[0])
                fieldcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            elif player_card_list_g[0] in player6_trapcards and player_name_g == player6_name:                
                player6_trapcards.remove(player_card_list_g[0])
                trapcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 400 and mouseY <= 440) and len(player_card_list_g) > 1:
            if player_card_list_g[1] in player1_fieldcards and player_name_g == player1_name:                
                player1_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player1_cardtotal -= 1
            elif player_card_list_g[1] in player1_trapcards and player_name_g == player1_name:                
                player1_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))     
                player1_cardtotal -= 1       
            elif player_card_list_g[1] in player2_fieldcards and player_name_g == player2_name:                
                player2_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player2_cardtotal -= 1
            elif player_card_list_g[1] in player2_trapcards and player_name_g == player2_name:                
                player2_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))      
                player2_cardtotal -= 1      
            elif player_card_list_g[1] in player3_fieldcards and player_name_g == player3_name:                
                player3_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player3_cardtotal -= 1
            elif player_card_list_g[1] in player3_trapcards and player_name_g == player3_name:                
                player3_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))       
                player3_cardtotal -= 1     
            elif player_card_list_g[1] in player4_fieldcards and player_name_g == player4_name:                
                player4_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player4_cardtotal -= 1
            elif player_card_list_g[1] in player4_trapcards and player_name_g == player4_name:                
                player4_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))       
                player4_cardtotal -= 1     
            elif player_card_list_g[1] in player5_fieldcards and player_name_g == player5_name:                
                player5_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player5_cardtotal -= 1
            elif player_card_list_g[1] in player5_trapcards and player_name_g == player5_name:                
                player5_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))    
                player5_cardtotal -= 1        
            elif player_card_list_g[1] in player6_fieldcards and player_name_g == player6_name:                
                player6_fieldcards.remove(player_card_list_g[1])
                fieldcard_list.append(player_card_list_g.pop(1))
                player6_cardtotal -= 1
            elif player_card_list_g[1] in player6_trapcards and player_name_g == player6_name:                
                player6_trapcards.remove(player_card_list_g[1])
                trapcard_list.append(player_card_list_g.pop(1))
                player6_cardtotal -= 1
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 580 and mouseY <= 620) and len(player_card_list_g) > 2:
            if player_card_list_g[2] in player1_fieldcards and player_name_g == player1_name:                
                player1_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player1_cardtotal -= 1
            elif player_card_list_g[2] in player1_trapcards and player_name_g == player1_name:                
                player1_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))     
                player1_cardtotal -= 1       
            elif player_card_list_g[2] in player2_fieldcards and player_name_g == player2_name:                
                player2_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player2_cardtotal -= 1
            elif player_card_list_g[2] in player2_trapcards and player_name_g == player2_name:                
                player2_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))      
                player2_cardtotal -= 1      
            elif player_card_list_g[2] in player3_fieldcards and player_name_g == player3_name:                
                player3_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player3_cardtotal -= 1
            elif player_card_list_g[2] in player3_trapcards and player_name_g == player3_name:                
                player3_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))        
                player3_cardtotal -= 1    
            elif player_card_list_g[2] in player4_fieldcards and player_name_g == player4_name:                
                player4_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player4_cardtotal -= 1
            elif player_card_list_g[2] in player4_trapcards and player_name_g == player4_name:                
                player4_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))          
                player4_cardtotal -= 1  
            elif player_card_list_g[2] in player5_fieldcards and player_name_g == player5_name:                
                player5_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player5_cardtotal -= 1
            elif player_card_list_g[2] in player5_trapcards and player_name_g == player5_name:                
                player5_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))       
                player5_cardtotal -= 1     
            elif player_card_list_g[2] in player6_fieldcards and player_name_g == player6_name:                
                player6_fieldcards.remove(player_card_list_g[2])
                fieldcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            elif player_card_list_g[2] in player6_trapcards and player_name_g == player6_name:                
                player6_trapcards.remove(player_card_list_g[2])
                trapcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            
        elif(mouseX >= 1100 and mouseX <= 1260) and (mouseY >= 760 and mouseY <= 800) and len(player_card_list_g) > 3:
            if player_card_list_g[3] in player1_fieldcards and player_name_g == player1_name:                
                player1_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player1_cardtotal -= 1
            elif player_card_list_g[3] in player1_trapcards and player_name_g == player1_name:                
                player1_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))   
                player1_cardtotal -= 1         
            elif player_card_list_g[3] in player2_fieldcards and player_name_g == player2_name:                
                player2_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player2_cardtotal -= 1
            elif player_card_list_g[3] in player2_trapcards and player_name_g == player2_name:                
                player2_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))    
                player2_cardtotal -= 1        
            elif player_card_list_g[3] in player3_fieldcards and player_name_g == player3_name:                
                player3_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player3_cardtotal -= 1
            elif player_card_list_g[3] in player3_trapcards and player_name_g == player3_name:                
                player3_trapcards.remove(player_card_list_g[3])
                player3_cardtotal -= 1
                trapcard_list.append(player_card_list_g.pop(0))            
            elif player_card_list_g[3] in player4_fieldcards and player_name_g == player4_name:                
                player4_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player4_cardtotal -= 1
            elif player_card_list_g[3] in player4_trapcards and player_name_g == player4_name:                
                player4_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))       
                player4_cardtotal -= 1     
            elif player_card_list_g[3] in player5_fieldcards and player_name_g == player5_name:                
                player5_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player5_cardtotal -= 1
            elif player_card_list_g[3] in player5_trapcards and player_name_g == player5_name:                
                player5_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))      
                player5_cardtotal -= 1      
            elif player_card_list_g[3] in player6_fieldcards and player_name_g == player6_name:                
                player6_fieldcards.remove(player_card_list_g[3])
                fieldcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            elif player_card_list_g[3] in player6_trapcards and player_name_g == player6_name:                
                player6_trapcards.remove(player_card_list_g[3])
                trapcard_list.append(player_card_list_g.pop(0))
                player6_cardtotal -= 1
            

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
    fieldCard7 = "Het is monsoon seizoen en door het regen zijn alle wegen versperd door drijfzand.\nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard8 = "Door gebruik te maken van een magische spreuk vallen alle tegenstanders in slaap.\nEen bijwerking van de spreuk zorgt ervoor dat wanneer de tegenstanders wakker worden, \nde gebruiker ook in slaap valt. \nDe tegenstanders slaan een beurt over, volgende beurt slaat de gebruiker een beurt over."
    fieldCard9 = "Je bent met je goede been uit bed gestapt. \nJe hebt het gevoel dat je meer kunt bewegen dan normaal. \nVoor deze beurt gebruik je een extra dobbelsteen om te bewegen. "
    fieldCard10 = "Door een magische spreuk ruil je plaatsen met een van je tegenstanders. \nJe tegenstander landt precies waar jij was, maar jij valt van 10 meter boven de grond. \nJe landt op een pijnlijke manier en moet uitrusten om verder te gaan. \nRuil plaats met gekozen tegenstander en sla een beurt over. "
    fieldCard11 = "Door een vloek hebben alle spelers een rot humeur. \nNiemand heeft zin om verder te gaan. \nZe doen het minimale van wat hun verwacht wordt. \nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard12 = "Door een magische spreuk kun je door een spiegel de kaarten van je tegenstander bekijken. \nHet nadeel is dat je tegenstander ook jouw kaarten kan zien, omdat de spiegel van beide kanten werkt. \nGebruiker en tegenstander tonen hun kaarten aan elkaar."
    fieldCard13 = "Het is monsoon seizoen en door het regen zijn alle wegen versperd door drijfzand.\nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard14 = "Door gebruik te maken van een magische spreuk vallen alle tegenstanders in slaap.\nEen bijwerking van de spreuk zorgt ervoor dat wanneer de tegenstanders wakker worden, \nde gebruiker ook in slaap valt. \nDe tegenstanders slaan een beurt over, volgende beurt slaat de gebruiker een beurt over."
    fieldCard15 = "Je bent met je goede been uit bed gestapt. \nJe hebt het gevoel dat je meer kunt bewegen dan normaal. \nVoor deze beurt gebruik je een extra dobbelsteen om te bewegen. "
    fieldCard16 = "Door een magische spreuk ruil je plaatsen met een van je tegenstanders. \nJe tegenstander landt precies waar jij was, maar jij valt van 10 meter boven de grond. \nJe landt op een pijnlijke manier en moet uitrusten om verder te gaan. \nRuil plaats met gekozen tegenstander en sla een beurt over. "
    fieldCard17 = "Door een vloek hebben alle spelers een rot humeur. \nNiemand heeft zin om verder te gaan. \nZe doen het minimale van wat hun verwacht wordt. \nAlle spelers gebruiken een dobbelsteen minder om te bewegen."
    fieldCard18 = "Door een magische spreuk kun je door een spiegel de kaarten van je tegenstander bekijken. \nHet nadeel is dat je tegenstander ook jouw kaarten kan zien, omdat de spiegel van beide kanten werkt. \nGebruiker en tegenstander tonen hun kaarten aan elkaar."
    
    duelCard1 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. \nDe aanvaller mag maar een dobbelsteen gebruiken."
    duelCard2 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. \nHierdoor zul je niet makkelijk verliezen. \nDe verdediger mag twee dobbelstenen gebruiken."
    duelCard3 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. \nDe aanvaller en de verdediger gebruiken een extra dobbelsteen."
    duelCard4 = "Tijdens het gevecht gooi je zand in het gezicht van je tegenstander. \nJe tegenstander kan je moeilijk zien, waardoor zijn kans van winnen minder wordt. \nVerminder het uiteindelijke getal van je tegenstander met 1."
    duelCard5 = "Tijdens het gevecht maakt je tegenstander een misstap en zit tijdelijk vast in drijfzand. \nJe tegenstander kan zich moeilijk bewegen, waardoor je kans van winnen groter wordt. \nVerhoog het uiteindelijke getal van de gebruiker met 1."
    duelCard6 = "Je vindt dat het gevecht niet was gegaan zoals je wilde. \nJe vraagt je tegenstander voor nog een gevecht. \nJe blijft zeuren totdat je tegenstander met tegenzin accepteert, \nmet als conditie dat 2 voorwerpen worden terug gelegd. \nForceer een rematch met 2 voorwerpen als prijs."
    duelCard7 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. \nDe aanvaller mag maar een dobbelsteen gebruiken."
    duelCard8 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. \nHierdoor zul je niet makkelijk verliezen. \nDe verdediger mag twee dobbelstenen gebruiken."
    duelCard9 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. \nDe aanvaller en de verdediger gebruiken een extra dobbelsteen."
    duelCard10 = "Tijdens het gevecht gooi je zand in het gezicht van je tegenstander. \nJe tegenstander kan je moeilijk zien, waardoor zijn kans van winnen minder wordt. \nVerminder het uiteindelijke getal van je tegenstander met 1."
    duelCard11 = "Tijdens het gevecht maakt je tegenstander een misstap en zit tijdelijk vast in drijfzand. \nJe tegenstander kan zich moeilijk bewegen, waardoor je kans van winnen groter wordt. \nVerhoog het uiteindelijke getal van de gebruiker met 1."
    duelCard12 = "Je vindt dat het gevecht niet was gegaan zoals je wilde. \nJe vraagt je tegenstander voor nog een gevecht. \nJe blijft zeuren totdat je tegenstander met tegenzin accepteert, \nmet als conditie dat 2 voorwerpen worden terug gelegd. \nForceer een rematch met 2 voorwerpen als prijs."
    duelCard13 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. \nDe aanvaller mag maar een dobbelsteen gebruiken."
    duelCard14 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. \nHierdoor zul je niet makkelijk verliezen. \nDe verdediger mag twee dobbelstenen gebruiken."
    duelCard15 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. \nJe wenst voor kracht om je tegenstander te verslaan. \nDe genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. \nDe aanvaller en de verdediger gebruiken een extra dobbelsteen."
    duelCard16 = "Tijdens het gevecht gooi je zand in het gezicht van je tegenstander. \nJe tegenstander kan je moeilijk zien, waardoor zijn kans van winnen minder wordt. \nVerminder het uiteindelijke getal van je tegenstander met 1."
    duelCard17 = "Tijdens het gevecht maakt je tegenstander een misstap en zit tijdelijk vast in drijfzand. \nJe tegenstander kan zich moeilijk bewegen, waardoor je kans van winnen groter wordt. \nVerhoog het uiteindelijke getal van de gebruiker met 1."
    duelCard18 = "Je vindt dat het gevecht niet was gegaan zoals je wilde. \nJe vraagt je tegenstander voor nog een gevecht. \nJe blijft zeuren totdat je tegenstander met tegenzin accepteert, \nmet als conditie dat 2 voorwerpen worden terug gelegd. \nForceer een rematch met 2 voorwerpen als prijs."
    
    fieldcard_list = [fieldCard1, fieldCard2, fieldCard3, fieldCard4, fieldCard5, fieldCard6,
                      fieldCard7, fieldCard8, fieldCard9, fieldCard10, fieldCard11, fieldCard12,
                      fieldCard13, fieldCard14, fieldCard15, fieldCard16, fieldCard17, fieldCard18,
                      duelCard1, duelCard2, duelCard3, duelCard4, duelCard5, duelCard6, 
                      duelCard7, duelCard8, duelCard9, duelCard10, duelCard11, duelCard12,
                      duelCard13, duelCard14, duelCard15, duelCard16, duelCard17, duelCard18]
    
    trapCard1 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. \nSla een beurt over."
    trapCard2 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard3 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, \nmaar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. \nNa een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. \nEen hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard4 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. \nJe komt erachter dat een van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
    trapCard5 = "Door een magische spreuk ruilen alle spelers plaatsen met elkaar. \nJe tegenstanders landen veilig op hun plaats, maar jij valt van 20 meter boven de grond. \nJe landt op je hoofd en bent buiten bewustzijn. Je wordt pas na een hele dag wakker. \nAlle spelers ruilen plaatsen met elkaar en sla twee beurten over."
    trapCard6 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. \nSla een beurt over."
    trapCard7 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard8 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, \nmaar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. \nNa een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. \nEen hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard9 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. \nJe komt erachter dat een van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
    trapCard10 = "Door een magische spreuk ruilen alle spelers plaatsen met elkaar. \nJe tegenstanders landen veilig op hun plaats, maar jij valt van 20 meter boven de grond. \nJe landt op je hoofd en bent buiten bewustzijn. Je wordt pas na een hele dag wakker. \nAlle spelers ruilen plaatsen met elkaar en sla twee beurten over."
    trapCard11 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. \nSla een beurt over."
    trapCard12 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard13 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, \nmaar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. \nNa een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. \nEen hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard14 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. \nJe komt erachter dat een van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
    trapCard15 = "Door een magische spreuk ruilen alle spelers plaatsen met elkaar. \nJe tegenstanders landen veilig op hun plaats, maar jij valt van 20 meter boven de grond. \nJe landt op je hoofd en bent buiten bewustzijn. Je wordt pas na een hele dag wakker. \nAlle spelers ruilen plaatsen met elkaar en sla twee beurten over."
    
    trapcard_list = [trapCard1, trapCard2, trapCard3, trapCard4, trapCard5,
                     trapCard6, trapCard7, trapCard8, trapCard9, trapCard10,
                     trapCard11, trapCard12, trapCard13, trapCard14, trapCard15]

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


def start_screen():
    global bgs, isMouseWithinSpace, gifWidth, gifHeight, images

    images[0].resize(width, height)
    background(images[0])    
    
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
    
    #volume_buttons
    if value == 0:
        textSize(70)
        fill(255)
        text("^", 60, 840)
        textSize(50)
        
        fill(35)
        rect(32, 700, 55, 125, 7)
        noStroke()
        
        fill(255)
        img = images[5]
        image(img, 40, 720)   #sound_button
        img2 = images[6]
        image(img2, 45, 780)  #mute_button

  
    def isMouseWithinSpace(x, y, breedte, hoogte):
        if x < mouseX < x + breedte and y < mouseY < y + hoogte:
            return True
        else:
            return False

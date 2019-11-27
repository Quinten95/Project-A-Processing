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
    
#Creates the main playing screen in which players can choose to draw a random card
#the cards per player are shown
#and players can use a card in their posession
def main_screen():
    font1 = createFont("Arial", 30)    
    font2 = createFont("Arial", 75)
    
    x = 0
    YPositionText = 150
    YPositionRect = 180
    y = player_number = 1
    
    player_names = [player1_name, player2_name, player3_name, player4_name, player5_name, player6_name]
    
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
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233
    
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
        
        x += 1
        y += 1
        YPositionText += 233
        YPositionRect += 233

        
    
    
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
   
    
     
def generateFieldCard():
    fill(255, 255, 255)
    drawADuelCard = rect(1100, 500, 50, 50)
    drawAFieldCard = rect(1200, 500, 50, 50)
    fill(0);
    textAlign(CENTER);
    textSize(28)
    text("!", 1125, 535)
    text("?", 1225, 535)
    
    
    fieldCard1 = "Het is monsoon seizoen en door het regen zijn alle wegen versperd door drijfzand. Alle spelers gebruiken één minder dobbelsteen om te bewegen. "
    fieldCard2 = "Door gebruik te maken van een magische spreuk vallen alle tegenstanders in slaap. Een bijwerking van de spreuk zorgt ervoor dat na de tegenstanders wakker worden, de gebruiker ook in slaap valt. De tegenstanders slaan een beurt over, volgende beurt slaat de gebruiker een beurt over."
    fieldCard3 = "Je bent met je goede been uit bed gestapt. Je hebt het gevoel dat je meer kunt bewegen dan normaal. Voor deze beurt gebruik je een extra dobbelsteen om te bewegen. "
    fieldCard4 = "Door een magische spreuk ruil je plaatsen met één van je tegenstanders. Je tegenstander landt precies waar jij was, maar jij valt van 10 meter boven de grond. Je landt op een pijnlijke manier en moet uitrusten om verder te gaan. Ruil plaats met gekozen tegenstander en sla een beurt over. "
    fieldCard5 = "Door een vloek hebben alle spelers een rot humeur. Niemand heeft zin om verder te gaan. Ze doen het minimale van wat hun verwacht wordt. Alle spelers gebruiken één minder dobbelsteen om te bewegen."
    fieldCard6 = "Door een magische spreuk kun je door een spiegel de kaarten van je tegenstander bekijken. Het nadeel is dat je tegenstander ook jouw kaarten kan zien, omdat de spiegel van beide kanten werkt. Gebruiker en tegenstander tonen hun kaarten aan elkaar."
    trapCard7 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. Sla een beurt over."
    trapCard8 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard9 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, maar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. Na een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. Een hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard10 = "Door gebruik te maken van een magisch portaal probeer je een voorwerp te stelen van een tegenstander. Het lukt, maar tijdens de transactie valt één van jouw items in het portaal. Gebruiker ruilt een random voorwerp met een tegenstander."
    trapCard11 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. Je komt erachter dat één van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
    trapCard12 = "Door een magische spreuk ruilen alle spelers plaatsen met elkaar. Je tegenstanders landen veilig op hun plaats, maar jij valt van 20 meter boven de grond. Je landt op je hoofd en bent buiten bewustzijn. Je wordt pas na een hele dag wakker. Alle spelers ruilen plaatsen met elkaar en sla twee beurten over."

    chosenFieldNumber = int(random(1, 12))
    selectedFieldCard = 0
    if chosenFieldNumber == 1:
        selectedFieldCard = fieldCard1
    elif chosenFieldNumber == 2:
        selectedFieldCard = fieldCard2
    elif chosenFieldNumber == 3:
        selectedFieldCard = fieldCard3
    elif chosenFieldNumber == 4:
        selectedFieldCard = fieldCard4
    elif chosenFieldNumber == 5:
        selectedFieldCard = fieldCard5
    elif chosenFieldNumber == 6:
        selectedFieldCard = fieldCard6
    elif chosenFieldNumber == 7:
        selectedFieldCard = trapCard7
    elif chosenFieldNumber == 8:
        selectedFieldCard = trapCard8
    elif chosenFieldNumber == 9:
        selectedFieldCard = trapCard9
    elif chosenFieldNumber == 10:
        selectedFieldCard = trapCard10
    elif chosenFieldNumber == 11:
        selectedFieldCard = trapCard11
    elif chosenFieldNumber == 12:
        selectedFieldCard = trapCard12
        
    print(selectedFieldCard)
    return selectedFieldCard
    
    
def generateDuelCard():
    duelCard13 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. Je wenst voor kracht om je tegenstander te verslaan. De genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. De aanvaller mag maar één dobbelsteen gebruiken."
    duelCard14 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. Hierdoor zul je niet makkelijk verliezen. De verdediger mag twee dobbelstenen gebruiken."
    duelCard15 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. Je wenst voor kracht om je tegenstander te verslaan. De genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. De aanvaller en de verdediger gebruiken één extra dobbelsteen."
    duelCard16 = "Tijdens het gevecht gooi je zand in het gezicht van je tegenstander. Je tegenstander kan je moeilijk zien, waardoor zijn kans van winnen minder wordt. Verminder het uiteindelijke getal van je tegenstander met 1."
    duelCard17 = "Tijdens het gevecht maakt je tegenstander een misstap en zit tijdelijk vast in drijfzand. Je tegenstander kan zich moeilijk bewegen, waardoor je kans van winnen groter wordt. Verhoog het uiteindelijke getal van de gebruiker met 1."
    duelCard18 = "Je vindt dat het gevecht niet was gegaan zoals je wilde. Je vraagt je tegenstander voor nog een gevecht. Je blijft zeuren totdat je tegenstander met tegenzin accepteert, met als conditie dat 2 voorwerpen naar de winnaar gaan. Forceer een rematch voor 2 voorwerpen als prijs."
        
    chosenDuelNumber = int(random(13, 18))
    if chosenDuelNumber == 13:
        selectedDuelCard = duelCard13
    elif chosenDuelNumber == 14:
        selectedDuelCard = duelCard14
    elif chosenDuelNumber == 15:
        selectedDuelCard = duelCard15
    elif chosenDuelNumber == 16:
        selectedDuelCard = duelCard16
    elif chosenDuelNumber == 17:
        selectedDuelCard = duelCard17
    elif chosenDuelNumber == 18:    
        selectedDuelCard = duelCard18
        
    print(selectedDuelCard)
    return selectedDuelCard

    

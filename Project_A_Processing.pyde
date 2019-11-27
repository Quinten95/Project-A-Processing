
def setup():
    size(1500, 900)
    background("#F9A602")
    arial = createFont("Arial", 20)

      
def draw():
    fill(255, 255, 255)
    drawADuelCard = rect(1100, 500, 50, 50)
    drawAFieldCard = rect(1200, 500, 50, 50)
    fill(0);
    textAlign(CENTER);
    textSize(28)
    text("!", 1125, 535)
    text("?", 1225, 535)
    
    
     
def generateFieldCard():
    fieldCard1 = "Het is monsoon seizoen en door het regen zijn alle wegen versperd door drijfzand. Alle spelers gebruiken een minder dobbelsteen om te bewegen. "
    fieldCard2 = "Door gebruik te maken van een magische spreuk vallen alle tegenstanders in slaap. Een bijwerking van de spreuk zorgt ervoor dat na de tegenstanders wakker worden, de gebruiker ook in slaap valt. De tegenstanders slaan een beurt over, volgende beurt slaat de gebruiker een beurt over."
    fieldCard3 = "Je bent met je goede been uit bed gestapt. Je hebt het gevoel dat je meer kunt bewegen dan normaal. Voor deze beurt gebruik je een extra dobbelsteen om te bewegen. "
    fieldCard4 = "Door een magische spreuk ruil je plaatsen met een van je tegenstanders. Je tegenstander landt precies waar jij was, maar jij valt van 10 meter boven de grond. Je landt op een pijnlijke manier en moet uitrusten om verder te gaan. Ruil plaats met gekozen tegenstander en sla een beurt over. "
    fieldCard5 = "Door een vloek hebben alle spelers een rot humeur. Niemand heeft zin om verder te gaan. Ze doen het minimale van wat hun verwacht wordt. Alle spelers gebruiken een minder dobbelsteen om te bewegen."
    fieldCard6 = "Door een magische spreuk kun je door een spiegel de kaarten van je tegenstander bekijken. Het nadeel is dat je tegenstander ook jouw kaarten kan zien, omdat de spiegel van beide kanten werkt. Gebruiker en tegenstander tonen hun kaarten aan elkaar."
    trapCard7 = "Je valt in een trap en zit vast in een grot. Het duurt een aantal uren tot je uit de grot kunt klimmen. Sla een beurt over."
    trapCard8 = "Je gaat door je enkel en moet uitrusten tot je weer verder kan. Sla een beurt over."
    trapCard9 = "Je valt in een trap en zit vast in een grot. Je probeert uit de grot te klimmen, maar iets of iemand heeft de grot glad gemaakt, waardoor je geen houvast kan hebben. Na een halve dag valt een stevig stuk touw naar beneden. Je beklimt het touw en ontsnapt de grot. Een hele dag is voorbijgegaan. Sla twee beurten over."
    trapCard10 = "Door gebruik te maken van een magisch portaal probeer je een voorwerp te stelen van een tegenstander. Het lukt, maar tijdens de transactie valt een van jouw items in het portaal. Gebruiker ruilt een random voorwerp met een tegenstander."
    trapCard11 = "Door de sterke wind van een zandstorm kun je nauwelijks iets zien. Na een tijdje is de zandstorm voorbij. Je komt erachter dat een van je voorwerpen door de zandstorm weggewaaid is. Verlies een random voorwerp."
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
    duelCard13 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. Je wenst voor kracht om je tegenstander te verslaan. De genie geeft je geen kracht, maar maakt wel je tegenstander zwakker. De aanvaller mag maar een dobbelsteen gebruiken."
    duelCard14 = "Voor het gevecht vind je een kist vol met wapens en een uitrusting. Hierdoor zul je niet makkelijk verliezen. De verdediger mag twee dobbelstenen gebruiken."
    duelCard15 = "Je vindt voor het gevecht een magische lamp. De genie in de lamp geeft je een wens. Je wenst voor kracht om je tegenstander te verslaan. De genie geeft je wel kracht, maar zorgt er ook voor dat je tegenstander sterker wordt. De aanvaller en de verdediger gebruiken een extra dobbelsteen."
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
    
def mousePressed():
    global mouseX, mouseY
    if (mouseY > 499 and mouseY < 551) and (mouseX > 1199 and mouseX < 1251):
      generateFieldCard()
    if (mouseY > 499 and mouseY < 551) and (mouseX > 1099 and mouseX < 1151):
      generateDuelCard()
      
    

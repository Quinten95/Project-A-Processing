
def setup():
    size(1500, 900)
    background("#F9A602")
    arial = createFont("Arial", 14)

      
def draw():
    fill(255, 255, 255)
    drawACard = rect(1200, 500, 100, 50)
    fill(0);
    textAlign(CENTER);
    text("testing", 750, 450)
    text("Draw A Card", 1250, 525)
    
def cardGenerator():
    
    pass
    
def mousePressed():
    global mouseX, mouseY
    if (mouseY > 499 and mouseY < 571) and (mouseX > 1199 and mouseX < 1301):
      print("AAAAAA")
    pass

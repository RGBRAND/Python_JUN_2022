import pgzrun

HEIGHT = 500
WIDTH = 700

box1_v1 = 2
box2_v2 = 2
box3_v3 = 2

box1 = Rect((120,50),(50,50))
box2 = Rect((220,50),(50,50))
box3 = Rect((320,50),(50,50))
box4 = Rect((75,400),(350,50))
def draw():
    screen.fill('black')
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box2, "red")
    screen.draw.filled_rect(box3, "red")
    screen.draw.filled_rect(box4, "white")

def update():
    global box1_v1
    global box2_v2
    global box3_v3

    box1.y += box1_v1
    box2.y += box2_v2
    box3.y += box3_v3
  
    if box1.y > HEIGHT:
        box1.y = 0
    if box1.y < 0:
        box1.y = 0
        box1_v1 = -box1_v1


    if box2.y > HEIGHT:
        box2.y = 0
    if box2.y < 0:
        box2.y = 0
        box2_v2 = -box2_v2
    
    if box3.y > HEIGHT:
        box3.y = 0
    if box3.y < 0:
        box3.y = 0
         box3_v3 = -box3_v3

    if box1.colliderect(box4):
        box1_v1 = -box1_v1
    if box2.colliderect(box4):
        box2_v2 = -box2_v2
    if box3.colliderect(box4):
        box3_v3 = -box3_v3


       

pgzrun.go()

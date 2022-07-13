import pgzrun

HEIGHT = 600
WIDTH = 700

box1_v1 = 2
box2_v2 = 3
box3_v3 = 2

box1 = Rect((300,150),(50,50))
box2 = Rect((300,300),(50,50))
box3 = Rect((300,450),(50,50))
box4 = Rect((650,250),(30,200))
box5 = Rect((50,250),(30,200))

def draw():
    screen.fill('black')
    screen.draw.filled_rect(box1, "pink")
    screen.draw.filled_rect(box2, "brown")
    screen.draw.filled_rect(box3, "green")
    screen.draw.filled_rect(box4, "red")
    screen.draw.filled_rect(box5, "red")


def update():
    global box1_v1
    global box2_v2
    global box3_v3

    box1.x += box1_v1
    box2.x += box2_v2
    box3.x += box3_v3
  
    if box1.x > HEIGHT:
        box1.x = 0
    if box1.x < 0:
        box1.x = HEIGHT


    if box2.x > HEIGHT:
        box2.x = 0
    if box2.x < 0:
        box2.x = HEIGHT
    
    if box3.x > HEIGHT:
        box3.x = 0
    if box3.x < 0:
        box3.x = HEIGHT

    if box1.colliderect(box4):
        box1_v1 = -box1_v1
    if box2.colliderect(box4):
        box2_v2 = -box2_v2
    if box3.colliderect(box4):
        box3_v3 = -box3_v3

    if box1.colliderect(box5):
        box1_v1 = -box1_v1
    if box2.colliderect(box5):
        box2_v2 = -box2_v2
    if box3.colliderect(box5):
        box3_v3 = -box3_v3
    platform_control()

def platform_control():
    if keyboard.up and box4.y >0:
        box4.y -= 3 
    elif keyboard.down and box4.y < HEIGHT-200:
        box4.y += 3

    if keyboard.down and box5.y >0:
        box5.y -= 3 
    elif keyboard.up and box5.y < HEIGHT-200:
        box5.y += 3
    



pgzrun.go()
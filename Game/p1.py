import pgzrun

HEIGHT = 500
WIDTH = 500
box1_vx = 2

box1 = Rect((100,250),(50,50))
box2 = Rect((10,25),(50,50))
def draw():
    screen.fill('black')
    screen.draw.text("Hellow world", (20,50), color="white")
    screen.draw.rect(box1, "white")
    screen.draw.filled_rect(box2, "red")

def update():
    global box1_vx

    box1.x += box1_vx
    
    if box1.x > WIDTH:
        box1.x = 0
    if box1.x < 0:
        box1.x = WIDTH

    box2.y += 3
    if box2.y > HEIGHT:
        box2.y = 0

    if box1.colliderect(box2):
        box1_vx = -box1_vx

pgzrun.go()

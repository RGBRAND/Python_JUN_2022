import pgzrun

HEIGHT = 400
WIDTH = 600

item = Rect((300,250), (25,25))
ivy = 3
item2 = Rect((250,250), (25,25))
i2vy = 2

platform = Rect((WIDTH/2, HEIGHT-50), (250,25))

def item_motion_control(obj, plt, speed):   #define new function name as item_motion_control
    obj.y += speed
    if obj.y > HEIGHT:
        obj.y = 0
    if obj.y < 0:
        obj.y = 0
        speed = -speed          #apply reverse unit
    if obj.colliderect(plt):
        speed = -speed
    return speed

def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(item2, 'yellow')
    screen.draw.filled_rect(platform, 'brown')



def platform_control():
    if keyboard.left:
        platform.x -= 3
    elif keyboard.right:
        platform.x += 3
        

def update():
    global ivy
    global i2vy
    ivy = item_motion_control(item, platform, ivy)
    i2vy = item_motion_control(item2, platform, i2vy)
    platform_control()

    print(item.x, item.y, ivy)

pgzrun.go()
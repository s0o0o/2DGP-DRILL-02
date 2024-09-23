import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y= 90

tri = True
cir = False

right = True
up = False
down = False

cirCenterX = 400
cirCenterY = 400
cirRadius = 200

while(True):
    clear_canvas_now()
    
    grass.draw_now(400,30)
    character.draw_now(x,y)

    if(cir):
        for theta in range(0,360):
            x = (cirCenterX + cirRadius*math.cos(math.radians(theta)))
            y = (cirCenterY + cirRadius*math.sin(math.radians(theta)))
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
        cir = False
        tri = True
        right = True
        x = 400
        y= 90

    else if(tri):

        if(right):
            if(x>700):
                up =True
                right = False
            if(x==380):
                tri=False
                cir=True
                right = False
            else:
                x+=10
                delay(0.01)

        if(up):
            if(x<=400 and y>=200):
                up = False
                down = True
            else:
                x-=10
                y+=15
                delay(0.01)
    
        if(down):
            if(x<=0 and y<=90):
                down = False
                right = True
                y=90
            else:
                x-=10
                y-=15
                delay(0.01)

                

    
        

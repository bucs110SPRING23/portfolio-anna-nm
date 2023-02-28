import pygame
import random
import math
pygame.init()


while 1: 
    pygame.event.pump()
    sf = pygame.display.set_mode((600,600))
    sf.fill("white")

    pygame.display.flip()
    pygame.draw.rect(sf,"antiquewhite1",[0,0,600,600])
    pygame.draw.circle(sf, "lemonchiffon4", [300,300],300)
    pygame.draw.line(sf, "black", (0,300), (600, 300))
    pygame.draw.line(sf, "black", (300,0), (300, 600))

    for i in range(10):
        x = random.randrange(0, 600)
        y = random.randrange(0, 600) 
        distance_from_center = math.hypot(x-300, y-300) 
        if distance_from_center <= 300: 
            pygame.draw.circle(sf, "maroon", (x,y), 5)
        else: 
            pygame.draw.circle(sf, "skyblue4", (x,y), 5)
    

    pygame.display.flip()
    pygame.time.wait(7000)
    break
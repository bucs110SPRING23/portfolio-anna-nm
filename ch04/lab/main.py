import pygame
import random
import math
pygame.init()


while 1: 
    pygame.event.pump()
    sf = pygame.display.set_mode((600,600))
    sf.fill("beige")
    pygame.display.flip()

    pygame.draw.rect(sf,"lightgreen",[50,50,100,100])
    #pygame.display.flip()

    pygame.draw.rect(sf,"khaki",[200,50,100,100])
    pygame.display.flip()

    #box1 = pygame.Surface((100, 100))
    #box1.fill("lightgreen") 
    #box2 = pygame.Surface((100, 100))
    #box2.fill("khaki") 
    #sf.blit(box1, (50, 50))
    #sf.blit(box2, (100, 50))
    

    selection = None

    while selection == None: 
        
        
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 150 and 50 <= mouse_y <= 150:
                    selection = "player1"
                elif 200 <= mouse_x <= 300 and 50 <= mouse_y <= 150:
                    selection = "player2"

    sf.fill("white")
    pygame.display.flip()
    pygame.draw.rect(sf,"antiquewhite1",[0,0,600,600])
    pygame.draw.circle(sf, "lemonchiffon4", [300,300],300)
    pygame.draw.line(sf, "black", (0,300), (600, 300))
    pygame.draw.line(sf, "black", (300,0), (300, 600))

    score_1 = 0
    score_2 = 0

    for i in range(10):
        x1 = random.randrange(0, 600)
        y1 = random.randrange(0, 600) 
        x2 = random.randrange(0, 600)
        y2 = random.randrange(0, 600) 
        
        
        distance_from_center_1 = math.hypot(x1-300, y1-300) 
        distance_from_center_2 = math.hypot(x2-300, y2-300)

        if distance_from_center_1 <= 300: 
            score_1 += 1
            pygame.draw.circle(sf, "lightgreen", (x1,y1), 5)
            pygame.display.flip()
            pygame.time.wait(300)
        else:
            pygame.draw.circle(sf, "darkgreen", (x1,y1), 5)
            pygame.display.flip()
            pygame.time.wait(300)
        
        if distance_from_center_2 <= 300: 
            score_2 += 1
            pygame.draw.circle(sf, "khaki", (x2,y2), 5)
            pygame.display.flip()
            pygame.time.wait(300)
        else:
            pygame.draw.circle(sf, "brown", (x2,y2), 5)
            pygame.display.flip()
            pygame.time.wait(300) 
   
    pygame.display.flip()
    pygame.time.wait(1000)
    
    font = pygame.font.Font(None, 28)
    if score_1 > score_2: 
        text = font.render("The winner is player 1", True, "white")
        if selection == "layer1": 
            text1 = font.render("Good guess!", True, "white")
        else: 
            text1 = font.render("Incorrect guess!", True, "white")

    elif score_1 < score_2: 
        text = font.render("The winner is player 2", True, "white")
        if selection == "player2": 
            text1 = font.render("Good guess!", True, "white")
        else: 
            text1 = font.render("Incorrect guess!", True, "white")
    else: 
        text = font.render("Draw - No player wins", True, "white")
        text1 = ""

    sf.blit(text, (200, 300)) 
    sf.blit(text1, (220, 320)) 

    

    pygame.display.flip()
    pygame.time.wait(5000)
    break
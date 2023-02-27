import pygame
pygame.init()

sf = pygame.display.set_mode()
sf.fill("white")
pygame.time.wait(1000)

pygame.display.flip()
pygame.draw.rect(sf,"blue",[500,500,500,500])
pygame.draw.rect(sf,"blue",[500,50,500,500])

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here


# PART B - complete part B here


window.exitonclick()

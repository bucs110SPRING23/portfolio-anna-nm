import pygame
pygame.init()

sf = pygame.display.set_mode((600,600))

sf.fill("white")
print(pygame.time.wait(1000))

pygame.display.flip()
pygame.draw.rect(sf,"blue",[0,0,600,600])
pygame.draw.circle(sf, "pink", [300,300],300)
pygame.display.flip()
pygame.time.wait(10000)

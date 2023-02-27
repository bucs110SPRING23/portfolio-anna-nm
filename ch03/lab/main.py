import pygame
pygame.init()




sf = pygame.display.set_mode()
pygame.display.get_window_size()

sf.fill("white")
print(pygame.time.wait(1000))

pygame.display.flip()
pygame.draw.rect(sf,"blue",[500,500,500,500])
pygame.draw.rect(sf,"blue",[500,50,500,500])

pygame.display.flip()
pygame.time.wait(2000)

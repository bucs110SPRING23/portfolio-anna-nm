import pygame
pygame.init()


screen = pygame.display.set_mode()
screen.fill("brown")
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.circle(screen, "white", [200, 150], 50)
pygame.display.flip()
pygame.draw.circle(screen, "white", [200, 250], 80)
pygame.display.flip()
pygame.draw.circle(screen, "white", [200, 380], 100)
pygame.display.flip()

pygame.time.wait(5000)








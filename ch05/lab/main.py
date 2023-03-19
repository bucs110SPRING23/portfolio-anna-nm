import pygame
pygame.init()

#PART A:
def threenp1(n):
    n = float(n)
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

def threenp1range(upper_limit):
    threenp1_dict = {}
    for i in range(2, upper_limit+1): 
        threenp1_dict[i] = threenp1(i)
    return threenp1_dict



#PART B 
def graph_coordinates(threenp1_dict): 
    values_num = len(threenp1_dict)
    print(values_num)
    if values_num > 2: 
        while 1: 
            pygame.event.pump()
            sf = pygame.display.set_mode((600,600))
            sf.fill("beige")
            pygame.display.flip()
            pygame.draw.line(sf, (0, 0, 0), (50, 50), (50, 550), 2)  # y-axis
            pygame.display.flip()
            for i in range(2, values_num+1):                 
                pygame.draw.line(sf, 'black', (i*50, (threenp1_dict[i]+1)*50), ((i+1)*50,(threenp1_dict[i+1]+1)*50), 2)
                pygame.display.flip()
                pygame.time.wait(500)
            new_sf = pygame.transform.flip(sf, False, True)
            pygame.draw.line(new_sf, (0, 0, 0), (50, 550), (550, 550), 2)  # x-axis
            pygame.display.flip()
            sf.blit(new_sf, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            break 

if __name__ == "__main__":
    print(threenp1range(5))   
    graph_coordinates(threenp1range(5))                              
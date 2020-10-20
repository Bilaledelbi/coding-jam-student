import pygame
from pygame.locals import *
import time
#intiating the windonw
pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
WIDTH = 450
HEIGHT = 244
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mecanical simulation")
WHITE = (255, 255, 255)
background = pygame.image.load("Backgrounds/road.jpg").convert()
#Done

#car animation
car = [pygame.image.load("car assets/car01.png"), pygame.image.load("car assets/car02.png"),
 pygame.image.load("car assets/car03.png"), pygame.image.load("car assets/car04.png")]




  
def play(F=0,M=1,V0=0):
    count = 0
    running = True
    # physics/placment constants
    x = 20
    x0 = x
    y = 190
    forces = []
    f = F
    m = M
    v0 = V0
    start = time.time()
    for i in forces:
        f += i
    a = f / m


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    v0 = 10



        def setvariables(v0, mass, f1, f2):
            M = mass
            V0 = v0
            F = f1 + f2
            print(M + V0 + F)

        end = time.time()
        T = end - start
        d = 20+(x - x0)
        #print("{:.2f}".format(T) + "s")
        V = (a * T) + v0
        #print("{:.2f}".format(d) + "m")
        x = ((0.5*a*(T**2)) + v0 * T)/1.2


        WIN.blit(background, [0, 0])
        if count + 1 >= 12:
            count = 0

        WIN.blit(car[count // 3], [x, y])
        if(V != 0):
            count += 1


        #label = myfont.render("Some text!", 1, (255,255,0))
		#WIN.blit(label, (100, 100))

    	

        #pygame.draw.rect(WIN, (0, 0, 0), (x, y, 60, 40))
        pygame.display.update()
    pygame.quit()

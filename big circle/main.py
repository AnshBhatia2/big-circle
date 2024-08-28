import pygame
pygame.init()

screen = pygame.display.set_mode([800,600])

red = (255,0,0)
green = (0, 255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)

screen.fill(white)

class Circle():
    def __init__(circ,color,pos,radius,width=0):
        circ.pos = pos
        circ.radius = radius
        circ.color = color
        circ.width = width
        circ.screen = screen

    def draw(circ):
        pygame.draw.circle(circ.screen,circ.color,circ.pos,circ.radius,circ.width)

    def grow(circ,x):
        circ.radius += x
        pygame.draw.circle(circ.screen,circ.color,circ.pos,circ.radius,circ.width)

pos = (300,300)
radius = 50
width = 2
pygame.draw.circle(screen, red, pos, radius, width)
pygame.display.update()

blueCircle = Circle(blue, pos, radius+60)
redCircle = Circle(red, pos, radius+40)
yellowCircle = Circle(yellow, pos, radius, 5)
greenCircle = Circle(green, pos, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = Circle(black, pos, 5)
            blackCircle.draw()
            pygame.display.update()
        
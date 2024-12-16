import pygame

from pygame.locals import *
        
        

resolution = (400, 300)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

class Ball:
    def __init__(self, xPos = resolution[0]/2, yPos = resolution[1]/2, xVel = 1, yVel = 1, rad = 15):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
    
    def draw(self, surface):
        pygame.draw.circle(surface, black, (self.x, self.y), self.radius)

    def update(self, surface):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.draw(surface)

screen = pygame.display.set_mode(resolution)
ball = Ball()
while True:
    screen.fill(white)
    ball.update(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

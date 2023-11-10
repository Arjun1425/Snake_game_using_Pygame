import pygame
from pygame.locals import *

def generate_snake():
    surface = pygame.display.set_mode(size = (1000,500))
    surface.fill((110, 110, 5)) 
    surface.blit(snake, (snake_x,snake_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode(size = (1000,500))
    surface.fill((110, 110, 5)) 
    
    snake = pygame.image.load("resources/block.jpg").convert()
    snake_x = 100
    snake_y = 100
    surface.blit(snake, (snake_x,snake_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    snake_y -= 10
                    generate_snake()
                elif event.key == K_DOWN:
                    snake_y += 10
                    generate_snake()
                elif event.key == K_RIGHT:
                    snake_x += 10
                    generate_snake()
                elif event.key == K_LEFT:
                    snake_x -= 10
                    generate_snake()

           
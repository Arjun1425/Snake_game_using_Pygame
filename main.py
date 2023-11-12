import pygame 
from pygame.locals import *

class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.generate_snake()
        self.run()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    elif event.key == K_UP:
                        self.snake.move_up()
                        
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                        
                    elif event.key == K_RIGHT:
                        self.snake.move_right()

                    elif event.key == K_LEFT:
                        self.snake.move_left() 

class Snake:

    def __init__(self, new_surface):
        self.new_surface = new_surface
        self.snake = pygame.image.load("resources/block.jpg").convert()
        self.snake_x = 100
        self.snake_y = 100

    def generate_snake(self):
        self.new_surface.fill((110,110,5))
        self.new_surface.blit(self.snake, (self.snake_x,self.snake_y))
        pygame.display.flip()

    def move_up(self):
        self.snake_y -= 10
        self.generate_snake()

    def move_down(self):
        self.snake_y += 10
        self.generate_snake()

    def move_right(self):
        self.snake_x += 10
        self.generate_snake()

    def move_left(self):
        self.snake_x -= 10    
        self.generate_snake()

if __name__ == '__main__':
    game = Game()
    game.run()
import pygame 
from pygame.locals import *
import time
import random
class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,1000))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.generate_snake()
        self.apple = Apple(self.surface)
        self.apple.generate_apple()
        

    def play(self):
        self.snake.walk()
        self.apple.generate_apple()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.snake_x[0],self.snake.snake_y[0],self.apple.apple_x,self.apple.apple_y):
            self.snake.increase_length()
            self.apple.move()
    
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}", True, (255,255,255))
        self.surface.blit(score, (800,10))

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
            
            self.play()
            time.sleep(0.5)

size = 40

class Snake:

    def __init__(self, new_surface, length=4):
        self.length = length
        self.new_surface = new_surface
        self.snake = pygame.image.load("resources/block.jpg").convert()
        self.snake_x = [size]*length 
        self.snake_y = [size]*length 
        self.direction = 'down'
        
    def generate_snake(self):
        self.new_surface.fill((110,110,5))
        for i in range(self.length):
            self.new_surface.blit(self.snake, (self.snake_x[i] ,self.snake_y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length +=1
        self.snake_x.append(-1)
        self.snake_y.append(-1)

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def walk(self):  
        
        for i in range(self.length - 1, 0, -1):
            self.snake_x[i] = self.snake_x[i-1]
            self.snake_y[i] = self.snake_y[i-1]

        if self.direction == 'up':
            self.snake_y[0] -= size

        elif self.direction == 'down':
            self.snake_y[0] += size

        elif self.direction == 'right':
            self.snake_x[0] += size
            
        elif self.direction == 'left':
            self.snake_x[0] -= size           
        self.generate_snake()

class Apple:

    def __init__(self, new_surface):
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.new_surface = new_surface
        self.apple_x =  size*3
        self.apple_y =  size*3   
    
    def generate_apple(self):
        self.new_surface.blit(self.apple, (self.apple_x ,self.apple_y))
        pygame.display.flip()

    def move(self):
        self.apple_x = random.randint(1,24)*size
        self.apple_y = random.randint(1,19)*size

if __name__ == '__main__':
    game = Game()
    game.run()
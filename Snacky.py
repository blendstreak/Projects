#Controls are 'WASD'. You could edit them.
import random 
import sys
import pygame
from pygame.math import Vector2
pygame.init()

cell_number = 20
cell_size = 20

width = cell_size * cell_number
height = cell_size * cell_number

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake game by Abhi")

game_font = pygame.font.Font(None, 50)

class Snake(object):
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.color = (225, 225, 125)
        self.direction = Vector2(1, 0)
        self.new_bock = False
        
    def move(self):
        if snake.new_bock:
            new_body = self.body[:]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body
            snake.new_bock = False
        else:
            new_body = self.body[: - 1]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body
            
    def draw(self):
        for block in self.body:
            self.x = block.x * cell_size
            self.y = block.y * cell_size
            snake_rect = pygame.Rect(self.x, self.y, cell_size, cell_size)
            pygame.draw.rect(screen, self.color, snake_rect)
            
    def add_block(self):
        snake.new_bock = True
        
    def check_hit(self):
        for block in self.body[1:]:
            if block == self.body[0]:
                print(f"your score was : {str(len(self.body) - 3)}")
                pygame.quit()
                sys.exit()
                
        if not 0 <= self.body[0].x < cell_number or not 0 <= self.body[0].y < cell_number:
            print(f"YOUR SCORE WAS : {str(len(self.body) - 3)}")
            pygame.quit()
            sys.exit()
            
            
class Fruit(object):
    def __init__(self):
        self.randomize()
        self.color = (225, 125, 125)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = (self.x, self.y)
        
    def draw(self):
        fruit_rect = pygame.Rect(self.x * cell_number, self.y * cell_number, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, fruit_rect)


def eat():
    if fruit.pos == snake.body[0]:
        snake.add_block()
        fruit.randomize()
    for block in snake.body:
        if fruit.pos == block:
            fruit.randomize()
            
            
def draw_score():
    score_text = str(len(snake.body) - 3)
    score_surface = game_font.render(score_text, True, (225, 225, 225))
    score_x = int(cell_size * cell_number- 60)
    score_y = int(cell_size * cell_number - 40)
    score_rect = score_surface.get_rect(center = (score_x, score_y))
    screen.blit(score_surface, score_rect)
 
    
fruit = Fruit()
snake = Snake()
black = (0, 0, 0)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_s:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_d:
                if snake.direction.x != -1:
                    snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_a:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
                    
    screen.fill(black)
    eat()
    snake.draw()
    snake.check_hit()
    draw_score()
    snake.move()
    fruit.draw()
    pygame.display.update()
    clock.tick(14)

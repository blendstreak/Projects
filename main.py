import pygame
import sys
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 500

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Paddle(object):
    def __init__(self, x, paddle):
        self.x = x
        self.speed = 7
        self.y = (HEIGHT//2 - HEIGHT//10)
        self.paddle = paddle
        self.color = (255, 255, 255)
        self.moveUp = False
        self.moveDown = False

    
    def draw(self):
        self.paddle_rect = pygame.Rect(self.x, self.y, 5, HEIGHT//5)
        pygame.draw.rect(screen, self.color, self.paddle_rect)

    def update(self):
        self.paddle_rect = pygame.Rect(self.x, self.y, 5, HEIGHT//5)
    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if self.paddle == "right":
                if event.key == pygame.K_UP:
                    self.moveUp = True
                if event.key == pygame.K_DOWN:
                    self.moveDown = True
            
            if self.paddle == "left":
                if event.key == pygame.K_w:
                    self.moveUp = True
                if event.key == pygame.K_s:
                    self.moveDown = True
        
        elif event.type == pygame.KEYUP:
            if self.paddle == "right":
                if event.key == pygame.K_UP:
                    self.moveUp = False
                if event.key == pygame.K_DOWN:
                    self.moveDown = False
            
            if self.paddle == "left":
                if event.key == pygame.K_w:
                    self.moveUp = False
                if event.key == pygame.K_s:
                    self.moveDown = False    
    
    def checkMoving(self):
        if self.moveUp and self.y > 0:
            self.y -= self.speed
        if self.moveDown and self.y + HEIGHT/5 < 500:
            self.y += self.speed

class Ball(object):
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.pos = (self.x, self.y)
        self.radius = 7
        self.speedx = 7 * random.choice((1, -1))
        self.speedy = 7 * random.choice((1, -1))
        self.ball_rect = pygame.Rect(WIDTH//2 - 8, HEIGHT//2 - 8, 16, 16)
        
        
    def draw_and_move(self):
        pygame.draw.ellipse(screen, WHITE, self.ball_rect)
        
        self.ball_rect.x += self.speedx
        self.ball_rect.y += self.speedy
    
    def reset(self):
        self.ball_rect.center = (WIDTH // 2, HEIGHT// 2)
        self.speedx *= random.choice((1, -1))
        self.speedy *= random.choice((1, -1))

paddleLeft = Paddle(5, paddle="left")
paddleRight = Paddle(WIDTH - 10, paddle="right")

ball = Ball()
paddleLeft_score = 0
paddleRight_score = 0
collisions = 0

def check_collision(ball):
    global collisions, paddleLeft_score, paddleRight_score
    if ball.ball_rect.top <= 0 or ball.ball_rect.bottom >= HEIGHT:
        ball.speedy *= -1
    if ball.ball_rect.left <= 0:
        if collisions != 0:
            paddleRight_score += 1
        ball.reset()
        collisions = 0
    if ball.ball_rect.right >= WIDTH:
        if collisions != 0:
            paddleLeft_score += 1
        ball.reset()
        collisions = 0
    if ball.ball_rect.colliderect(paddleLeft.paddle_rect) or ball.ball_rect.colliderect(paddleRight.paddle_rect):
        ball.speedx *= -1
        collisions += 1


def bot():
    if paddleRight.paddle_rect.centery < ball.ball_rect.centery:
        if paddleRight.y + paddleRight.paddle_rect.height < HEIGHT:
            paddleRight.y += 5
    elif paddleRight.paddle_rect.centery > ball.ball_rect.centery:
        if paddleRight.y > 0:
            paddleRight.y -= 5

font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        paddleLeft.move(event)
        paddleRight.move(event)

    screen.fill((0, 0, 0))

    paddleLeft.checkMoving()
    paddleRight.checkMoving()
    
    pygame.draw.aaline(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (WIDTH//2, 0), (WIDTH//2, 500))

    text = font.render(f"{paddleLeft_score} : {paddleRight_score}", True, WHITE, BLACK)
    text.set_alpha(127)
    textRect = text.get_rect()
    textRect.center = (WIDTH//2, HEIGHT//2)
    screen.blit(text, textRect)

    paddleLeft.draw()
    paddleRight.draw()
    ball.draw_and_move()

    check_collision(ball)
    paddleLeft.update()
    paddleRight.update()
    bot()
    pygame.display.update()
    clock.tick(60)

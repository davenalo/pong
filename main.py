import pygame, random

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

pygame.display.set_caption("Pong")

WHITE = (255, 255, 255) # RGB
BLACK = (0, 0, 0,)

r = random.randint(0, 255)

g = random.randint(0, 255)

b = random.randint(0, 255)

COLORFUL = (r, g, b)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Ball:

    COLOR = WHITE
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = MAX_VEL
        self.y_vel = 0


class Paddle:
    '''las paletas se repiten, y sus movimientos también'''
    COLOR = COLORFUL
    VEL = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def handdle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 5:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT - 5:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 5:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT - 5:
        right_paddle.move(up=False)    

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    line = Paddle(348, 0, WIDTH - 698, 500)
    '''utilizo Paddle para hacer una línea en el centro del campo, un poco cutre pero bueno'''

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle, line])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handdle_paddle_movement(keys, left_paddle, right_paddle)
    pygame.quit()

if __name__=="__main__":
    main()
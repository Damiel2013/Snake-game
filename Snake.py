import pygame
import random
pygame.font.init()

WIN_WIDTH = 1000
WIN_HEIGHT = 700
FPS = 10

PIXEL_WIDTH = 10

STAT_FONT = pygame.font.SysFont("comicsans", 50)

class Snake:
    direction = 1   #N:0  E:1  S:2  W:3
    length = 1


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snake_pos = [(x, y)]

    def move(self):
        if len(self.snake_pos) > 1:
            i = len(self.snake_pos)-1
            while i >= 1:
                self.snake_pos[i] = self.snake_pos[i-1]
                i -= 1
        self.snake_pos[0] = (self.x, self.y)

    def move_north(self):
        if self.direction != 2:
            self.direction = 0
            self.y -= PIXEL_WIDTH
            self.move()
        else:
            self.idle()

    def move_east(self):
        if self.direction != 3:
            self.direction = 1
            self.x += PIXEL_WIDTH
            self.move()
        else:
            self.idle()

    def move_west(self):
        if self.direction != 1:
            self.direction = 3
            self.x -= PIXEL_WIDTH
            self.move()
        else:
            self.idle()

    def move_south(self):
        if self.direction != 0:
            self.direction = 2
            self.y += PIXEL_WIDTH
            self.move()
        else:
            self.idle()

    def idle(self):
        if self.direction == 0:
            self.move_north()
        elif self.direction == 1:
            self.move_east()
        elif self.direction == 2:
            self.move_south()
        else:
            self.move_west()

    def eat(self):
        new_pos = self.snake_pos[-1]
        self.snake_pos.append(new_pos)

    def draw(self, win):
        #rect(surface, color, rect, width=0)
        color = (0, 255, 0)
        for spos in self.snake_pos:
            pygame.draw.rect(win, color, (spos[0], spos[1], PIXEL_WIDTH, PIXEL_WIDTH))
'''
class Pixel:
    WIDTH = PIXEL_WIDTH
    snake = False
    food = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self ,win):
        #rect(surface, color, rect, width=0)
        color = (255, 255, 255)
        pygame.draw.rect(win, color, (self.x, self.y, self.WIDTH, self.WIDTH),1)
'''
class Food:
    x = PIXEL_WIDTH*random.randrange(0, WIN_WIDTH//PIXEL_WIDTH-1)
    y = PIXEL_WIDTH*random.randrange(0, WIN_HEIGHT//PIXEL_WIDTH-1)

    def __init__(self):
        pass

    def draw(self, win):
        color = (255, 0, 0)
        pygame.draw.rect(win, color, (self.x, self.y, PIXEL_WIDTH, PIXEL_WIDTH))

    def reset(self, snake_pos):
        while snake_pos[0] == self.x and snake_pos[1] == self.y:
            self.x = PIXEL_WIDTH*random.randrange(0, WIN_WIDTH//PIXEL_WIDTH-1)
            self.y = PIXEL_WIDTH*random.randrange(0, WIN_HEIGHT//PIXEL_WIDTH-1)

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = Snake(PIXEL_WIDTH*3, PIXEL_WIDTH*3)
    food = Food()
    score = 0
    '''
    i, x, y, length = 0, 0, 0, (WIN_WIDTH//PIXEL_WIDTH)*(WIN_HEIGHT//PIXEL_WIDTH)
    pixels = []
    while i < length:
        if x >= WIN_WIDTH//PIXEL_WIDTH:
            x = 0
            y += 1
        pixels.append(Pixel(PIXEL_WIDTH*x, PIXEL_WIDTH*y))
        x += 1
        i += 1
    '''
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            snake.move_north()
        elif key[pygame.K_DOWN]:
            snake.move_south()
        elif key[pygame.K_LEFT]:
            snake.move_west()
        elif key[pygame.K_RIGHT]:
            snake.move_east()
        else:
            snake.idle()

        if snake.x == food.x and snake.y == food.y:
            score += 1
            snake.eat()
            food.reset((snake.x, snake.y))

        i = len(snake.snake_pos) - 1
        while i >= 1:
            if snake.snake_pos[i][0] == snake.x and snake.snake_pos[i][1] == snake.y and len(snake.snake_pos) > 2:
                print('Your final score is: ' + str(score))
                run = False
                break
            i -= 1

        if snake.x < 0 or snake.x + PIXEL_WIDTH > WIN_WIDTH or snake.y < 0 or snake.y + PIXEL_WIDTH > WIN_HEIGHT:
            print('Your final score is: ' + str(score))
            run = False
            break

        draw_window(win, snake, food, score)

def draw_window(win, snake, food, score):
    color = (0, 0, 0)
    pygame.draw.rect(win, color, (0, 0, WIN_WIDTH, WIN_HEIGHT))
    '''
    for pixel in pixels:
        pixel.draw(win)
    '''
    food.draw(win)
    snake.draw(win)
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    pygame.display.update()

main()

import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)

# screen size
width = 600
height = 400

# create window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Skane Game")

# Clock
clock = pygame.time.Clock()

# Snake block size
block = 20
speed = 15

# Font
font = pygame.font.SysFont("Arial", 25)

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])

def game_loop():
    end_of_game = False
    game_over = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake = []
    snake_size = 1

    food_x = round(random.randrange(0, width - block) / block) * block
    food_y = round(random.randrange(0, height - block) / block) * block

    while not end_of_game:

        while game_over:
            screen.fill(black)
            message("You lose! Press Q to quit or C to play again.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end_of_game = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_of_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = block

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        screen.fill(black)
        pygame.draw.rect(screen, green, [food_x, food_y, block, block])

        head = []
        head.append(x)
        head.append(y)
        snake.append(head)

        if len(snake) > snake_size:
            del snake[0]

        for part in snake[:-1]:
            if part == head:
                game_over = True

        for part in snake:
            pygame.draw.rect(screen, white, [part[0], part[1], block, block])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block) / block) * block
            food_y = round(random.randrange(0, height - block) / block) * block
            snake_size += 1

        clock.tick(speed)
    
    show_score(snake_size - 1)
    pygame.quit()
    quit()

def home_menu():
    while True:
        screen.fill(black)
        message("Press SPACE to play or Q to quit", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
home_menu()

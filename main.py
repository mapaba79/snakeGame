import pygame
import time
import random

pygame.init()

# Sounds
try:
    eat_sound = pygame.mixer.Sound("eat.mp3")
except pygame.error:
    print("Warning: 'eat.mp3' not found. Sound effects will not play.")
    eat_sound = None

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
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Snake block size
block = 20
speed = 15

# Font
font = pygame.font.SysFont("Arial", 25)
large_font = pygame.font.SysFont("Arial", 50) # Added for bigger "Game Over" message

# Modifique a função message para aceitar um y_position opcional
def message(msg, color, y_position=None, font_type=font):
    text = font_type.render(msg, True, color)
    text_rect = text.get_rect(center=(width / 2, y_position if y_position is not None else height / 3))
    screen.blit(text, text_rect)

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

            # CALCULE AS POSIÇÕES VERTICAIS PARA CADA MENSAGEM AQUI
            # Exemplo: Comece no 1/3 da altura e adicione um espaçamento para cada linha
            game_over_y = height / 3
            score_y = game_over_y + 60 # Ajuste este valor para mais ou menos espaço
            restart_quit_y = score_y + 40 # Ajuste este valor

            message("Game Over!", red, y_position=game_over_y, font_type=large_font)
            message(f"You lose! Your score: {snake_size - 1}", white, y_position=score_y)
            message("Press C to play again or Q to quit.", red, y_position=restart_quit_y, font_type=font)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end_of_game = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    end_of_game = True
                    game_over = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_of_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -block
                elif event.key == pygame.K_DOWN and y_change == 0:
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

        show_score(snake_size - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            if eat_sound:
                pygame.mixer.Sound.play(eat_sound)
            food_x = round(random.randrange(0, width - block) / block) * block
            food_y = round(random.randrange(0, height - block) / block) * block
            snake_size += 1

        clock.tick(speed)
    
    pygame.quit()
    quit()

def home_menu():
    while True:
        screen.fill(black)
        # Para o menu, a mensagem pode continuar centralizada em height / 3
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

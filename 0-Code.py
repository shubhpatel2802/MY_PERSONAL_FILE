import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

# Snake initial position
x1, y1 = width // 2, height // 2
x1_change, y1_change = 0, 0

# Initial length of the snake
snake_length = 1
snake_list = []

# Food settings
food_size = 10
food_x = round(random.randrange(0, width - food_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - food_size) / 10.0) * 10.0

# Clock to control the snake speed
clock = pygame.time.Clock()

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

# Run the game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Update snake position
    x1 += x1_change
    y1 += y1_change

    # Check for collisions with walls
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    # Update snake length when it eats the food
    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, width - food_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - food_size) / 10.0) * 10.0
        snake_length += 1

    # Update snake body
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collisions with itself
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw everything
    win.fill(black)
    pygame.draw.rect(win, red, [food_x, food_y, food_size, food_size])
    our_snake(snake_block, snake_list)

    # Update display
    pygame.display.update()

    # Control the snake speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()

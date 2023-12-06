import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space War")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player settings
player_width, player_height = 50, 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Enemy settings
enemy_width, enemy_height = 50, 50
enemy_speed = 3

# Bullet settings
bullet_width, bullet_height = 5, 15
bullet_speed = 7
max_bullets = 5

# Clock to control frame rate
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
bullet_img = pygame.image.load('bullet.png')

# Function to draw the player
def draw_player(x, y):
    win.blit(player_img, (x, y))

# Function to draw an enemy
def draw_enemy(x, y):
    win.blit(enemy_img, (x, y))

# Function to draw a bullet
def draw_bullet(x, y):
    win.blit(bullet_img, (x, y))

# Main game loop
def game_loop():
    player_x_change = 0
    player_bullets = []

    enemy_x = random.randint(0, width - enemy_width)
    enemy_y = 0

    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -player_speed
                elif event.key == pygame.K_RIGHT:
                    player_x_change = player_speed
                elif event.key == pygame.K_SPACE and len(player_bullets) < max_bullets:
                    player_bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change

        # Boundaries for player
        if player_x < 0:
            player_x = 0
        elif player_x > width - player_width:
            player_x = width - player_width

        # Update enemy position
        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_x = random.randint(0, width - enemy_width)
            enemy_y = 0
            score += 1

        # Update bullet positions
        for bullet in player_bullets:
            bullet[1] -= bullet_speed

        # Check for collisions with enemy
        for bullet in player_bullets:
            if (
                enemy_x < bullet[0] < enemy_x + enemy_width and
                enemy_y < bullet[1] < enemy_y + enemy_height
            ):
                enemy_x = random.randint(0, width - enemy_width)
                enemy_y = 0
                score += 10
                player_bullets.remove(bullet)

        # Draw everything
        win.fill(black)
        draw_player(player_x, player_y)
        draw_enemy(enemy_x, enemy_y)
        for bullet in player_bullets:
            draw_bullet(bullet[0], bullet[1])

        # Display score
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, white)
        win.blit(score_text, (10, 10))

        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()

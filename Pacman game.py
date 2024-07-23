import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PACMAN Game")

# Pacman settings
pacman_size = 20
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
pacman_speed = 5

# Ghost settings
ghost_size = 20
ghosts = []

for _ in range(4):
    ghost_x = random.randint(0, SCREEN_WIDTH - ghost_size)
    ghost_y = random.randint(0, SCREEN_HEIGHT - ghost_size)
    ghosts.append((ghost_x, ghost_y))

# Pellet settings
pellet_size = 5
pellets = []

for _ in range(50):
    pellet_x = random.randint(0, SCREEN_WIDTH - pellet_size)
    pellet_y = random.randint(0, SCREEN_HEIGHT - pellet_size)
    pellets.append((pellet_x, pellet_y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    screen.fill(BLACK)

    # Draw Pacman
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size)

    # Draw Ghosts
    for ghost_x, ghost_y in ghosts:
        pygame.draw.rect(screen, RED, (ghost_x, ghost_y, ghost_size, ghost_size))

    # Draw Pellets
    for pellet_x, pellet_y in pellets:
        pygame.draw.circle(screen, WHITE, (pellet_x, pellet_y), pellet_size)

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()

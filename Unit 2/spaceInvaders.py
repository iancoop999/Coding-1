import math
import random

try:
    import pygame  # type: ignore[import-not-found]
except ImportError as exc:
    raise SystemExit(
        "Pygame is required. Install it with: python -m pip install pygame"
    ) from exc

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 120, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 30
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 60
player_x_change = 0
player_speed = 5

# Bullet settings
bullet_width = 7
bullet_height = 17
bullet_x = 0
bullet_y = player_y
bullet_y_change = -10
bullet_state = "ready"  # "ready" means you can't see the bullet, "fire" means it's moving

# Alien settings
alien_width = 40
alien_height = 30
num_of_aliens = 7
aliens = []

for i in range(num_of_aliens):
  aliens.append({
      "x": random.randint(50, SCREEN_WIDTH - 100),
      "y": random.randint(50, 150),
      "x_change": 3,
      "y_change": 40,
  })

# Score
score_value = 0
font = pygame.font.Font(None, 36)


def show_score(x, y):
  score = font.render(f"Score: {score_value}", True, WHITE)
  screen.blit(score, (x, y))


def player(x, y):
  pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))
  # Draw a little cannon on top
  pygame.draw.rect(
      screen,
      GREEN,
      (x + player_width // 2 - 4, y - 10, 8, 10),
  )


def alien(x, y):
  pygame.draw.rect(screen, RED, (x, y, alien_width, alien_height))


def fire_bullet(x, y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(
      pygame.Surface((bullet_width, bullet_height)),
      (x + player_width // 2 - bullet_width // 2, y),
      pygame.draw.rect(
          screen, BLUE, (x + player_width // 2 - bullet_width // 2, y, bullet_width, bullet_height)
      ),
      (0, 0),
  )


def is_collision(alien_x, alien_y, bullet_x, bullet_y):
  distance = math.sqrt(
      math.pow(alien_x - bullet_x, 2) + math.pow(alien_y - bullet_y, 2)
  )
  if distance < 27:
    return True
  return False


# Game Loop
running = True
while running:
  # RGB Background fill
  screen.fill(BLACK)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # If keystroke is pressed check whether it's right or left
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_x_change = -player_speed
      if event.key == pygame.K_RIGHT:
        player_x_change = player_speed
      if event.key == pygame.K_SPACE:
        if bullet_state == "ready":
          bullet_x = player_x
          fire_bullet(bullet_x, bullet_y)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player_x_change = 0

  # --- Player Movement ---
  player_x += player_x_change
  if player_x <= 0:
    player_x = 0
  elif player_x >= SCREEN_WIDTH - player_width:
    player_x = SCREEN_WIDTH - player_width

  # --- Alien Movement ---
  for a in aliens:
    # Game Over check
    if a["y"] > SCREEN_HEIGHT - 100:
      for alb in aliens:
        alb["y"] = 2000  # Move all aliens down off screen
      running = False
      break

    a["x"] += a["x_change"]
    if a["x"] <= 0:
      a["x_change"] = 3
      a["y"] += a["y_change"]
    elif a["x"] >= SCREEN_WIDTH - alien_width:
      a["x_change"] = -3
      a["y"] += a["y_change"]

    # Collision Check
    collision = is_collision(a["x"], a["y"], bullet_x, bullet_y)
    if collision:
      bullet_y = player_y
      bullet_state = "ready"
      score_value += 1
      # Respawn alien
      a["x"] = random.randint(50, SCREEN_WIDTH - 100)
      a["y"] = random.randint(50, 150)

    alien(a["x"], a["y"])

  # --- Bullet Movement ---
  if bullet_y <= 0:
    bullet_y = player_y
    bullet_state = "ready"

  if bullet_state == "fire":
    fire_bullet(bullet_x, bullet_y)
    bullet_y += bullet_y_change

  # Draw Player and Score
  player(player_x, player_y)
  show_score(10, 10)

  pygame.display.update()
  clock.tick(60)

pygame.quit()
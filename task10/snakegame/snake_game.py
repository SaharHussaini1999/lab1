import pygame
import random
import sys
from user_db import get_or_create_user, get_latest_level, save_score

# ---------------------
# Level settings
# ---------------------


def get_level_settings(level):
    if level == 1:
        return 5
    elif level == 2:
        return 10
    elif level == 3:
        return 15
    return 5


# ---------------------
# User setup
# ---------------------
username = input("Enter your username: ")
user_id = get_or_create_user(username)
level = get_latest_level(user_id)
print(f"Welcome {username}! Starting at level {level}")
FPS = get_level_settings(level)

# ---------------------
# Pygame setup
# ---------------------
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WALL_COLOR = (100, 100, 100)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# ---------------------
# Game State
# ---------------------
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)

foods = []
food_weights = [1, 2, 3]
food_lifetime = 50

score = 0
paused = False
walls = []

# ---------------------
# Food Spawner
# ---------------------


def spawn_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            break
    weight = random.choice(food_weights)
    foods.append({"pos": (x, y), "weight": weight, "timer": food_lifetime})

# ---------------------
# Walls Generator
# ---------------------


def generate_walls(level):
    walls = []
    # Border walls
    for x in range(0, WIDTH, CELL_SIZE):
        walls.append((x, 0))
        walls.append((x, HEIGHT - CELL_SIZE))
    for y in range(0, HEIGHT, CELL_SIZE):
        walls.append((0, y))
        walls.append((WIDTH - CELL_SIZE, y))

    if level == 2:
        # Horizontal barrier with gap
        barrier_y = int(HEIGHT * 2 / 3)
        gap_start = WIDTH // 2 - 2 * CELL_SIZE
        gap_end = WIDTH // 2 + 2 * CELL_SIZE
        for x in range(0, WIDTH, CELL_SIZE):
            if gap_start <= x < gap_end:
                continue
            walls.append((x, barrier_y))

        # Vertical pillars in corners
        for y in range(0, 3 * CELL_SIZE, CELL_SIZE):
            walls.append((CELL_SIZE * 2, y + CELL_SIZE * 2))
            walls.append((WIDTH - 3 * CELL_SIZE, y + CELL_SIZE * 2))

    elif level == 3:
        # Center box
        box_start_x = WIDTH // 2 - 3 * CELL_SIZE
        box_end_x = WIDTH // 2 + 3 * CELL_SIZE
        box_start_y = HEIGHT // 2 - 3 * CELL_SIZE
        box_end_y = HEIGHT // 2 + 3 * CELL_SIZE
        for x in range(box_start_x, box_end_x, CELL_SIZE):
            walls.append((x, box_start_y))
            walls.append((x, box_end_y - CELL_SIZE))
        for y in range(box_start_y, box_end_y, CELL_SIZE):
            walls.append((box_start_x, y))
            walls.append((box_end_x - CELL_SIZE, y))

        # Side vertical walls
        for y in range(CELL_SIZE * 4, HEIGHT - CELL_SIZE * 4, CELL_SIZE):
            walls.append((CELL_SIZE * 5, y))
            walls.append((WIDTH - 6 * CELL_SIZE, y))

    return walls


# ---------------------
# Initialize first walls
# ---------------------
walls = generate_walls(level)
spawn_food()

# ---------------------
# Game Loop
# ---------------------
running = True
while running:
    screen.fill(BLACK)

    # ----------------- Event Handling -----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, level, score)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused!")
                    save_score(user_id, level, score)
                else:
                    print("Game resumed!")

    # ----------------- Movement Input -----------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # ----------------- Pause State -----------------
    if paused:
        pause_text = font.render("PAUSED", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(5)
        continue

    # ----------------- Move Snake -----------------
    head_x, head_y = snake[0]
    new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
    snake.insert(0, new_head)

    # ----------------- Collision: Wall -----------------
    if new_head in walls:
        print("Game Over! You hit a wall!")
        save_score(user_id, level, score)
        pygame.quit()
        sys.exit()

    # ----------------- Collision: Edge -----------------
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        print("Game Over! You hit the edge!")
        save_score(user_id, level, score)
        pygame.quit()
        sys.exit()

    # ----------------- Collision: Self -----------------
    if new_head in snake[1:]:
        print("Game Over! You bit yourself!")
        save_score(user_id, level, score)
        pygame.quit()
        sys.exit()

    # ----------------- Check Food Collision -----------------
    eaten = False
    for food in foods[:]:
        if new_head == food["pos"]:
            score += food["weight"]
            foods.remove(food)
            spawn_food()
            eaten = True
            break

    if not eaten:
        snake.pop()

    # ----------------- Update Foods -----------------
    for food in foods[:]:
        pygame.draw.rect(screen, RED, (*food["pos"], CELL_SIZE, CELL_SIZE))
        food["timer"] -= 1
        if food["timer"] <= 0:
            foods.remove(food)
            spawn_food()

    # ----------------- Draw Walls -----------------
    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOR, (*wall, CELL_SIZE, CELL_SIZE))

    # ----------------- Draw Snake -----------------
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

    # ----------------- Draw Score & Level -----------------
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(level_text, (10, 40))

    # ----------------- Level Progression -----------------
    if score >= 10 and level == 1:
        level = 2
        FPS = get_level_settings(level)
        walls = generate_walls(level)
        save_score(user_id, level, score)
        print(f"Level up! Now Level {level} (saved to DB)")

    elif score >= 20 and level == 2:
        level = 3
        FPS = get_level_settings(level)
        walls = generate_walls(level)
        save_score(user_id, level, score)
        print(f"Level up! Now Level {level} (saved to DB)")

    # ----------------- Refresh Display -----------------
    pygame.display.flip()
    clock.tick(FPS)

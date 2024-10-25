import pygame
import os

def run_game(screen_size):
    pygame.init()
    
    # Set window size based on the passed dimensions
    width, height = screen_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Brick Breaker")
    
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Initialize score and high score
    score = 0
    high_score = load_high_score()

    # Define ball and paddle properties
    ball_radius = 10
    ball_speed_x = 5
    ball_speed_y = -5
    ball_pos = [width // 2, height // 2]

    paddle_width = 100
    paddle_height = 10
    paddle_pos = [width // 2 - paddle_width // 2, height - 20]

    # Create bricks
    brick_rows = 5
    brick_cols = 10
    brick_width = width // brick_cols
    brick_height = 30
    bricks = [[1 for _ in range(brick_cols)] for _ in range(brick_rows)]

    # Font for displaying score
    font = pygame.font.Font(None, 36)

    # Game loop
    running = True
    game_over = False
    while running:
        screen.fill(BLACK)

        if not game_over:
            # Draw bricks
            for row in range(brick_rows):
                for col in range(brick_cols):
                    if bricks[row][col] == 1:
                        pygame.draw.rect(screen, GREEN, (col * brick_width, row * brick_height, brick_width, brick_height))

            # Draw ball
            pygame.draw.circle(screen, WHITE, (ball_pos[0], ball_pos[1]), ball_radius)

            # Draw paddle
            pygame.draw.rect(screen, RED, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

            # Draw score
            score_text = font.render(f"Score: {score}", True, WHITE)
            high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(high_score_text, (10, 40))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Get key states
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
                paddle_pos[0] -= 5
            if keys[pygame.K_RIGHT] and paddle_pos[0] < width - paddle_width:
                paddle_pos[0] += 5

            # Update ball position
            ball_pos[0] += ball_speed_x
            ball_pos[1] += ball_speed_y

            # Collision detection
            if ball_pos[0] <= ball_radius or ball_pos[0] >= width - ball_radius:
                ball_speed_x = -ball_speed_x
            if ball_pos[1] <= ball_radius:
                ball_speed_y = -ball_speed_y
            if (paddle_pos[0] < ball_pos[0] < paddle_pos[0] + paddle_width) and (paddle_pos[1] < ball_pos[1] + ball_radius < paddle_pos[1] + paddle_height):
                ball_speed_y = -ball_speed_y

            # Collision with bricks
            for row in range(brick_rows):
                for col in range(brick_cols):
                    if bricks[row][col] == 1:
                        brick_rect = pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height)
                        if brick_rect.collidepoint(ball_pos[0], ball_pos[1]):
                            bricks[row][col] = 0  # Remove brick
                            ball_speed_y = -ball_speed_y
                            score += 1  # Increase score

            # Check for game over
            if ball_pos[1] > height:
                if score > high_score:
                    high_score = score  # Update high score if current score is greater
                    save_high_score(high_score)  # Save new high score
                game_over = True  # End game

        else:
            # Game Over Screen
            game_over_text = font.render("Game Over", True, WHITE)
            restart_text = font.render("Press R to Restart", True, WHITE)
            menu_text = font.render("Press Q to QUIT!", True, WHITE)

            screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 50))
            screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2))
            screen.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 + 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        run_game(screen_size)  # Restart the game
                    if event.key == pygame.K_q:
                        running = False  

        # Refresh screen
        pygame.display.flip()
        pygame.time.delay(10)

    pygame.quit()

def load_high_score():
    """Load high score from a file."""
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as file:
            return int(file.read().strip())
    return 0

def save_high_score(high_score):
    """Save high score to a file."""
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))
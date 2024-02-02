import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Define choices
choices = ['rock', 'paper', 'scissors']

# Function to determine winner
def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and opponent_choice == "scissors") or \
         (user_choice == "paper" and opponent_choice == "rock") or \
         (user_choice == "scissors" and opponent_choice == "paper"):
        return "You win! Opponent chose " + opponent_choice
    else:
        return "You lose! Opponent chose " + opponent_choice

# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if rock_rect.collidepoint(x, y):
                    user_choice = 'rock'
                elif paper_rect.collidepoint(x, y):
                    user_choice = 'paper'
                elif scissors_rect.collidepoint(x, y):
                    user_choice = 'scissors'
                else:
                    continue

                opponent_choice = random.choice(choices)
                result = determine_winner(user_choice, opponent_choice)
                print(result)

        screen.fill(BLACK)

        # Draw buttons
        rock_rect = pygame.draw.rect(screen, WHITE, (50, 150, 100, 50))
        paper_rect = pygame.draw.rect(screen, WHITE, (250, 150, 100, 50))
        scissors_rect = pygame.draw.rect(screen, WHITE, (450, 150, 100, 50))

        # Draw text on buttons
        rock_text = font.render('Rock', True, BLACK)
        paper_text = font.render('Paper', True, BLACK)
        scissors_text = font.render('Scissors', True, BLACK)
        screen.blit(rock_text, (rock_rect.centerx - rock_text.get_width() / 2, rock_rect.centery - rock_text.get_height() / 2))
        screen.blit(paper_text, (paper_rect.centerx - paper_text.get_width() / 2, paper_rect.centery - paper_text.get_height() / 2))
        screen.blit(scissors_text, (scissors_rect.centerx - scissors_text.get_width() / 2, scissors_rect.centery - scissors_text.get_height() / 2))

        pygame.display.flip()

if __name__ == "__main__":
    main()

import sys

import pygame


def run_game():
    # Initialize game and create a screemn obj.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Make the most recently dawn screen visible.
        pygame.display.flip()

run_game()
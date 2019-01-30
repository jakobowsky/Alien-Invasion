import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    ''' A class to represent a single alien in the fleet. '''

    def __init__(self, ai_settings, screen):
        ''' Initialize the alien and set its starting pos '''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien img and set its rect attr.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien' s exact position
        self.x = float(self.rect.x)

    def blitme(self):
        ''' Draw the alien at its current location '''
        self.screen.blit(self.image, self.rect)
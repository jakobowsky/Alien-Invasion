import pygame.font


class Scoreboard():
    ''' A class to report scoring info '''

    def __init__(self, ai_settings, screen, stats):
        ''' initialize scorekeepign attrs'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
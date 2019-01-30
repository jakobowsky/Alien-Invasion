class GameStats():
    ''' Track statistics for alien invasion '''

    def __init__(self, ai_settings):
        ''' Initialize statistics '''
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        ''' Initialize staatistics than can change during the game '''
        self.ship_left = self.ai_settings.ship_limit
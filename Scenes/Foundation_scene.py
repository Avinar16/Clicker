import pygame
from Scenes.Base_scene import Base_scene
from Classes.draw_text import draw_text
from Config import Config

# Foundation includes score managment
class Foundation_scene(Base_scene):
    def __init__(self, screen):
        self.screen = screen
        self.this_confing = Config()
        super().__init__(screen)

    def render(self):
        # Background init
        background = pygame.image.load("Scenes\Background\sfoundation_background1.png").convert_alpha()
        self.screen.blit(background, (0, 0))

        # Read coins from file, blit on screen
        self.coins = int(self.this_confing.getValue('coins'))
        draw_text(self.screen, str(self.coins), 64, 100, 100)
        # Base_scene render
        super().render('found_shop')

    def add_coin(self):
        if self.is_click_enabled:
            self.coins += 1
            # Writing score to file
            self.this_confing.setValue('coins', str(self.coins))

    # annul score (for tests)
    def cleanup(self):
        self.this_confing.setValue('coins', 0)
        print('Destroyed')

import pygame
from Scenes.Base_scene import Base_scene
from Classes.draw_text import draw_text
from Config import Config
from Classes.AssetManager import assetManager


# Foundation includes score managment
class Foundation_scene(Base_scene):
    def __init__(self, screen):
        self.screen = screen
        self.this_confing = Config()
        self.coins = float(self.this_confing.getValue('coins'))
        super().__init__(screen)

    def render(self):
        # Background init
        background = assetManager.load_image("sfoundation_background1.png")
        self.screen.blit(background, (0, 0))
        # Read coins from file and blit on screen
        draw_text(self.screen, str(self.coins), 64, 100, 100)
        # Base_scene render
        super().render('found_shop')

    def add_coin(self):
        if self.is_click_enabled:
            self.coins += 1
            # Writing score to file
            self.this_confing.setValue('coins', str(self.coins))

    def add_coin_per_sec(self, ):
        pps = float(self.this_confing.getValue('pps'))
        self.coins += pps
        self.coins = round(self.coins, 1)
        self.this_confing.setValue('coins', str(self.coins))

    def check_pps_and_add_new(self):
        pps = float(self.this_confing.getValue(('pts')))

        pass


    # annul score (for tests)
    def cleanup(self):
        self.this_confing.setValue('coins', 0)
        print('Destroyed')

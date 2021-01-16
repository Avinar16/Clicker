import pygame
from Scenes.Base_scene import Base_scene
from Classes.draw_text import draw_text
from Config import config
from Classes.AssetManager import assetManager
from Classes.numbers_to_text import numbers_to_text


# Foundation includes score managment
class Foundation_scene(Base_scene):
    def __init__(self, screen):
        self.screen = screen
        super().__init__(screen)

    def render(self):
        # Background init
        background = assetManager.load_image("sfoundation_background1.png")
        self.screen.blit(background, (0, 0))

        frame = assetManager.load_image('ramka.png')
        self.screen.blit(frame, (540, 80))
        frame = pygame.transform.scale(frame, (350, 78))

        self.screen.blit(frame, (540, 300))
        cps = config.getValue('pps')
        draw_text(self.screen, f'{cps}$/per sec', 30, 715, 320, font=True)

        self.screen.blit(frame, (953, 300))
        click_power = config.getValue('damage')
        draw_text(self.screen, f'{click_power}$/per click', 30, 1130, 320, font=True)

        # Read coins from file and blit on screen
        self.money = int(config.getValue('coins'))
        draw_text(self.screen, f'{numbers_to_text(self.money)}$', 64, 915, 115, font=True)
        # Base_scene render
        super().render('found_shop')

    def add_coin(self):
        if self.is_click_enabled:
            self.money += int(config.getValue('damage'))
            # Writing score to file
            config.setValue('coins', str(self.money))

    # annul score (for tests)
    def cleanup(self):
        config.load_backup()


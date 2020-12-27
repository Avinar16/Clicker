import pygame
from Classes.Button import Buttons


class Shop:
    def __init__(self, shop):
        self.buttons = Buttons(1920, 1080)
        SHOP = {'foundation': 'Scenes\Background\sfoundation_background1.png',
                'fight': 'Scenes\Background\sfoundation_background1.png'}
        self.shop_file = SHOP[shop]

    def render(self):
        # shop image init
        self.shop = pygame.image.load(self.shop_file).convert_alpha()
        self.screen.blit(self.shop, (540, 1))
        # Turn off clicking for coins or attacks

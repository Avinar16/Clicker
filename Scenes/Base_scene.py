import pygame
from Classes.Button import Buttons
from Classes.AssetManager import assetManager


class Base_scene():
    def __init__(self, screen):
        self.screen = screen

        self.shop = False

        self.shop_is_opened = False

        self.STATES = ['closed', 'opened']
        self.state = self.STATES[0]

        self.is_click_enabled = True

        self.buttons = Buttons(1920, 1080)

    # Base class render
    def render(self, shop_filename):
        # Positions for colliders
        self.pos = pygame.mouse.get_pos()
        # clicks positiob
        self.pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        self.shop_render(shop_filename)

    def check_buying(self):
        x = 1200
        y = 185
        for i in range(8):
            coords = (x, y)
            buy_button = assetManager.load_image(f"UI\Shop\Buy_button.png")
            if i == 0:
                self.screen.blit(buy_button, coords)
            else:
                y += 55
            buy_button_rect = buy_button.get_rect()
            buy_button_rect = buy_button.move(coords)
            if buy_button_rect.collidepoint(self.pos) and self.pressed1:
                return False
            return True

    def button_render(self, image):
        pass

    def check_closing(self):
        cords = (1100, 100)
        # Button image init
        self.buttons.generate('close_button', start_x=1100, start_y=100)


    def set_shop_opened(self, state):
        self.shop_is_opened = state

    def get_shop_opened(self):
        return self.shop_is_opened

    def shop_render(self, filename):
        if self.shop_is_opened:
            # shop image init
            self.shop = assetManager.load_image(f"UI\{filename}.png")
            self.screen.blit(self.shop, (540, 1))

            # Turn off clicking for coins or attacks
            self.is_click_enabled = False
        else:
            self.is_click_enabled = True

import pygame


class Base_scene():
    def __init__(self, screen):
        self.screen = screen

        self.shop_is_opened = False

        self.is_click_enabled = True

    # Base class render
    def render(self, shop_filename):
        # Positions for colliders
        self.pos = pygame.mouse.get_pos()
        self.pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        # filename for shop image
        self.shop_filename = shop_filename

        # Shop logic
        if self.shop_is_opened:
            # shop image init
            self.shop = pygame.image.load(f"UI\{self.shop_filename}.png").convert_alpha()
            self.screen.blit(self.shop, (540, 1))
            # method that checks is closeing button clicked
            self.shop_is_opened = self.check_closing()

            # Turn off clicking for coins or attacks
            self.is_click_enabled = False
        else:
            self.is_click_enabled = True

    def check_buying(self):
        x = 1200
        y = 185
        for i in range(8):
            coords = (x, y)
            buy_button = pygame.image.load(f"UI\Buy_button.png").convert_alpha()
            if i == 0:
                self.screen.blit(buy_button, coords)
            else:
                y += 55
            buy_button_rect = buy_button.get_rect()
            buy_button_rect = buy_button.move(coords)
            if buy_button_rect.collidepoint(self.pos) and self.pressed1:
                return False
            return True


    def check_closing(self):
        cords = (1100, 100)
        # Button image init
        close_button = pygame.image.load(f"UI\close_button.png").convert_alpha()
        self.screen.blit(close_button, cords)
        # Button rect for collision init
        close_button_rect = close_button.get_rect()
        close_button_rect = close_button_rect.move(cords)
        # Check if pressed
        if close_button_rect.collidepoint(self.pos) and self.pressed1:
            return False
        return True

    def set_shop_opened(self, state):
        self.shop_is_opened = state


    def get_shop_opened(self):
        return self.shop_is_opened

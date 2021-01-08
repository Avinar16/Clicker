import pygame
from math import ceil
from Classes.AssetManager import assetManager
from Classes.Button import Buttons
from Classes.draw_text import draw_text
from Config import config
from Classes.numbers_to_text import numbers_to_text


class Base_scene():
    def __init__(self, screen):
        self.screen = screen

        self.shop_is_opened = False

        self.is_click_enabled = True
        # init sprite  group for shop buttons
        self.buttons = Buttons(1920, 1080)
        self.money = int(config.getValue('coins'))

    # Base class render
    def render(self, shop_filename):
        # Positions for colliders
        self.mouse_pos = pygame.mouse.get_pos()
        # clicks position
        self.pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        self.money = int(config.getValue('coins'))
        self.shop_render(shop_filename)

    def check_buying(self):
        config_id = 0
        self.money = int(config.getValue('coins'))
        for button in self.buttons:
            if button.get_button_name() == 'Buy_button':
                if button.rect.collidepoint(self.mouse_pos) and self.pressed1 and self.able_to_buy:
                    self.able_to_buy = False
                    print(self.money)
                    bonus_config = list(map(lambda x: int(x),
                                            config.getValue(self.shop_type, config_id).split(' ')))

                    if self.money >= bonus_config[1] and self.shop_type == 'bonus_fond':
                        self.money -= bonus_config[1]
                        bonus_config[2] += 1
                        bonus_config[1] = ceil(bonus_config[1] * 1.3)
                        curent_pps = int(config.getValue('pps'))
                        config.setValue('pps', curent_pps + bonus_config[0])
                        config.setValue(self.shop_type, ' '.join(map(str, bonus_config)), index=config_id)
                    elif self.money >= bonus_config[1] and self.shop_type == 'bonus_fight' and bonus_config[2] < 1:
                        self.money -= bonus_config[1]
                        bonus_config[2] += 1
                        curent_damage = int(config.getValue('damage'))
                        config.setValue('damage', curent_damage + bonus_config[0])
                        config.setValue(self.shop_type, ' '.join(map(str, bonus_config)), index=config_id)
                    print(self.money)
                    config.setValue('coins', self.money)
                    print(config.getValue('coins'))
                config_id += 1

    def add_coin_per_sec(self):
        pps = int(config.getValue('pps'))
        money = pps + int(config.getValue('coins'))
        config.setValue('coins', str(money))

    def text_render(self, scene, startx=0, starty=0, offset=0):
        x = startx
        y = starty
        # set name for interactions with config
        if scene == 'found_shop':
            self.shop_type = 'bonus_fond'
        else:
            self.shop_type = 'bonus_fight'
        for i in range(4):
            # load info from config
            power, price, ammount = config.getValue(self.shop_type, i).split(' ')

            # draw config info in shop
            draw_text(self.screen, f'{price}$', 40, x, y, True)
            draw_text(self.screen, f'{ammount}', 30, x, y + 50, True)
            y += offset
        coins = config.getValue('coins')
        draw_text(self.screen, f'{numbers_to_text(coins)}$', 40, 700, 130, True)

    def button_render(self):
        # Render shop buttons
        self.buttons.empty()
        self.buttons.generate('close_button', start_x=1100, start_y=100)
        self.buttons.generate('Buy_button', count=4, offset_y=150, start_x=1218, start_y=250)
        self.buttons.draw(self.screen)

    def check_closing(self):
        # If button is close_button and clicked -> close the shop
        for button in self.buttons:
            if button.get_button_name() == 'close_button':
                if button.rect.collidepoint(self.mouse_pos) and self.pressed1:
                    self.shop_is_opened = False

    def set_shop_opened(self, state):
        self.shop_is_opened = state

    def get_shop_opened(self):
        return self.shop_is_opened

    def set_buy_click(self, state):
        self.able_to_buy = state

    def shop_render(self, filename):
        if self.shop_is_opened:
            # shop image init
            self.shop = assetManager.load_image(f"UI\{filename}.png")
            self.screen.blit(self.shop, (540, 1))
            self.button_render()
            self.text_render(filename, 1050, 220, 160)

            self.check_buying()
            self.check_closing()
            # Turn off clicking for coins or attacks
            self.is_click_enabled = False
        else:
            self.is_click_enabled = True

    def set_mouse_pos(self, pos):
        self.mouse_pos = pos

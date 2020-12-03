from Classes.draw_text import draw_text
from Scenes.Fight_scene import Fight_scene
from Scenes.Foundation_scene import Foundation_scene
import pygame


class Scene_manager():
    def __init__(self, screen):
        # Main screen
        self.screen = screen

        # Id for scenes
        self.scene_id = 0

        # tuple of avaliable scenes
        self.scenes = (Foundation_scene(self.screen), Fight_scene(self.screen))

        # setting start scene
        self.scenes[self.scene_id].render()

    # Setting scene interactions with mouse
    def on_click(self, event_pos):
        # Change scene_id if button clicked
        mouse_x, mouse_y = event_pos
        if 960 > mouse_x >= 460 and mouse_y >= 930:
            self.scene_id = 0
        elif 1420 > mouse_x >= 960 and mouse_y >= 930:
            self.scene_id = 1
        # Open shop
        elif mouse_x >= 0 and mouse_y >= 930:
            print(self.scenes[self.scene_id].get_shop_opened())
            if self.scenes[self.scene_id].get_shop_opened():
                self.scenes[self.scene_id].set_shop_opened(False)
            else:
                self.scenes[self.scene_id].set_shop_opened(True)

    def render(self):
        # Render current scene
        self.scenes[self.scene_id].render()

        # switch mode button
        Mode_switch = pygame.image.load("UI\game_switch.png").convert_alpha()
        self.screen.blit(Mode_switch, (460, 930))
        # shop open button
        shop_button = pygame.image.load("UI\shop_button.png").convert_alpha()
        self.screen.blit(shop_button, (0, 930))

    def get_foundation(self):
        return self.scenes[0]

    def get_fight(self):
        return self.scenes[1]

    def get_current_scene_id(self):
        return self.scene_id

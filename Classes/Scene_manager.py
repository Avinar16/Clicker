from Scenes.Fight_scene import Fight_scene
from Scenes.Foundation_scene import Foundation_scene
from Classes.AssetManager import assetManager


class Scene_manager():
    def __init__(self, screen):
        # Main screen
        self.screen = screen

        # Id for scenes
        self.scene_id = 1

        # tuple of avaliable scenes
        self.scenes = (Foundation_scene(self.screen), Fight_scene(self.screen))

        # setting start scene
        self.scenes[self.scene_id].render()

    # Setting scene interactions with mouse
    def on_click(self, event_pos):
        # Change scene_id if button clicked
        mouse_x, mouse_y = event_pos
        if 960 > mouse_x >= 460 and mouse_y >= 930:
            self.scenes[self.scene_id].set_shop_opened(False)
            self.scene_id = 0
        elif 1420 > mouse_x >= 960 and mouse_y >= 930:
            self.scenes[self.scene_id].set_shop_opened(False)
            self.scene_id = 1

        # Open shop
        elif mouse_x >= 0 and mouse_y >= 930:
            if self.scenes[self.scene_id].get_shop_opened():
                self.scenes[self.scene_id].set_shop_opened(False)
            else:
                self.scenes[self.scene_id].set_shop_opened(True)

        elif 1750 > mouse_x >= 1250 and 850 > mouse_y >= 100:
            if self.scene_id == 1:
                self.scenes[self.scene_id].add_hits()

        elif 1313 > mouse_x >= 550 and 856 > mouse_y >= 700:
            if self.scene_id == 1:
                self.scenes[self.scene_id].activate_timer()

    def render(self, mouse_point):
        # Render current scene
        self.scenes[self.scene_id].render()
        self.scenes[self.scene_id].set_mouse_pos(mouse_point)

        # switch mode button
        Mode_switch = assetManager.load_image("UI\game_switch.png").convert_alpha()
        self.screen.blit(Mode_switch, (460, 930))
        # shop open button
        shop_button = assetManager.load_image("UI\shop_button.png").convert_alpha()
        self.screen.blit(shop_button, (0, 930))

    def get_foundation(self):
        return self.scenes[0]

    def get_fight(self):
        return self.scenes[1]

    def get_current_scene_id(self):
        return self.scene_id

    def set_click_for_buy(self, state):
        self.scenes[self.scene_id].set_buy_click(state)

    def render_coins_persec(self):
        self.scenes[self.scene_id].add_coin_per_sec()


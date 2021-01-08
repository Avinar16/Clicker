import pygame
from Classes.AssetManager import assetManager


class Buttons(pygame.sprite.Group):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def generate(self, image, count=1, offset_x=0, offset_y=0, start_x=0, start_y=0):
        self.image = assetManager.load_image(f"{image}.png")
        x = start_x
        y = start_y
        self.index = 0
        for _ in range(count):
            Button(x, y, image, self.index, self)
            self.index += 1
            x += offset_x
            y += offset_y

    def on_click(self, pos, button=None):
        for sprite in self.sprites():
            if sprite.rect.collidepoint(pos):
                pass


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, index, *groups):
        super().__init__(groups)
        self.path = image
        self.button_name = self.path.split('\\')
        self.button_name.append(index)
        self.image = assetManager.load_image(f"{self.path}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = assetManager.load_image(f"{self.path}.png")

    def get_button_name(self):
        return self.button_name[0]

    def get_button_index(self):
        return self.button_name[1]

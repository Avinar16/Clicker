import pygame
from Classes.Button import Button
from Classes.draw_text import draw_text


class Fight_scene:
    def __init__(self, screen, coords):
        fone = pygame.image.load("Scenes\Background\Back.png").convert_alpha()
        Hero_JoJo = pygame.image.load("Heros\Jonatan.jpg").convert_alpha()
        screen.blit(fone, (0, 0))
        screen.blit(Hero_JoJo, (100, 50))
        Color_green = (206, 255, 0)
        text_color = (0, 0, 0)
        draw_text(fone, 'Score!:', 100, 1200, 100)
        attack_button = pygame.Rect(1200, 870, 250, 100)
        click_button = pygame.Rect(200, 870, 250, 100)
        pygame.draw.rect(screen, [26, 240, 150], click_button)
        pygame.draw.rect(screen, [0, 0, 0], attack_button)
      #  self.jump_button = Button.create_button(self, fone, Color_green, 1800, 50, 150, 50, 1, 'К Вагону', text_color)
      #  screen.blit(self.jump_button, 1350, 50)
        # draw_text(fone, str(score), 100, 1350, 100)

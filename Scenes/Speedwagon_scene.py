import pygame

class Speedwagon_scene:
    def __init__(self, screen, coords):
        jump_button = pygame.Surface((100, 50))
        jump_button.fill([206, 255, 0])
        screen.blit(jump_button, coords)


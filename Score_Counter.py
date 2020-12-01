import pygame

class Score_Counter:
    def __init__(self, screen, cords):
        Score_surfase = pygame.Surface((200, 200))
        Score_surfase.fill([255, 255, 255])
        screen.blit(Score_surfase, cords)



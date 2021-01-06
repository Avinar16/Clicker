import pygame


def draw_text(surf, text, size, x, y, font=False):
    WHITE = (255, 255, 255)
    if not font:
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
    else:
        font = pygame.font.Font("20008.ttf", size)

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
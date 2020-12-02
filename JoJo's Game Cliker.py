import pygame
from Init import Init

pygame.init()
size = [1920, 980]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
sound = pygame.mixer.Sound('Music\Main Theme maybe.wav')
sound.set_volume(0.01)
pygame.display.set_caption("JoJo's Cliker")

score = 0


# surf - поверхность на которой пишем
# text - то что пишем (genius)
# x, y - логично будет понять что это координаты, чекай последнее слово предыдущей строки
def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    WHITE = (255, 255, 255)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            score += 1
        sound.play()
    screen.fill((200, 100, 0))
    # Уже хз на что два след коммента но пусть будут
    # draw_text(click_button, "Click!", 20, 10, 10)
    # text = font_name.render(str(score), True, (255, 255, 255))
    # Тот самый
    init = Init(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

import pygame

pygame.init()
size = [1920, 980]

WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fone = pygame.image.load("Fons\Back.png").convert_alpha()
Jonatan = pygame.image.load("Heros\Jonatan.jpg").convert_alpha()
sound = pygame.mixer.Sound('Music\Main Theme maybe.wav')
sound.set_volume(0.01)
pygame.display.set_caption("JoJo's Cliker")
attack_button = pygame.Rect(1200, 870, 250, 100)
click_button = pygame.Rect(200, 870, 250, 100)
score = 0
font_name = pygame.font.match_font('arial')


# surf - поверхность на которой пишем
# text - то что пишем (genius)
# x, y - логично будет понять что это координаты, чекай последнее слово предыдущей строки
def draw_text(surf, text, size, x, y):  # Выводим текст что тут может быть не понятного, когда там уже чайник вскипит
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    # blit почему то не работает спросил у препода, жду...
    # Кофе кста вкусный


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            score += 1
        sound.play()
    screen.fill((200, 100, 0))
    screen.blit(fone, (0, 0))
    screen.blit(Jonatan, (100, 50))
    pygame.draw.rect(screen, [26, 240, 150], click_button)
    # draw_text(click_button, "Click!", 20, 10, 10)
    # text = font_name.render(str(score), True, (255, 255, 255))
    draw_text(fone, 'Score!:', 100, 1200, 100)
    draw_text(fone, str(score), 100, 1350, 100)
    pygame.draw.rect(screen, [0, 0, 0], attack_button)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

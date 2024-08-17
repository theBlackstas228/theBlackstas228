import pygame
pygame.init()
player1 = pygame.Rect(100, 100, 50 , 50)
window = pygame.display.set_mode((500,500))
back_color = (0,255,200)

game = True
clock = pygame.time.Clock()
while game:
    pygame.display.update()
    clock.tick(24)
    window.fill(back_color)
    pygame.draw.rect(window, (0,0,0), player1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_d] and player1.x < 450:
        player1.x += 3
    if keys [pygame.K_a] and player1.x > 0:
        player1.x -= 3
    if keys [pygame.K_s] and player1.y < 450:
        player1.y += 3
    if keys [pygame.K_w] and player1.y > 0:
        player1.y -= 3
    

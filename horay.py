import pygame
pygame.init()
import random
font = pygame.font.Font(None, 20)
text = font.render("click me!!", True,(220,0,0))
players = [pygame.Rect(75, 100, 80, 250),
pygame.Rect(175, 100, 80,250), 
pygame.Rect(275, 100, 80,250),
pygame.Rect(375, 100, 80,250)]

text_on_area = random.choice(players)
start_time = pygame.time.get_ticks()

score = 0

window = pygame.display.set_mode((500,500))

back_color = (255,255,0)

game = True



clock = pygame.time.Clock()
while game:
    
    window.fill(back_color)
    window.blit(text,(75,100))


    for pl in players:
        pygame.draw.rect(window, (0,0,0), pl)

    current_time = pygame.time.get_ticks()
    elapsed = current_time - start_time
    if elapsed > 1000:
        text_on_area = random.choice(players)
        start_time = pygame.time.get_ticks()
    window.blit(text,(text_on_area.x+13,text_on_area.y+100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        elif event.type == pygame.MOUSEBUTTONDOWN  and event.button == 1:
            x,y = event.pos
            if text_on_area.collidepoint(x,y):
                score += 1
                print(score)
        elif event.type == pygame.KEYDOWN:
            print(20)
   
    pygame.display.update()
    clock.tick(30)

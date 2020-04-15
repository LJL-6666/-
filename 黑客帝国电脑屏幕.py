import random
import string
import pygame

PANEL_width = 1000
PANEL_highly = 800
FONT_PX = 15

pygame.init()
winSur = pygame.display.set_mode((PANEL_width,PANEL_highly))
font = pygame.font.SysFont("msyh.tss",25)
bg_suface = pygame.Surface((PANEL_width,PANEL_highly),flags = pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0,0,0,28))
winSur.fill((0,0,0))
#texts = [font.render(str(i),True,(0,255,0)) for i in range(10)]
letter = string.ascii_lowercase
texts = [font.render(str(letter[i]),True,(0,225,0)) for i in range(26)]

column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            chang = pygame.key.get_pressed()
            if(chang[32]):
                exit()

    pygame.time.delay(30)
    winSur.blit(bg_suface,(0,0))
    for i in range(len(drops)):
        text = random.choice(texts)

        winSur.blit(text,(i*FONT_PX,drops[i]*FONT_PX))
        drops[i] += 1
        if drops[i]*10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip() 

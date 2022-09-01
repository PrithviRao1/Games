import pygame
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow=(255, 181, 0)
black=(0,0,0)
X = 800
Y = 600
fh = open('score.txt','r')
finalScoreStr = fh.read()
fh.close()
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Game Over')
font = pygame.font.Font('Gamerock.otf', 100)
font2 =  pygame.font.Font('8-BIT WONDER.TTF', 20)
text = font.render('Game Over', True, yellow, black)
text2= font2.render('Your final score was', True, white, black)
text3= font2.render(finalScoreStr, True, white, black)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect.center = (X // 2, Y // 2-150)
textRect2.center = (X // 2, Y // 2-50)
textRect3.center = (X // 2, Y // 2)
while True:
    display_surface.fill(black)
    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    display_surface.blit(text3, textRect3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import main
        pygame.display.update()
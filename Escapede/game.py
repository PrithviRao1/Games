import pygame
from menu import * #imports all classes 
from pygame import mixer

class Game():
    def __init__(self): #initializing
        pygame.init() 
        self.running, self.playing = True, False #differentiating between when game is being played and when it is idle
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  #variables to keep track of actions in menu
        self.DISPLAY_W, self.DISPLAY_H = 1000, 700  #screen size
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))  #creating canvas
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H))) #creating window
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE, self.BLUE,self.YELLOW = (0, 0, 0), (255, 255, 255), (9 ,11 ,72 ),(255, 181, 0)
        self.main_menu = MainMenu(self)
        self.credits=CreditsMenu(self)
        self.characters=Characters(self)
        self.leaderboard=Leaderboard(self)
        self.curr_menu = self.main_menu

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #to check if player closed game
                self.running, self.playing = False, False #to close the game
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN: #to check if player pressed any key
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True  #Enter=Select
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True   #Backspace=Back
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True   #down key
                if event.key == pygame.K_UP:
                    self.UP_KEY = True    #up key

    def reset_keys(self): #resetting so each operation can be repeated
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False                   
       
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
                import startscreen
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()           

    def draw_text(self, text, size, x, y ): #function for printing
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_2(self, text, size, x, y ): #function for printing
        font = pygame.font.Font("Gamerock.otf",size)
        text_surface = font.render(text, True, self.YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_4(self, text, size, x, y ): #function for printing(white)
        font = pygame.font.Font("Gamerock.otf",size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_3(self, text, size, x, y ): #function for printing (yellow)
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)



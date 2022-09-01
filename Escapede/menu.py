import pygame
from os import path

character_selected="Angry Cat   "
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20) #creating cursor of defined size
        self.offset = - 170 # offset so cursor wont overlap with text

    def draw_cursor(self): #location of cursor on screen
        self.game.draw_text_3('*', 30, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 20 # positioning start button 
        self.charactersx, self.charactersy = self.mid_w, self.mid_h + 60 #positioning characters button
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
        self.leaderboardx, self.leaderboardy = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) #cursor starting position
        

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            #Location of text on homepage
            self.game.draw_text_2('ESCAPEDE™', 120, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 150)
            self.game.draw_text("Start Game", 30, self.startx, self.starty)
            self.game.draw_text("Characters", 30, self.charactersx, self.charactersy)
            self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            self.game.draw_text("Leaderboard", 28, self.leaderboardx, self.leaderboardy)
            self.game.draw_text("Character selected", 25, self.mid_w, self.mid_h+230)
            self.game.draw_text(character_selected, 25, self.mid_w, self.mid_h+270)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.mid_w, self.mid_h+180)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.mid_w, self.mid_h-20)

            self.draw_cursor()
            self.blit_screen() #Updates the screen with all changes

    def move_cursor(self): #moving cursor based on currect location then updating the state ( position ) of cursor to match input
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.charactersx + self.offset, self.charactersy)
                self.state = 'Characters'
            elif self.state == 'Characters':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'   
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'        
            elif self.state == 'Characters':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.charactersx + self.offset, self.charactersy)
                self.state = 'Characters'

    def check_input(self):#changing state of cursor 
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing=True
            elif self.state == 'Characters':
                self.game.curr_menu = self.game.characters
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Leaderboard':
                self.game.curr_menu = self.game.leaderboard
            self.run_display = False    

class CreditsMenu(Menu):#Text displayed on page
    def __init__(self, game):
        Menu.__init__(self, game)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text_2('Credits', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('created by', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 55)
            self.game.draw_text('Swapnil', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Siddharth', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)
            self.game.draw_text('Prithvi', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 190)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.mid_w, self.mid_h )
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.mid_w, self.mid_h+240)
            self.blit_screen()

     
class Leaderboard(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def fetchScores(self):
        if path.exists("myScore.txt"):
            scoreList = [int(line.strip()) for line in open("myScore.txt", 'r')]
            scoreList.sort(reverse=True)
            scoreList = scoreList[:5]
            return scoreList
        else:
            return []
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False    
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text_2('Leaderboard', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 10)
            scoreList = self.fetchScores()
            if len(scoreList)==0:
                self.game.draw_text("No existing records", 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 55)
            else:
                self.game.draw_text("Your top scores", 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 55)
            wVar = 50
            for i in range(0,len(scoreList)):
                self.game.draw_text(str(scoreList[i]), 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + wVar)
                wVar += 50
            self.blit_screen()

class Characters(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state="Angry Cat   "
        self.char1x,self.char1y=self.mid_w-200, self.mid_h-75
        self.char2x,self.char2y=self.mid_w-200, self.mid_h+50
        self.char3x,self.char3y=self.mid_w-200, self.mid_h+175
        self.cursor_rect.midtop = (self.char1x + self.offset, self.char1y)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False   
            self.game.draw_text("Angry Cat   ", 30, self.char1x, self.char1y)
            self.game.draw_text("Yee Dinosaur", 30, self.char2x, self.char2y)
            self.game.draw_text("Stonks Man", 30, self.char3x, self.char3y)
            self.game.draw_text_2("Choose your character", 75, self.mid_w, self.mid_h-250)
            self.game.draw_text_4("-----------------------------------------------------------------------------------------------------------------------------------------",25,self.mid_w, self.mid_h-180)

            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Angry Cat   ':
                self.cursor_rect.midtop = (self.char2x + self.offset, self.char2y)
                self.state = 'Yee Dinosaur'
            elif self.state == 'Yee Dinosaur':
                self.cursor_rect.midtop = (self.char3x + self.offset, self.char3y)
                self.state = 'Stonks Man'
            elif self.state == 'Stonks Man':
                self.cursor_rect.midtop = (self.char1x + self.offset, self.char1y)
                self.state = 'Angry Cat   '
        elif self.game.UP_KEY:
            if self.state == 'Stonks Man':
                self.cursor_rect.midtop = (self.char2x + self.offset, self.char2y)
                self.state = 'Yee Dinosaur'
            elif self.state == 'Yee Dinosaur':
                self.cursor_rect.midtop = (self.char1x + self.offset, self.char1y)
                self.state = 'Angry Cat   '
            elif self.state == 'Angry Cat   ':
                self.cursor_rect.midtop = (self.char3x + self.offset, self.char3y)
                self.state = 'Stonks Man'

    def check_input(self):
        global character_selected
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Angry Cat   ':
                character_selected="Angry Cat   "
            elif self.state == 'Yee Dinosaur':
                character_selected="Yee Dinosaur"
            elif self.state == 'Stonks Man':
                character_selected="Stonks Man"
            self.run_display = False    



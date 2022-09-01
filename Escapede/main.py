from game import Game #importing the Game class 
g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
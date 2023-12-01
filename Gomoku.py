import pygame

from Chessboard import Chessboard

class Gomoku():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("GOMOKU")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.going = True
        self.firstTurn = 'b'
        self.firstTurnPassed = False

        self.chessboard = Chessboard()

    def loop(self):
        while self.going:
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.going = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    self.firstTurn = 'w' if self.firstTurn == 'b' else 'b'
                    self.firstTurnPassed = False
                    self.chessboard.reset()

            if self.firstTurnPassed == False and self.firstTurn == 'w':
                self.firstTurnPassed = True
                self.chessboard.ai_move()

            else:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.chessboard.handle_key_event(e):
                        self.chessboard.ai_move()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))

        #Render winned match for Player and for AI
        self.screen.blit(self.font.render("Player: {0}".format(self.chessboard.player_wins), True, (0, 0, 0)), (600, 40))
        self.screen.blit(self.font.render("AI: {0}".format(self.chessboard.ai_wins), True, (0, 0, 0)), (600, 70))

        self.chessboard.draw(self.screen)
        if self.chessboard.game_over:
            self.screen.blit(self.font.render("{0} Win".format("Black" if self.chessboard.winner == 'b' else "White"), True, (0, 0, 0)), (500, 10))
            #Render BUTTON NEW GAME
            self.screen.blit(self.font.render("Press RETURN", True, (0, 0, 0)), (550, 150))
            self.screen.blit(self.font.render("for a new game", True, (0, 0, 0)), (550, 180))

        pygame.display.update()


if __name__ == '__main__':
    game = Gomoku()
    game.loop()

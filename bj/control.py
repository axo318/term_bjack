from bj.game import Game
from bj.view import *


class Mode:
    """
    ABSTRACT
    """
    def __init__(self):
        self.last_input = None
        self.previousMode = None
        self.nextMode = None

    def getNextMode(self, user_input):
        self.last_input = user_input
        self.previousMode = self.__class__
        self.nextMode = self.__class__
        if user_input == 'exit':
            self.nextMode = ExitMode

    def execute(self, game, view_controller):
        pass


class ExitMode(Mode):
    def execute(self, game, view_controller):
        view_controller.update(ExitView())
        return True


class MenuMode(Mode):
    def getNextMode(self, user_input):
        super().getNextMode(user_input)
        if user_input == "play":
            self.nextMode = GameModeStart
        return self.nextMode()

    def execute(self, game, view_controller):
        view_controller.update(MenuView())


class GameMode(Mode):
    """
    ABSTRACT
    """
    def getNextMode(self, user_input):
        super().getNextMode(user_input)
        if user_input == 'menu':
            self.nextMode = MenuMode
        return self.nextMode()


class GameModeStart(GameMode):
    def getNextMode(self, user_input):
        super().getNextMode(user_input)
        return self.nextMode()

    def execute(self, game, view_controller):
        game.initialise()
        view_controller.update(GameView(len(game.players)))


class Controller:

    def __init__(self):
        self.on = True
        self.game = Game()
        self.view_controller = ViewController()
        self.mode = MenuMode()
        self.mode.execute(self.game, self.view_controller)
        self.update()

    def dealWithInput(self, user_input):
        self.mode = self.mode.getNextMode(user_input)
        sig = self.mode.execute(self.game, self.view_controller)
        if sig is not None:
            self.on = False

    def update(self):
        self.view_controller.draw()

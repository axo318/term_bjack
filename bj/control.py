from bj.game import Game
from bj.view import ViewController


class Mode:
    def deal(self, user_input, control):
        return self


class GameMode(Mode):
    pass


class ExitMode(Mode):
    pass


class IntroMode(Mode):
    def deal(self, user_input, control):
        if user_input == "play":
            control.view.body = "This is game mode!"
            control.view.user_choices = "1.Draw\n2.Pass"
            return GameMode()

        elif user_input == "exit":
            control.view.body = "Exiting bj"
            control.view.user_choices = ""
            control.on = False
            return ExitMode()

        else:
            return self


class Controller:

    def __init__(self):
        self.on = True
        self.game = Game()
        self.view = ViewController()
        self.mode = IntroMode()

        self.execute()

    def dealWithInput(self, user_input):
        self.mode = self.mode.deal(user_input, self)
        self.execute()

    def execute(self):
        self.view.draw()

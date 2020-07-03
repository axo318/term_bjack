import os

from bj.utils import clearScreen


class View:
    """
     General View class holding basic elements for the player terminal view
    """

    def __init__(self):
        self.header = None
        self.body = None
        self.user_choices = None

    def getHeader(self):
        return self.header

    def getBody(self):
        return self.body

    def getUserChoices(self):
        return self.user_choices


class BaseView(View):
    def __init__(self):
        super().__init__()
        self.header = """----------------------------\n""" + \
                      """|------- Term BJack -------|\n""" + \
                      """----------------------------\n"""


class ExitView(BaseView):
    def __init__(self):
        super().__init__()
        self.body = "Exiting game ..."
        self.user_choices = ""


class MenuView(BaseView):
    def __init__(self):
        super().__init__()
        self.body = "This is the menu body"  # IntroBody()
        self.user_choices = "Play\nExit"  # IntroUserChoices()


class GameView(BaseView):
    def __init__(self, players):
        super().__init__()
        self.body = f"This is Game Mode!\nThere are {players} players"
        self.user_choices = "1.Draw  2.Pass"


class ViewController:
    def __init__(self):
        self.view = None

    def update(self, view):
        self.view = view

    def draw(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
        clearScreen()
        print(self.view.getHeader())
        print()
        print(self.view.getBody())
        print()
        print(self.view.getUserChoices())
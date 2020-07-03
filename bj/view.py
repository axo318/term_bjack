import os


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


class IntroView(View):
    def __init__(self):
        super().__init__()
        self.header = "This is terminal black jack!"  # IntroHeader()
        self.body = "This is the intro body"  # IntroBody()
        self.user_choices = "Play\nExit"  # IntroUserChoices()


class ViewController:
    def __init__(self):
        self.view = IntroView()

    def update(self, view):
        self.view = view

    def draw(self):
        os.system('cls')
        print(self.view.getHeader())
        print(self.view.getBody())
        print(self.view.getUserChoices())

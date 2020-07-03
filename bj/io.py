class InputManager:

    def __init__(self):
        self.message = ' >>'

    def captureInput(self):
        print()
        return input(self.message)

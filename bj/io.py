class InputManager:

    def __init__(self):
        self.message = 'Type here >>'

    def captureInput(self):
        print()
        return input(self.message)

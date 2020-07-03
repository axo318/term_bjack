from bj.control import Controller
from bj.io import InputManager


def main():
    input_manager = InputManager()
    control = Controller()

    while control.on:
        u = input_manager.captureInput()
        control.dealWithInput(u)


if __name__ == "__main__":
    main()

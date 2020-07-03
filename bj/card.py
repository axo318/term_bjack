import random


class Card:
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def __eq__(self, other):
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return False

        return self.color == other.color and self.number == other.number

    def __repr__(self):
        return f"Card({self.color!r}, {self.number!r})"

    def getValue(self):
        if self.number in [2, 3, 4, 5, 6, 7]:
            return self.number
        elif self.number in [8, 9, 10]:
            return 0
        else:
            return -1


class ChooseStrategy:
    """
     Choose strategy Superclass-Subclass pattern
    """
    def chooseCard(self, state):
        pass


class StandardChooseStrategy(ChooseStrategy):
    def chooseCard(self, state):
        remaining_cards = state.remainingCards()
        ind = random.randrange(len(remaining_cards))
        return remaining_cards[ind]


class CardDeck:
    """
     Object class which saves the state and strategy for card choosing
    """
    def __init__(self, strategy: ChooseStrategy):
        self.strategy = strategy
        self.deck_state = InitialDeckState()

    def __repr__(self):
        return repr(self.deck_state.remaining_cards)

    def chooseCard(self):
        card = self.strategy.chooseCard(self.deck_state)
        self.deck_state.alter(card)
        return card



class DeckState:
    """
     Class that holds information and deals with card picking state changes
    """
    def __init__(self, cards):
        self.remaining_cards = cards

    def remainingCards(self):
        return self.remaining_cards

    def alter(self, card):
        if card in self.remaining_cards:
            self.remaining_cards.remove(card)


class InitialDeckState(DeckState):
    def __init__(self):
        cards = buildSet()
        super().__init__(cards)


def buildSet():
    """
     Function that builds the initial card deck
    :return: list[Card]
    """
    numbers = range(1, 14)

    red_cards = [Card('red', i) for i in numbers]
    blue_cards = [Card('blue', i) for i in numbers]
    green_cards = [Card('green', i) for i in numbers]
    yellow_cards = [Card('yellow', i) for i in numbers]

    deck = red_cards + blue_cards + green_cards + yellow_cards
    return deck

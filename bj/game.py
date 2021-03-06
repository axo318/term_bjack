from bj.card import Card, CardDeck, StandardChooseStrategy

INITIAL_POINTS = 0
INITIAL_SCORE = 0


class Player:
    def __init__(self, username: str):
        self.username = username
        self.points = INITIAL_POINTS
        # self.score = INITIAL_SCORE
        self.cards = []

    def __eq__(self, other):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return False
        return self.username == other.username

    def __repr__(self):
        return f"Player({self.username!r}, {self.points!r})"

    def receive(self, card: Card):
        self.cards += card
        self.points += card.getValue()
        # self.score += 1


class Dealer:
    def __init__(self):
        self.deck = CardDeck(StandardChooseStrategy())

    def hand(self, player: Player):
        card = self.deck.chooseCard()
        player.receive(card)

    def __repr__(self):
        return "Dealer's deck: " + repr(self.deck)


class Game:
    def __init__(self):
        self.dealer = None
        self.players = None
        self.current_player = None

    def initialise(self, player_num=1, player_names=None):
        if player_names is None:
            player_names = ['player' + str(i + 1) for i in range(player_num)]
        elif len(player_names) < player_num:
            player_names += ['player' + str(i + 1) for i in range(len(player_names), player_num)]

        self.dealer = Dealer()
        self.players = [Player(player_names[i]) for i in range(player_num)]
        self.current_player = self.players[0]

    def playerDraws(self):
        self.dealer.hand(self.current_player)
        self.playerPasses()

    def playerPasses(self):
        self.current_player = self._nextPlayer()

    def _nextPlayer(self):
        idx = self.players.index(self.current_player)
        next_idx = (idx + 1) % len(self.players)
        return self.players[next_idx]

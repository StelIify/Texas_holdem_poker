class GameRound:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        """Shuffles the deck and deals two initial cards for each player"""
        self.deck.shuffle()
        for player in self.players:
            player.add_cards(self.deck.deal_cards(2))

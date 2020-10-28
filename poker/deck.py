class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, cards):
        self.cards.extend(cards)
import random


class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, number_of_cards):
        """Returns a list of cards and deletes them from
        self.cards attribute"""
        cards = self.cards[:number_of_cards]
        del self.cards[:number_of_cards]
        return cards

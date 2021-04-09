import unittest

from poker import Card, Deck


class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_add_card_to_collection(self):
        deck = Deck()
        card = Card("Ace", "Clubs")
        deck.add_cards([card])
        self.assertEqual(
            deck.cards,
            [card]
        )

    def test_deck_has_length(self):
        deck = Deck()
        self.assertEqual(len(deck), 0)

    def test_remove_specified_number_of_cards_from_deck(self):
        ace = Card("Ace", "Hearts")
        king = Card("King", "Clubs")
        queen = Card("Queen", "Diamonds")
        cards = [ace, king, queen]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(deck.deal_cards(2), [ace, king])
        self.assertEqual(deck.cards, [queen])

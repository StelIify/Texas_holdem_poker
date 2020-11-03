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
        deck.add_card([card])
        self.assertEqual(
            deck.cards,
            [card]
        )

import unittest
from poker import Card, Hand


class HandTest(unittest.TestCase):
    def test_recives_and_stores_cards(self):
        cards = [
            Card("Ace", "Spades"),
            Card("King", "Hearts")
        ]

        hand = Hand(cards=cards)
        self.assertEqual(
            hand.cards,
            cards
        )

    def test_figures_out_high_card_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("7", "Hearts")
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_card(),
            "High Card"
        )

    def test_figures_out_pair_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Clubs")
        ]
        hand = Hand(cards)
        self.assertEqual(
            hand.best_card(),
            "Pair"
        )

    def test_fifures_out_two_pairs_is_best_card(self):
        card = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Clubs"),
            Card("King", "Diamonds"),
            Card("King", "Clubs"),
            Card("5", "Clubs"),
        ]

        hand = Hand(card)
        self.assertEqual(
            hand.best_card(),
            "Two Pair"
        )
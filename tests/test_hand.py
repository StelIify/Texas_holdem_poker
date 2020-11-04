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
            [Card("King", "Hearts"),
             Card("Ace", "Spades")]
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

    def test_figures_out_two_pairs_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Clubs"),
            Card("King", "Diamonds"),
            Card("King", "Clubs"),
            Card("5", "Clubs"),
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_card(),
            "Two Pair"
        )

    def test_figures_out_three_of_the_kind_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("King", "Clubs"),
            Card("5", "Clubs"),
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_card(),
            "Three of a Kind"
        )

    def test_figures_out_straight_is_best_card(self):
        cards = [
            Card("6", "Diamonds"),
            Card("7", "Hearts"),
            Card("8", "Clubs"),
            Card("9", "Spades"),
            Card("10", "Diamonds")
        ]

        hand = Hand(cards)
        self.assertEqual(
            hand.best_card(),
            "Straight"
        )

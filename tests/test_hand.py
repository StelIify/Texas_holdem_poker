import unittest
from poker import Card, Hand


class HandTest(unittest.TestCase):
    def test_recieves_and_stores_cards(self):
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

    def test_figures_out_flush_is_best_card(self):
        cards = [Card(rank = rank, suit="Hearts")
                 for rank in ["2", "5", "10", "Queen", "King"]
                 ]
        hand = Hand(cards)
        self.assertEqual(hand.best_card(), "Flush")

    def test_figures_out_full_house_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Ace", "Clubs"),
            Card("King", "Spades"),
            Card("King", "Diamonds")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.best_card(), "Full House")

    def test_figures_out_four_of_a_kind_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Ace", "Clubs"),
            Card("Ace", "Spades"),
            Card("King", "Diamonds")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.best_card(), "Four of a Kind")

    def test_figures_out_straight_flush_is_best_card(self):
        cards = [
            Card("6", "Diamonds"),
            Card("7", "Diamonds"),
            Card("8", "Diamonds"),
            Card("9", "Diamonds"),
            Card("10", "Diamonds")
        ]
        hand = Hand(cards)
        self.assertEqual(hand.best_card(), "Straight Flush")

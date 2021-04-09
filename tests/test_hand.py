import unittest
from poker import Card, Hand


class HandTest(unittest.TestCase):

    def test_hand_start_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_receives_and_stores_cards(self):
        hand = Hand()
        hand.add_cards([Card("Ace", "Spades"),
                        Card("King", "Hearts")])
        self.assertEqual(
            hand.cards,
            [Card("King", "Hearts"),
             Card("Ace", "Spades")]
        )

    def test_hand_has_technical_representation(self):
        hand = Hand()

        cards = [Card("7", "Spades"),
                 Card("Queen", "Diamonds")]
        hand.add_cards(cards)
        self.assertEqual(repr(hand),
                         "7 of Spades, Queen of Diamonds")

    def test_figures_out_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.best_rank(), "No Cards")

    def test_figures_out_high_card_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("7", "Hearts")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
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

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
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

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
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

        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_figures_out_flush_is_best_card(self):
        cards = [Card(rank=rank, suit="Hearts")
                 for rank in ["2", "5", "10", "Queen", "King"]
                 ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Flush")

    def test_figures_out_full_house_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Ace", "Clubs"),
            Card("King", "Spades"),
            Card("King", "Diamonds")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Full House")

    def test_figures_out_four_of_a_kind_is_best_card(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Ace", "Clubs"),
            Card("Ace", "Spades"),
            Card("King", "Diamonds")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Four of a Kind")

    def test_figures_out_straight_flush_is_best_card(self):
        cards = [
            Card("6", "Diamonds"),
            Card("7", "Diamonds"),
            Card("8", "Diamonds"),
            Card("9", "Diamonds"),
            Card("10", "Diamonds")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Straight Flush")

    def test_figures_out_royal_flush_is_best_card(self):
        cards = [
            Card("10", "Diamonds"),
            Card("Jack", "Diamonds"),
            Card("Queen", "Diamonds"),
            Card("King", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Royal Flush")

import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card("Queen", "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card("2", "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_card_representation(self):
        card = Card("Ace", "Diamonds")
        self.assertEqual(str(card), "Ace of Diamonds")

    def test_card_has_four_possible_suits(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Diamonds", "Spades", "Clubs")
        )

    def test_card_has_thirteen_possible_ranks(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")
        )

    def test_card_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Hearts")

    def test_card_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank="2", suit="Dots")

    def test_create_52_cards(self):
        cards = Card.create_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(
            cards[0],
            Card("2", "Hearts")
        )
        self.assertEqual(
            cards[-1],
            Card("Ace", "Clubs")
        )

    def test_for_object_equality(self):
        self.assertEqual(
            Card(rank="2", suit="Hearts"),
            Card(rank="2", suit="Hearts")
        )
import unittest
from unittest.mock import MagicMock
from poker import Player
from poker import Hand


class TestPlayer(unittest.TestCase):
    def test_stores_name_and_cards(self):
        hand = Hand()
        player = Player(name="Oleks", hand=hand)
        self.assertEqual(player.name, "Oleks")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        player = Player(name="Oleks", hand=mock_hand)

        player.best_hand()
        mock_hand.best_rank.assert_called()
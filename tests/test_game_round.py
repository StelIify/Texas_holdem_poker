import unittest

from poker import GameRound
from unittest.mock import MagicMock, call


class GameRoundTest(unittest.TestCase):
    def test_stores_deck_and_players(self):
        deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        gameround = GameRound(deck=deck, players=players)

        self.assertEqual(gameround.deck, deck)
        self.assertEqual(gameround.players, players)

    def test_game_play_shuffles_deck(self):
        deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock(),
        ]

        gameround = GameRound(deck=deck, players=players)

        gameround.play()

        deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_player(self):
        deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock(),
        ]

        gameround = GameRound(deck=deck, players=players)

        gameround.play()

        deck.deal_cards.assert_has_calls([
            call(2), call(2)
        ])

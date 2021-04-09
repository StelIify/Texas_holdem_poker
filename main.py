from poker import Card, Deck, Hand, Player, GameRound

deck = Deck()
deck.add_cards(Card.create_52_cards())

hand1 = Hand()
hand2 = Hand()

player1 = Player("Oleks", hand1)
player2 = Player("Lexa", hand2)

game_round = GameRound(deck, [player1, player2])
game_round.play()

print(player1.best_hand())
print(player2.best_hand())
print(player1.hand)
print(len(deck))









# def ranks_with_count(cards, count):
#     return {
#         rank: rank_count
#         for rank, rank_count in card_rank_count(cards).items()
#         if rank_count == count
#     }
#
#
# def card_rank_count(cards):
#     card_rank_count = {}
#     for card in cards:
#         card_rank_count.setdefault(card.rank, 0)
#         card_rank_count[card.rank] += 1
#     return card_rank_count
#
#
# print(ranks_with_count(cards, 2))
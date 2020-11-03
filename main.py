from poker import Card, Deck, Hand


# deck = Deck()
# cards = Card.create_52_cards()
# deck.add_card(cards)
# print(deck.cards)

cards = [Card("Ace", "Diamonds"),
            Card("Ace", "Clubs"),
            Card("King", "Diamonds"),
            Card("King", "Clubs"),
            Card("5", "Clubs")]
hand = Hand(cards)
print(hand.best_card())



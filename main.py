from poker import Card, Deck, Hand


# deck = Deck()
# cards = Card.create_52_cards()
# deck.add_card(cards)
# print(deck.cards)

cards = [Card("6", "Diamonds"),
            Card("7", "Diamonds"),
            Card("8", "Diamonds"),
            Card("9", "Diamonds"),
            Card("10", "Diamonds")
          ]
hand = Hand(cards)
print(hand.best_card())



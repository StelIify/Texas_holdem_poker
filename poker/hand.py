class Hand():
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    @property
    def _rank_validation_from_best_to_worst(self):
        return (
            ("Royal Flush", self._is_royal_flush()),
            ("Straight Flush", self._is_straight_flush()),
            ("Four of a Kind", self._is_four_of_a_kind()),
            ("Full House", self._is_full_house()),
            ("Flush", self._is_flush()),
            ("Straight", self._is_straight()),
            ("Three of a Kind", self._is_three_of_a_kind()),
            ("Two Pair", self._is_two_pair()),
            ("Pair", self._is_pair()),
            ("High Card", self._is_high_card()),
            ("No Cards", self._no_cards())
        )

    def best_rank(self):
        for rank in self._rank_validation_from_best_to_worst:
            name, validate_func = rank
            if validate_func:
                return name

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def _is_royal_flush(self):
        is_straight_flush = self._is_straight_flush()
        if not is_straight_flush:
            return False

        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        four_of_a_kind = self._ranks_with_count(4)
        return len(four_of_a_kind) == 1

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        suit_count_dic = {
            suit: suit_count
            for suit, suit_count in self._card_suit_count.items()
            if suit_count >= 5
        }
        return len(suit_count_dic) == 1

    def _is_straight(self):
        if len(self.cards) < 5:
            return False

        rank_indexes = [card.rank_index for card in self.cards]
        return rank_indexes == list(range(rank_indexes[0], rank_indexes[-1] + 1))

    def _is_three_of_a_kind(self):
        three_of_a_kind = self._ranks_with_count(3)
        return len(three_of_a_kind) == 1

    def _is_two_pair(self):
        rank_with_pairs = self._ranks_with_count(2)
        return len(rank_with_pairs) == 2

    def _is_pair(self):
        rank_with_pairs = self._ranks_with_count(2)
        return len(rank_with_pairs) == 1

    def _is_high_card(self):
        return len(self.cards) >= 2

    def _no_cards(self):
        return len(self.cards) == 0

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_count.items()
            if rank_count == count
        }

    @property
    def _card_rank_count(self):
        card_rank_count = {}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        return card_rank_count

    @property
    def _card_suit_count(self):
        card_suit_count = {}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] += 1
        return card_suit_count

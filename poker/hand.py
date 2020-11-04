class Hand():
    def __init__(self, cards):
        copy = cards[:]
        copy.sort()
        self.cards = copy

    @property
    def _rank_validation_from_best_to_worst(self):
        return (
            ("Straight", self._is_straight()),
            ("Three of a Kind", self._is_three_of_a_kind()),
            ("Two Pair", self._is_two_pair()),
            ("Pair", self._is_pair()),
            ("High Card", self._is_high_card())
        )

    def best_card(self):
        for rank in self._rank_validation_from_best_to_worst:
            name, validate_func = rank
            if validate_func:
                return name

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
        return True

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

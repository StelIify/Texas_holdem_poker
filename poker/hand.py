class Hand():
    def __init__(self, cards):
        self.cards = cards

    @property
    def _card_rank_count(self):
        card_rank_count = {}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        return card_rank_count

    def best_card(self):
        rank_with_pairs = {
            rank: rank_count
            for rank, rank_count in self._card_rank_count.items()
            if rank_count == 2
        }

        if len(rank_with_pairs) == 2:
            return "Two Pair"
        elif len(rank_with_pairs) == 1:
            return "Pair"
        else:
            return "High Card"

    # @staticmethod
    # def count_rank_occurrence(cards):
    #     counts = {}
    #     for card in cards:
    #         if card.rank in counts:
    #             counts[card] += 1
    #         else:
    #             counts[card] = 1
    #     return counts

class Card:
    SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Your value is '{rank}'. Rank must be one of the following {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Your value is '{suit}'. It must be one of the following {self.SUITS}")
        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank_index < other.rank_index

    @classmethod
    def create_52_cards(cls):

        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

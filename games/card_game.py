import random


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return '(%s, %s)' % (self.suit, self.rank)


class CardDeck(object):
    """
      Initializes a Deck object with 52 Cards
      Card Ranking Map
      Suit Ranking Map
    """

    def __init__(self):
        # Ace's Rank is 14, King 13 and so on
        self.ranks = range(2, 15)
        self.suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        self.deck = []
        self.rank_map = {11: 'Jack', 12: 'Queen', 13: ' King', 14: 'Ace'}
        self.suit_map = {'Clubs': 4, 'Hearts': 3, 'Diamonds': 2, 'Spades': 1}

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def draw(self):
        return self.deck.pop(0)

    def sort(self):
        return sorted(self.deck, key=lambda card: self.calculate_card_rank(card))

    def calculate_card_rank(self, card):
        return card.rank * self.suit_map.get(card.suit, 0)


class CardGame(object):
    """
      Initializes a CardGame with Players and Turns

      Args
      players : No. of players in the game
      turns : No. of turns for each player
    """

    def __init__(self, players=2, turns=3):
        self.players = players
        self.turns = turns
        self.deck = CardDeck()
        self.players_cards_hist = {}
        self.winning_player = None
        self.score = {}

        if players * turns > 52:
            raise ValueError
        for player in range(0, self.players):
            self.players_cards_hist[player] = []
            self.score[player] = 0

    """
      Shuffles cards in deck. Initializes Players with drawn cards.
    """

    def start(self):
        self.deck.shuffle()
        for i in range(0, self.turns):
            for player in self.players_cards_hist:
                curr_cards_for_player = self.players_cards_hist.get(player, [])
                if len(curr_cards_for_player) >= self.turns:
                    break
                curr_cards_for_player.append(self.deck.draw())
                self.players_cards_hist.update({player: curr_cards_for_player})

    """
      Computes card ranks for all Players based on cards drawn to determine the winner
    """

    def find_winner(self):
        max_score = 0
        for player, cards in self.players_cards_hist.items():
            curr_score = 0
            curr_score = sum(self.deck.calculate_card_rank(card) for card in cards)
            if curr_score > max_score:
                self.winning_player = player
            max_score = max(curr_score, max_score)
            self.score[player] = curr_score
        return self.winning_player


def main():
    # deck = Deck()
    play = CardGame(15, 3)
    play.start()
    print('Player ' + str(play.find_winner()) + ' Won !!')


if __name__ == "__main__":
    main()

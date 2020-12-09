import unittest
from games.card_game import CardGame, CardDeck, Card


class MyTestCase(unittest.TestCase):

    def test_CardGameWithTwoPlayersAndThreeTurns(self):
        play = CardGame(2, 3)
        self.assertIsNone(play.find_winner())
        play.start()
        self.assertIsNotNone(play.find_winner())

    def test_CardGameWithZeroPlayersAndZeroTurns(self):
        play = CardGame(0, 0)
        play.start()
        self.assertIsNone(play.find_winner())

    def test_ShuffleDeck(self):
        card_deck = CardDeck()
        self.assertNotEqual(card_deck, card_deck.shuffle())

    def test_SortDeck(self):
        deck = CardDeck()
        highest_card = deck.sort()[-1]
        self.assertEqual((highest_card.suit, highest_card.rank), ('Clubs', 14))

    def test_CalculateRank(self):
        card_deck = CardDeck()
        highest_card = card_deck.sort()[-1]
        self.assertEqual(card_deck.calculate_card_rank(highest_card), 56)
        lowest_card = card_deck.deck[0]
        self.assertEqual(card_deck.calculate_card_rank(lowest_card), 2)


if __name__ == '__main__':
    unittest.main()

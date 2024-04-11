import random

# card suits n ranks
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# card init class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return 'Deck of ' + str(len(self.cards)) + ' cards'

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# hand cards class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
                score += 11
            elif card.rank in ['J', 'Q', 'K']:
                score += 10
            else:
                score += int(card.rank)

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

# game class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def play(self):
        self.deal_initial_cards()
        print('Player hand:', self.player_hand)
        print('Dealer showing:', self.dealer_hand.cards[0])

        while True:
            action = input('Do you want to hit or stand? ').lower()
            if action == 'hit':
                self.player_hand.add_card(self.deck.deal())
                print('Player hand:', self.player_hand)
                if self.player_hand.calculate_score() > 21:
                    print('Bust! You lose.')
                    break
            elif action == 'stand':
                while self.dealer_hand.calculate_score() < 17:
                    self.dealer_hand.add_card(self.deck.deal())
                print('Dealer hand:', self.dealer_hand)
                if self.dealer_hand.calculate_score() > 21 or self.dealer_hand.calculate_score() < self.player_hand.calculate_score():
                    print('You win!')
                elif self.dealer_hand.calculate_score() > self.player_hand.calculate_score():
                    print('You lose.')
                else:
                    print('It\'s a tie!')
                break
            else:
                print('Invalid input. Please type "hit" or "stand".')

# Main
game = Game()
game.play()
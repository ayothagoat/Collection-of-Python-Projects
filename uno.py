import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        
    def __repr__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
        for color in ['red', 'yellow', 'green', 'blue']:
            for value in range(1, 10):
                self.cards.append(Card(color, value))
            for value in ['skip', 'reverse', 'draw two']:
                self.cards.append(Card(color, value))
        for i in range(4):
            self.cards.append(Card('black', 'wild'))
            self.cards.append(Card('black', 'wild draw four'))
        random.shuffle(self.cards)
        
    def draw(self):
        return self.cards.pop()
    
class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
        self.discard_pile = []
        
    def start(self):
        # Deal 7 cards to each player
        for i in range(7):
            for player in self.players:
                player.hand.append(self.deck.draw())
        
        # Choose the first player and put the first card on the discard pile
        self.current_player = 0
        self.discard_pile.append(self.deck.draw())
        
        # Start the game loop
        while True:
            # Check if the current player has won
            if not self.players[self.current_player].hand:
                print(f"Player {self.current_player} wins!")
                break
            
            # Print the current state of the game
            print(f"Current player: {self.current_player}")
            print(f"Discard pile: {self.discard_pile[-1]}")
            for i, player in enumerate(self.players):
                print(f"Player {i} hand: {player.hand}")
            
            # Let the current player make a move
            self.players[self.current_player].make_move()
            
            # Advance to the next player
            self.current_player = (self.current_player + 1) % self.num_players

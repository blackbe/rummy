#!/usr/bin/python

#in the python standard library
import random

"""
Author: Ben Black
A simple rummy game demonstrating object oriented design principles.
"""

#Constants
FACE = [ 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King' ]
SUIT = ['Hearts', 'Clubs', 'Spades', 'Diamonds']

# Not used yet
JOKERS = { 'Little Joker': 666, 'Big Joker': 777 }
VALUES = { 'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13 }

class Card:
    # Class to describe a card

    def __init__(self, face, suit):
        """
        Constructor
        Args: 
            suit: string
            face: string
        Returns: none
        """
        self.face = face
        self.suit = suit
        
		
    def __str__(self):
        """
        1.function to display the card correctly
        Args: none
        Returns: string representation of the card
        """
        return '{0} of {1}'.format(self.face, self.suit)


class Deck:
    # Class to describe a deck

    def __init__(self):
        """
        Constructor
        Args: none
        Returns: none
        """
        # talk about optimization here
        self.deck_stack = []
        for s in SUIT:
            for f in FACE:
                self.deck_stack.append(Card(f, s))
    
    def draw_card(self):
        """ Draw a card from the top of the Deck
        Args:
        	No args
        Returns:
        	a Card Object
        """
        s = self.deck_stack[0]
        s.deck_stack.pop(0)
        return s
    
    def discard(self, discard_pile, card):
        # Discard a card from the players hand
        """
        Args:
        No args
        Returns:
        a Card Object
        """
        
        self.discard_pile = []
        self.card = card
        
        p = self.discard_pile[0]
        self.card.append(0)
        return p
        
    def shuffle(self):
        """ Shuffle the Deck, so that cards are ordered in a random order
        Args: none
        Returns: none
        """
        #shuffle algorithm goes here
        random.shuffle(self.deck_stack)

class Player:
    #Class to describe a player
    
    def __init__(self, name, deck, game_play):
		""" Class Constructor
		Args:
			name: Name of the Player - string
			deck: Reference to the Deck Object that is part of the Game
			game: Reference to the Game object that is being played now
		Returns:
			No return value
		"""
		self.hand = []
		self.name = name
		self.deck = deck
		self.game_play = game_play
        
    def deal_card(self, card, hand):

        """ Deal a card from the top of the Deck
        Args:
        	deck_stack, number_in_hand
        Returns:
        	a Card Object
        """
        try:
            self.hand.append(card)
            if len(hand) > 7:
		    raise ValueError('ERROR: Player cannot have more than 14 cards during turn')
        except ValueError as err:
		    print(err.args)
    def choose_discard(self, card):
        """
        Args: card: The player chooses to discard 
		Returns: none
		"""
		# Get the card from hand
        """card = get_object(self.hand, card)"""
        if card not in self.hand:
		    return False
        else:
		    self.hand.remove(card)
		    self.deck.discard(card)
		    return True

class Rummy:
    # Class to describe rummy game play
    
    #need to initialize
    
    """
    Defines playing rummy:
    1. hand dealt to each player - 2-4
    2. take turns drawing/improving/discard (max number of cards is 7)
    3. Need to loop until win condition is met:
        - sort the hand
        - loop through hand looking for the following:
            - check for 3 of a kind or 3 of same suit, first...if not found exit immediately to optimize
            - 4 of same suit, 3 of same suit = 00
            - 4 of same suit, run of 3       = 01
            - run of 4, 3 of same suit       = 10
            - run of 4, run of 3             = 11
    4. Variant - Jokers...if discarded skip 2 turns
    5. Variant - Scoring - add hands of losing players and keep dealing until a players hand exceeds 101
        - Ace = 1, Face cards = 10, Jokers = 25, number cards = their number value
        - the player whose hand > 101 is the loser and game ends
    """
        


    
    
    """
    Items to do:
    1. Need more tests
    2. Calculate for efficiency
    3. easy to understand
    4. use good formatting
    """

def main():

    # Create Deck
    deck = Deck()

    """Test Outputs"""
    # test all cards in the deck
    for i in deck.deck_stack:
        print i
    # test shuffle (can do conditional formatting duplicate matching in excel to check)
    print("\n\n")
    deck.shuffle()
    for i in deck.deck_stack:
        print i
    """



	# New game with 2 players
	g = Rummy(2, deck)

	# Now let the Players begin
	g.play()
	
	# Joker Logic should go here
	# deck.set_joker()
    """

if __name__ == "__main__":
    main()
   	# unit_tests()
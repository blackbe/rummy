#!/usr/bin/python

#in the python standard library
import random

"""
Author: Ben Black
A simple rummy game demonstrating object oriented design principles.

Background:
A deck of cards consists of 52 individual cards, divided into
four sets of thirteen cards. These four sets are known as suits
and are given names: spades, clubs, hearts, and diamonds.
With each set, the same set of numbered cards appears,
running from two to 10, alongside four “special” cards, the
ace, jack, queen and king, each represented by the first letter
of their name, as shown below.
A deck of cards may be used to play a large number of games,
involving a variety of rules and scoring mechanisms.

Fig 1: An example deck of cards (source: Wikipedia/Wikimedia Commons)
For this task, we shall make use of the game of rummy. This
game is typically played with between two and four players.
Each player is initially dealt seven cards from the deck, the
remaining cards forming a stock from which additional cards
may be drawn as the game progresses.
To win the game, a player must form a hand comprising of
two “melds” of cards, one of three cards, one of four, both
consisting of either of:
• a sequential run of numbers of the same suit, e.g. the
ace, two, three and four of clubs, or the seven, eight and
nine of spades.
• a collection of cards of the same face value from
differing suits, e.g. all four sixes, or three eights.
An example of a winning hand for rummy, comprising of the seven to ten of diamonds
and the aces of clubs, hearts, and spades. (source:
Wikipedia/Wikimedia Commons)

On each player’s turn, they
must draw a card either from the draw deck or by taking
the top card from the discard pile, if one is available.
The player uses this card to improve his hand, aiming to
build up a valid meld over a number of turns. To

complete his turn, the player must discard one of his
cards onto a discard pile, leaving him with exactly seven
cards in his hand.
"""

#Constants
SUIT = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
FACE_VALUES = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13 }
# JOKER = { 'J*': 777 }

class Card:
    # Class to describe a card

    def __init__(self, suit, value):
        """
        Constructor
        Args: 
            suit: string
            value: character
        Returns: none
        """
        self.suit = suit
        self.value = value
		
    def __str__(self):
        """
        1.function to display the card correctly
        Args: none
        Returns: string representation of the card
        """
        return (self.suit + self.value)


class Deck:
    # Class to describe a deck

    def __init__(self, name):
        """
        Constructor
        Args: 
            deck: number of cards in the deck - int
        Returns: none
        """
        self.cards = []  #for cards in the deck
        self.stack = []  #for the draw stack
        self.pile = []   #for the discard pile
        self.hand = []
        self.name = name
        
    def shuffle(self):
		""" Shuffle the Deck, so that cards are ordered in a random order
		Args: none
		Returns: none
		"""
		random.shuffle(self.cards)
		
    def deal_card(self, card):
        """ Deal a Card to the Player
        Args:
        	card:  The Card object provided to Player as part of the deal
        Returns:
        	No returns
        """
        try:
        	self.hand.append(card)
        	if len(self.hand) > 7:
        		raise ValueError('ERROR: Player cannot have more than 7 cards during turn')
        except ValueError as err:
        	print(err.args) 
	
    def draw_cards(self):
        """ Draw a card from the top of the Deck
        Args:
        	No args
        Returns:
        	a Card Object
        """
        s = self.stack[0]
        self.cards.pop(0)
        return s

    def discard(self):
        """ Discard a card from the players hand
        Args:
        	No args
        Returns:
        	a Card Object
        """
        p = self.pile[0]
        self.cards.append(0)
        return p
"""



Client script using classes to play rummy:
1. hand dealt to each player - 2-4
2. take turns drawing/improving/discard (max number of cards is 7)
3. win conditions
    - 4 of same suit, 3 of same suit = 00
    - 4 of same suit, run of 3       = 01
    - run of 4, 3 of same suit       = 10
    - run of 4, run of 3             = 11
4. scoring
"""


"""
Items to do:
1. Need unit tests
2. Calculate for efficiency
3. easy to understand
4. use good formatting
"""

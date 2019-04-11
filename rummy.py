#!/usr/bin/python3

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

 
#Class to describe a deck of cards


SUIT = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
FACE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']






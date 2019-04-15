# Rummy

This is a simple rummy game used to demonstrate simple object oriented design principles

## Improvements to be made
1. The standard python standard shuffle method doesn't always contain all of the cards, so need to write own algorithm for random.shuffle to contain all 52 cards in a shuffled list that would still use the random library
2. I used 2 for loops.   That is  O(N2) and so if a larger data set were to be used I'd want to find a different algorithm, but since the data set is small this should be fine.
3. I need to define the game play as I didn't get that far yet.
    
        a. hand dealt to each player - 2-4
        b. take turns drawing/improving/discard (max number of cards is 7)
        c. Need to loop until win condition is met:
    
                i. sort the hand
                ii. loop through hand looking for the following:
                    - check for 3 of a kind or 3 of same suit, first...if not found exit immediately to optimize ( would be null until a condition is met)
                    - 4 of same suit, 3 of same suit = 00
                    - 4 of same suit, run of 3       = 01
                    - run of 4, 3 of same suit       = 10
                    - run of 4, run of 3             = 11
        d. Variant - Jokers...if discarded skip 2 turns
        e. Variant - Scoring - add hands of losing players and keep dealing until a players hand exceeds 101
            - Ace = 1, Face cards = 10, Jokers = 25, number cards = their number value
            - the player whose hand > 101 is the loser and game ends
4. Additional items left to do:
    
        a. Need more tests
        b. Calculate for efficiency
        c. make sure well commented and easy to understand
        d. use good formatting
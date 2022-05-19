"""
This is a program that will simulate a game of blackjack and count cards.
In short, card counting assigns a value of 1, 0, or -1 to any card that comes
out of a "SHOE" - the object that holds the cards - in order to keep track of
the cards that have already played. These values are added to what is called the
"RUNNING COUNT". The running count gives the counter an ESTIMATE of the number
of high value cards left in the shoe. The goal of counting cards is to get to
a point where there are more 10s, face cards, and aces in the shoe left so that
they MIGHT get natural blackjack more often.
"""

import random
import classes as cards

#test_deck = Deck()
#test_deck.show()
test_shoe = cards.Shoe(2)
#test_shoe.show()

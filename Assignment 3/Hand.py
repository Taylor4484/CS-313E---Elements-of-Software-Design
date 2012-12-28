#  Files: Card.py, Deck.py, Hand.py, Poker.py
#
# Description: Hand Class, defines a hand of 5 playing cards for poker.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 9/28/12
#
# Date Last Modified: 9/28/12


import Card
from Deck import *

class Hand:
    """A hand is simply a list of 5 cards, dealt from the deck."""
    # Note that we have to pass in a Deck because we need
    # a place from which to draw the cards.

    def __init__(self, deck):
        """A hand is simply the first five cards in the deck, if there are
        five cards available. If not, return None."""

        
        hand = 5              # Number of cards in a hand (int)
        self._mysuits = [0] * 4     # a list of 4 zeros used for evaluation
        self._myranks = [0] * 13    # a list of 13 zeros used for evaluation

        #checks if there are enough cards in deck for a hand
        if len(deck) >= hand:
            
            #list to contain cards in hand
            self._cards = []

            #for each card in hand
            for cards in range(hand):

                #deal a new card
                newCard = deck.deal()
                self._cards.append(newCard)

                #Get suit and rank for each card in hand
                suit = Card.getSuit(newCard)
                rank = Card.getRank(newCard)

                #increase rank count for evaluation
                rank -= 1
                self._myranks[rank] += 1

                #increase suit count for evaluation
                if suit == "Spades":
                    self._mysuits[0] += 1
                if suit == "Diamonds":
                    self._mysuits[1] += 1
                if suit == "Hearts":
                    self._mysuits[2] += 1
                if suit == "Clubs":
                    self._mysuits[3] += 1               

        else:
            return None

        
    def __str__(self):
        """The string representation of the Hand, which is just the
        five cards."""
        result = ""
        for cards in self._cards:
            result = result + "\t   " + str(cards) + "\n"
        return result



    def hasRoyalFlush(self):
        """Return a boolean indicating whether
        the current hand contains a Royal Flush:
        A straight from a ten to an ace with all
        five cards of the same suit. In poker all
        suits are ranked equally."""
        if (5 in self._mysuits) and (self._myranks[0] == 1 ) and \
        (self._myranks[10] == 1 ) and (self._myranks[11] == 1 ) and \
        (self._myranks[12] == 1 ) and (self._myranks[13] == 1 ):
            return True
        else:
            return False


    def hasStraightFlush(self):
        """Return a boolean indicating whether
        the current hand contains a Straight Flush:
        Any straight with all five cards of the same
        suit."""
        if self.hasStraight() and self.hasFlush():
            return True
        else:
            return False
        
    def hasFourOfAKind(self):
        """Return a boolean indicating whether
        the current hand contains Four of a Kind:
        Any four cards of the same rank. If two
        players share the same Four of a Kind,
        the bigger fifth card (known as the kicker)
        decides who wins the pot."""
        #look for a 4 in rank counter
        if 4 in self._myranks:
            return True
        else:
            return False

    def hasFullHouse(self):
        """Return a boolean indicating whether
        the current hand contains a Full House:
        Any three cards of the same rank together
        with any two cards of the same rank."""
        #look for a 3 in rank counter
        if 2 and 3 in self._myranks:
            return True
        else:
            return False


    def hasFlush(self):
        """Return a boolean indicating whether
        the current hand contains a Flush:
        Any five cards of the same suit (not
        consecutive). The highest card of the
        five determines the rank of the flush."""
        #look for a 5 in suit counter
        if 5 in self._mysuits:
            return True
        else:
            return False


    def hasStraight(self):
        """Return a boolean indicating whether
        the current hand contains a straight:
        Any five consecutive cards of different
        suits. Aces can count as either a high
        or a low card."""
        counter = 0
        #loop through rank counter
        for i in self._myranks:
            #check counter for straight of 5
            if counter == 5:
                return True
            #increase counter if 1
            if i == 1:
                counter += 1
            #reset counter if not 1
            elif i == 0:
                counter = 0
            #if not 0 or 1, straight isn't possible
            else:
                return False
        #if ace, allow it as a high card    
        if self._myranks[0] == 1:
            counter += 1
        #recheck counter for straight of 5
        if counter == 5:
            return True
        #else not a straight
        else:
            return False


    def hasThreeOfAKind(self):
        """Return a boolean indicating whether
        the current hand contains Three of a Kind:
        Any three cards of the same rank."""
        #look for a 3 in rank counter
        if 3 in self._myranks:
            return True
        else:
            return False

    def hasTwoPair(self):
        """Return a boolean indicating whether
        the current hand contains two sets of pairs:
        Any two cards of the same rank together
        with another two cards of the same rank."""
        counter = 0
        #loop through rank counter
        for i in self._myranks:
            #if 2, pair found, increase counter
            if i == 2:
                counter +=1
        #is this 2 or more pairs?
        if counter >=2:
            return True
        else:
            return False
        
    def hasPair(self):
        """Return a boolean indicating whether
        the current hand contains a pair:
        Any two cards of the same rank together
        with another two cards of the same rank."""
        #look for 2 in rank counter, indicates pair
        if 2 in self._myranks:
            return True
        else:
            return False
        
        
    def evaluateHand(self):
        """Evaluates hand for highest possible combination
        and returns it, else returns 'nothing'"""
        if self.hasRoyalFlush():
            return "Royal Flush"
        elif self.hasStraightFlush():
            return "Straight Flush"
        elif self.hasFourOfAKind():
            return "Four of a kind"
        elif self.hasFullHouse():
            return "Full House"
        elif self.hasFlush():
            return "Flush"
        elif self.hasStraight():
            return "Straight"
        elif self.hasThreeOfAKind():
            return "Three of a kind"
        elif self.hasTwoPair():
            return "Two Pairs"
        elif self.hasPair():
            return "Pair"
        else:
            return "Sorry You've Got Nothing"



#Without using tkinter or graphics

import random

suits = ('hearts', 'diamonds', 'clubs', 'spades')
numcards = ('ace', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' )
value = {'ace':11, 'two':2,'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10 }
playing  = True

class Card:
	def __init__(self, suit, numcard):
		self.suit = suit
		self.numcard = numcard
	def __str__(self):
		return "Card : " + self.suit + ' ' + self.numcard


class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for numcard in numcards:
				self.deck.append(Card(suit,numcard))
	def shuffle(self):
		random.shuffle(self.deck)
	def __str__(self):
		pass
	def pop_card(self):
		single_card = self.deck.pop()
		return single_card

class Hand:
	def __init__(self):
		self.val = 0
		self.aces = 0
		self.carddds = []
	def add_card(self, card):
		self.carddds.append(card)
		self.val += value[card.numcard]
		if card.numcard == 'ace':
			self.aces += 1
	def adjust_ace(self):
		if self.val > 21 and self.aces > 0:
			self.aces -= 1
			self.val -= 10


totalbet = 0
while(playing==True):
	bet = int(input('Enter your bet : '))
	yo  =  Deck()
	yo.shuffle()

	user_hand = Hand()
	cpu_hand = Hand()

	cpu_hand.add_card(yo.pop_card())
	cpu_hand.add_card(yo.pop_card())
	user_hand.add_card(yo.pop_card())
	user_hand.add_card(yo.pop_card())
    
	print('One CPU card is : {}'.format(cpu_hand.carddds[0]))
	
	print('User cards are : {} and {}'.format(user_hand.carddds[0] , user_hand.carddds[1]))

	user_hand.adjust_ace()
	cpu_hand.adjust_ace()

	hitorpass = input('Press H to Hit and P to pass : ')
	while(hitorpass=='H'):
		i = 2
		user_hand.add_card(yo.pop_card())
		user_hand.adjust_ace()
		print('New card is {}'.format(user_hand.carddds[i]))
		i+= 1
		if user_hand.val > 21:
			break
		hitorpass = input('Press H to Hit and P to pass : ')
	print('CPU blind card was {}'.format(cpu_hand.carddds[1]))
	if user_hand.val > 21:
		print('You just lost your bet of ${}'.format(bet))
		totalbet -= bet
	elif user_hand.val<cpu_hand.val:
		print('You just lost your bet of ${}'.format(bet))
		totalbet -= bet
	elif user_hand.val==cpu_hand.val:
		totalbet += 0
		print('Draawwwwwwwwwwwwwwwwwwwwww!!!!!')
	else:
		print('You just won your bet of ${}'.format(bet))
		totalbet += bet

	play = input("Press Y to play again and N to leave")
	if(play=='Y'):
		playing=True
	else:
		playing=False
		print('Thanks for playing \nYour Total earning from todays game is : {}'.format(totalbet))


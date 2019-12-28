import random
from tkinter import *
import cv2
suits = ('hearts', 'diamonds', 'clubs', 'spades')
numcards = ('ace', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' )
value = {'ace':11, 'two':2,'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10 }
imgloc = {('hearts', 'ace'):"h1.png",('hearts', 'two'):"h2.png",('hearts', 'three'):"h3.png",('hearts', 'four'):"h4.png",('hearts', 'five'):"h5.png",('hearts', 'six'):"h6.png",('hearts', 'seven'):"h7.png",('hearts', 'eight'):"h8.png",('hearts', 'ten'):"h10.png",('hearts', 'jack'):"hj.png",('hearts', 'queen'):"hq.png",('hearts', 'king'):"hk.png",('hearts', 'nine'):"h9.png",
('spades', 'ace'):"s1.png",('spades', 'two'):"s2.png",('spades', 'three'):"s3.png",('spades', 'four'):"s4.png",('spades', 'five'):"s5.png",('spades', 'six'):"s6.png",('spades', 'seven'):"s7.png",('spades', 'eight'):"s8.png",('spades', 'ten'):"s10.png",('spades', 'jack'):"sj.png",('spades', 'queen'):"sq.png",('spades', 'king'):"sk.png",('spades', 'nine'):"s9.png",
('clubs', 'ace'):"c1.png",('clubs', 'two'):"c2.png",('clubs', 'three'):"c3.png",('clubs', 'four'):"c4.png",('clubs', 'five'):"c5.png",('clubs', 'six'):"c6.png",('clubs', 'seven'):"c7.png",('clubs', 'eight'):"c8.png",('clubs', 'ten'):"c10.png",('clubs', 'jack'):"cj.png",('clubs', 'queen'):"cq.png",('clubs', 'king'):"ck.png",('clubs', 'nine'):"c9.png",
('diamonds', 'ace'):"d1.png",('diamonds', 'two'):"d2.png",('diamonds', 'three'):"d3.png",('diamonds', 'four'):"d4.png",('diamonds', 'five'):"d5.png",('diamonds', 'six'):"d6.png",('diamonds', 'seven'):"d7.png",('diamonds', 'eight'):"d8.png",('diamonds', 'ten'):"d10.png",('diamonds', 'jack'):"dj.png",('diamonds', 'queen'):"dq.png",('diamonds', 'king'):"dk.png",('diamonds', 'nine'):"d9.png"
}

playing  = True

class Card:
	def __init__(self, suit, numcard):
		self.suit = suit
		self.numcard = numcard

class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for numcard in numcards:
				self.deck.append(Card(suit, numcard))
	def shuffle(self):
		random.shuffle(self.deck)
	def pop_card(self):
		singlecard = self.deck.pop()
		return singlecard

class Hand:
	def __init__(self):
		self.cards = []
		self.val = 0
		self.aces = 0
	def add_card(self, card):
		self.cards.append(card)
		if card.numcard == 'ace':
			self.aces += 1
		self.val += value[card.numcard]
		self.img = PhotoImage(file =imgloc[(card.suit, card.numcard)])
		self.label = Label(BlackJack, image = self.img)	
		self.label.pack()
	def adjust_ace(self):
		if self.aces > 0 and self.val > 21:
			self.aces -= 1
			self.val -= 10

			
hitpass = False
def hitorpass():
	if hitpass == True:
		user_hand.add_card(yo.pop_card())
def check_win():
	if user_hand.val > cpu_hand.val and user_hand.val <= 21:
		return True
	elif user_hand.val == cpu_hand.val:
		return True 
	else:
		return False

yo = Deck()
user_hand = Hand()
cpu_hand = Hand()
yo.shuffle()
BlackJack = Tk()
BlackJack.title('BlackJack - Aditya')
user_hand.add_card(yo.pop_card())
img1 = PhotoImage(file=imgloc[(user_hand.cards.suit, user_hand.cards.numcard)])
label1 = Label(BlackJack, image = img1)
label1.pack(side = 'bottom')

user_hand.add_card(yo.pop_card())
img2 = PhotoImage(file=imgloc[(user_hand.cards.suit, user_hand.cards.numcard)])
label2 = Label(BlackJack, image = img2)
label2.pack(side ='bottom')

user_hand.add_card(yo.pop_card())
img3 = PhotoImage(file=imgloc[(user_hand.cards.suit, user_hand.cards.numcard)])
label3 = Label(BlackJack, image = img3)
label3.pack(side = 'bottom')

cpu_hand.add_card(yo.pop_card())
img4 = PhotoImage(file=imgloc[(cpu_hand.cards.suit, cpu_hand.cards.numcard)])
label4 = Label(BlackJack, image = img4)
label4.pack(side = 'top')

cpu_hand.add_card(yo.pop_card())
img5 = PhotoImage(file=imgloc[(cpu_hand.cards.suit, cpu_hand.cards.numcard)])
label5 = Label(BlackJack, image = img5)
label5.pack(side = 'top')


hit = Button(BlackJack, text = "HIT", command= user_hand.add_card(yo.pop_card()))
hit.pack(side='left')

leave = Button(BlackJack, text="PASS")
leave.pack()
BlackJack.mainloop()
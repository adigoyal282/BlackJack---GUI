import random
from tkinter import *
import time
import tkinter.messagebox
suits = ('hearts', 'diamonds', 'clubs', 'spades')
numcards = ('ace', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' )
value = {'ace':11, 'two':2,'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10 }
imgloc = {('hearts', 'ace'):"h1.png",('hearts', 'two'):"h2.png",('hearts', 'three'):"h3.png",('hearts', 'four'):"h4.png",('hearts', 'five'):"h5.png",('hearts', 'six'):"h6.png",('hearts', 'seven'):"h7.png",('hearts', 'eight'):"h8.png",('hearts', 'ten'):"h10.png",('hearts', 'jack'):"hj.png",('hearts', 'queen'):"hq.png",('hearts', 'king'):"hk.png",('hearts', 'nine'):"h9.png",
('spades', 'ace'):"s1.png",('spades', 'two'):"s2.png",('spades', 'three'):"s3.png",('spades', 'four'):"s4.png",('spades', 'five'):"s5.png",('spades', 'six'):"s6.png",('spades', 'seven'):"s7.png",('spades', 'eight'):"s8.png",('spades', 'ten'):"s10.png",('spades', 'jack'):"sj.png",('spades', 'queen'):"sq.png",('spades', 'king'):"sk.png",('spades', 'nine'):"s9.png",
('clubs', 'ace'):"c1.png",('clubs', 'two'):"c2.png",('clubs', 'three'):"c3.png",('clubs', 'four'):"c4.png",('clubs', 'five'):"c5.png",('clubs', 'six'):"c6.png",('clubs', 'seven'):"c7.png",('clubs', 'eight'):"c8.png",('clubs', 'ten'):"c10.png",('clubs', 'jack'):"cj.png",('clubs', 'queen'):"cq.png",('clubs', 'king'):"ck.png",('clubs', 'nine'):"c9.png",
('diamonds', 'ace'):"d1.png",('diamonds', 'two'):"d2.png",('diamonds', 'three'):"d3.png",('diamonds', 'four'):"d4.png",('diamonds', 'five'):"d5.png",('diamonds', 'six'):"d6.png",('diamonds', 'seven'):"d7.png",('diamonds', 'eight'):"d8.png",('diamonds', 'ten'):"d10.png",('diamonds', 'jack'):"dj.png",('diamonds', 'queen'):"dq.png",('diamonds', 'king'):"dk.png",('diamonds', 'nine'):"d9.png"
}
#We can slice up the python window in multiple frames by using Frame key word

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
		self.val += value[card.numcard]
		if card.numcard == 'ace':
			self.aces += 1


	def adjust_ace(self):
		if self.aces > 0 and self.val > 21:
			self.aces -= 1
			self.val -= 10
i = 1



BlackJack = Tk()
BlackJack.title('BlackJack - Aditya')

yo = Deck()
user_hand = Hand()
cpu_hand = Hand()
yo.shuffle()
user_hand.add_card(yo.pop_card())
img1 = PhotoImage(file=imgloc[(user_hand.cards[0].suit, user_hand.cards[0].numcard)])
label1 = Label(BlackJack, image = img1)
label1.grid(column = 0, row = 4)

user_hand.add_card(yo.pop_card())
img2 = PhotoImage(file=imgloc[(user_hand.cards[1].suit, user_hand.cards[1].numcard)])
label2 = Label(BlackJack, image = img2)
label2.grid(column = 1, row = 4)

def presshit():
	global i
	user_hand.add_card(yo.pop_card())
	img3 = PhotoImage(file=imgloc[(user_hand.cards[2].suit, user_hand.cards[2].numcard)])
	
	label3 = Label(BlackJack, image = img3)
	label3.grid(column = 2, row = 4)
	
	i += 1

def check_win():
	if (user_hand.val > cpu_hand.val) and user_hand.val<=21:
		tkinter.messagebox.showinfo('User Won')
	elif user_hand.val == cpu_hand.val:
		tkinter.messagebox.showinfo('Game Tied')
	else:
		tkinter.messagebox.showinfo('CPU Won')
	

	
cpu_hand.add_card(yo.pop_card())
img4 = PhotoImage(file=imgloc[(cpu_hand.cards[0].suit, cpu_hand.cards[0].numcard)])
label4 = Label(BlackJack, image = img4)
label4.grid(column = 0, row = 1)

cpu_hand.add_card(yo.pop_card())
img5 = PhotoImage(file=imgloc[(cpu_hand.cards[1].suit, cpu_hand.cards[1].numcard)])
label5 = Label(BlackJack, image = img5)
label5.grid(column = 1, row = 1)

hit = Button(BlackJack, text = "HIT",fg = "green", command =lambda: presshit())
hit.grid(column=0, row = 2)

leave = Button(BlackJack, text="PASS", fg="red", command =lambda: check_win())
leave.grid(column=1, row= 2)

	
BlackJack.mainloop()
print(i)

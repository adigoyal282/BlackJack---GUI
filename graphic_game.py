#New try of black jack using gui

from tkinter import *
import random
import tkinter.messagebox
suits = ('hearts', 'diamonds', 'clubs', 'spades')
numcards = ('ace', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king' )
NValue = {'ace':11, 'two':2,'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10 }
imgloc = {('hearts', 'ace'):"h1.png",('hearts', 'two'):"h2.png",('hearts', 'three'):"h3.png",('hearts', 'four'):"h4.png",('hearts', 'five'):"h5.png",('hearts', 'six'):"h6.png",('hearts', 'seven'):"h7.png",('hearts', 'eight'):"h8.png",('hearts', 'ten'):"h10.png",('hearts', 'jack'):"hj.png",('hearts', 'queen'):"hq.png",('hearts', 'king'):"hk.png",('hearts', 'nine'):"h9.png",
('spades', 'ace'):"s1.png",('spades', 'two'):"s2.png",('spades', 'three'):"s3.png",('spades', 'four'):"s4.png",('spades', 'five'):"s5.png",('spades', 'six'):"s6.png",('spades', 'seven'):"s7.png",('spades', 'eight'):"s8.png",('spades', 'ten'):"s10.png",('spades', 'jack'):"sj.png",('spades', 'queen'):"sq.png",('spades', 'king'):"sk.png",('spades', 'nine'):"s9.png",
('clubs', 'ace'):"c1.png",('clubs', 'two'):"c2.png",('clubs', 'three'):"c3.png",('clubs', 'four'):"c4.png",('clubs', 'five'):"c5.png",('clubs', 'six'):"c6.png",('clubs', 'seven'):"c7.png",('clubs', 'eight'):"c8.png",('clubs', 'ten'):"c10.png",('clubs', 'jack'):"cj.png",('clubs', 'queen'):"cq.png",('clubs', 'king'):"ck.png",('clubs', 'nine'):"c9.png",
('diamonds', 'ace'):"d1.png",('diamonds', 'two'):"d2.png",('diamonds', 'three'):"d3.png",('diamonds', 'four'):"d4.png",('diamonds', 'five'):"d5.png",('diamonds', 'six'):"d6.png",('diamonds', 'seven'):"d7.png",('diamonds', 'eight'):"d8.png",('diamonds', 'ten'):"d10.png",('diamonds', 'jack'):"dj.png",('diamonds', 'queen'):"dq.png",('diamonds', 'king'):"dk.png",('diamonds', 'nine'):"d9.png"
}
class Card:
	def __init__(self,suit,numcard):
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
	

class Value:
	def __init__(self):
		self.value = 0
		self.aces = 0
	def add_value(self,card):
		self.value += NValue[card.numcard]
		if card.numcard == 'ace':
			self.aces += 1
	def adjust_Ace(self):
		if(self.aces>=1 and self.value > 21):
			self.value -= 10
			self.aces -= 1
root = Tk()
root.title('BlackJack- Aditya')
taash = Deck()
taash.shuffle()
i = 0
user_value = Value()
cpu_value = Value()
def press_hit():
	global i 
	if(i==0):
		user_value.add_value(taash.deck[4])	
		label5 = Label(root, image = img5)
		label5.grid(column = 2, row = 3)
		
	if i==1:
		user_value.add_value(taash.deck[5])	
		label6 = Label(root, image = img6)
		label6.grid(column = 3, row = 3)
	i += 1
		


def check_win():
	label2.grid(column = 1, row = 1)
	if (user_value.value > cpu_value.value) and user_value.value<=21:
		tkinter.messagebox.showinfo('User Won')
	elif user_value.value == cpu_value.value:
		tkinter.messagebox.showinfo('Game Tied')
	else:
		tkinter.messagebox.showinfo('CPU Won')


	


#cpu has card 3 and 1
cpu_value.add_value(taash.deck[0])
cpu_value.add_value(taash.deck[2])
img1 = PhotoImage(file =imgloc[(taash.deck[0].suit,taash.deck[0].numcard)])
img2 = PhotoImage(file= imgloc[(taash.deck[2].suit, taash.deck[2].numcard)])
label1 = Label(root, image = img1)
label1.grid(column = 0, row = 1)
label2 = Label(root, image = img2)

user_value.add_value(taash.deck[1])
user_value.add_value(taash.deck[3])
img3 = PhotoImage(file =imgloc[(taash.deck[1].suit,taash.deck[1].numcard)])
img4 = PhotoImage(file= imgloc[(taash.deck[3].suit, taash.deck[3].numcard)])
img5 = PhotoImage(file= imgloc[(taash.deck[4].suit, taash.deck[4].numcard)])
img6 = PhotoImage(file= imgloc[(taash.deck[5].suit, taash.deck[5].numcard)])

label3 = Label(root, image = img3)
label3.grid(column = 0, row = 3)
label4 = Label(root, image = img4)
label4.grid(column = 1, row = 3)

hit = Button(root, text='HIT', command= lambda:press_hit())
leave = Button(root, text='PASS', command= lambda:check_win())
hit.grid(column=0, row=2)
leave.grid(column=1, row=2)
root.mainloop()




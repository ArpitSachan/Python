
from random import shuffle


SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards=[]
for r in RANKS:
	for s in SUITE:
		mycards.append((s, r))

class Deck:
	def __init__(self):
		print("Creating new ordered deck")
		self.allcards=mycards

	def shuffle(self):
		print("Shuffling Deck")
		shuffle(self.allcards)

	def split_in_half(self):
		return (self.allcards[:26], self.allcards[26:])

class Hand:

	def __init__(self, cards):
		self.cards=cards

	def __str__(self):
		return "Contains {} cards".format(len(self.cards))

	def add(self, added_cards):
		self.cards.extend(added_cards)

	def remove_card(self):
		return self.cards.pop()

class Player:

	def __init__(self, name, hand):
		self.name=name
		self.hand=hand

	def play_card(self):
		drawn_card=self.hand.remove_card()
		print("{} has placed: {}".format(self.name, drawn_card))
		print("/n")
		return drawn_card

	def remove_war_cards(self):
		war_cards=[]
		if len(self.hand.cards)<3:
			return self.hand.cards
		else:
			for x in range(3):
				war_cards.append(self.hand.cards.pop())
			return war_cards

	def still_has_cards(self):
		"""
		Return True if player still has cards
		"""

		return len(self.hand.cards)!=0


# Create a new deck and split in two half

d= Deck()
d.shuffle()
half1, half2=d.split_in_half()

#create both player!
comp=Player("comp", Hand(half1))

name=input("What's your name?: ")
user=Player(name, Hand(half2))


totla_rounds=0
war_cards=0
war_count=0
while user.still_has_cards() and comp.still_has_cards():
	totla_rounds+=1
	print("Time for a new round")
	print("Here are the current standings")
	print(user.name+"has the count: "+str(len(user.hand.cards)))
	print(comp.name+"has the count"+str(len(comp.hand.cards)))
	print("Play a card!")


	table_cards=[]
	c_card=comp.play_card()
	p_card=user.play_card()

	table_cards.append(c_card)
	table_cards.append(p_card)

	if(c_card[1]==p_card[1]):
		war_count+=1

		print("War!")

		table_cards.extend(user.remove_war_cards())
		table_cards.extend(comp.remove_war_cards())

		if(RANKS.index(c_card[1])<RANKS.index(p_card[1])):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)

	else:
		if(RANKS.index(c_card[1])<RANKS.index(p_card[1])):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)


print("Game over!, number of rounds: "+str(totla_rounds))
print("A war happened "+str(war_count)+" times")
print("Computer cards: ")
print(str(comp.still_has_cards()))
print("Player cards: ")
print(str(user.still_has_cards()))
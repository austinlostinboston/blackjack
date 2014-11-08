# -*- coding: utf-8 -*-
import random
#import sys
#import codecs

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class deck():

	def __init__(self,num_decks=1):
		self.num_decks = num_decks
		self.cards = []
		for i in range(0,self.num_decks):
			self.cards.extend(list(range(1,53)))

	def __str__(self):
		return "Number of decks: %s \nCards left in deck: %s \nCards: %s" % (self.num_decks,len(self.cards),self.cards)

	def shuffle(self):
		random.shuffle(self.cards)

	def chooseOne(self):
		# Chooses cards on top as if top card was being turned over
		card = self.cards[0]

		# Deletes existance of top card
		self.cards = self.cards[1:]

		# Returns selected card
		#print(card)
		#return readCard(card)[0]
		return card

def readCard(card):
	#suites = [u'♠', u'♥', u'♦', u'♣']
	suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
	card_pos = card % 13
	hand_name = ''
	suite = ''

	# Determins face value of card
	if card_pos == 11:
		hand_name = 'Jack'
		card_val = 10
	elif card_pos == 12:
		hand_name = 'Queen'
		card_val = 10
	elif card_pos == 0:
		hand_name = 'King'
		card_val = 10
	elif card_pos == 1:
		hand_name = 'Ace'
		card_val = 11
	else:
		hand_name = card_pos
		card_val  = card_pos

	# Determines suite value of card
	if card >= 1 and card <= 13:
		suite = suites[0]
	elif card >= 14 and card <= 26:
		suite = suites[1]
	elif card >= 27 and card <= 39:
		suite = suites[2]
	elif card >= 40 and card <= 52:
		suite = suites[3]
	else:
		return 'Card Suite Error!'

	#print(u'♥')
	#sys.stdout.buffer.write('♥')
	return "%s %s" % (hand_name,suite), card_val
#text = sys.stdout(u'♠')
#print(text.encode('utf-8'))
#print(sys.stdout.encoding)
#print(text)
#sys.stdout.write("Ûnicöde")
#sys.stdout.buffer.write('\u25BC'.encode('cp437'))
#print('♠'.encode('cp437'))
import deck

class players():

	def __init__(self, is_dealer=True):
		self.hand = []
		self.card_vals = []
		self.is_dealer = is_dealer

	def __str__(self):
		if self.is_dealer:
			ret_str = "Dealer's"
		else:
			ret_str = "Player's"

		return ret_str + " hand: %s\ncards: %s\nscore: %s" % (self.hand,self.readHand(self.hand),self.score())

	def addToHand(self, card_pos):
		self.hand.append(card_pos)
		self.card_vals.append(deck.readCard(card_pos)[1])

	def score(self):
		total = 0
		for val in self.card_vals:
			total += val
		return total

	def readHand(self,hand):
		self.hand = hand
		cards = []
		for card in hand:
			read = deck.readCard(card)[0]
			cards.append(read)
		return cards

	def clearHand(self):
		self.hand = []
		self.card_vals = []

	def soften(self):
		while 11 in self.card_vals and self.score() > 21:
			ace = self.card_vals.index(11)
			self.card_vals[ace] = 1
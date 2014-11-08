from players import players
from deck import deck

class game():
	
	def __init__(self,num_decks=1):
		#self.num_players = num_players

		self.deck = deck(num_decks)
		self.dealer = players(True)
		self.player = players(False)

		self.deck.shuffle()

	def __str__(self):
		return "Dealer's Hand: %s Score: %s\nPlayer's Hand: %s Score: %s" % (self.dealer.readHand(self.dealer.hand), self.dealer.score(), self.player.readHand(self.player.hand), self.player.score())

	def dealHand(self):
		self.dealer.clearHand()
		self.player.clearHand()

		self.player.addToHand(self.deck.chooseOne())
		self.dealer.addToHand(self.deck.chooseOne())
		self.player.addToHand(self.deck.chooseOne())
		self.dealer.addToHand(self.deck.chooseOne())

		self.player.soften()
		self.dealer.soften()

	def dealerPlay(self):
		while self.dealer.score() < 17:
			self.dealer.addToHand(self.deck.chooseOne())
			self.dealer.soften()

	def hit(self):
		self.player.addToHand(self.deck.chooseOne())
		self.player.soften()

	def whoWon(self):
		if self.dealer.score() >= self.player.score():
			return 0
		else:
			return 1





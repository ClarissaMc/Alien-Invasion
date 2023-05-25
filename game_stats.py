class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# High score should never be reset.
		#	Retrieve high score if it exists,
		#	Otherwise set it to 0
		try:
			with open('high_score.txt', 'r') as file_object:
				contents = file_object.read()
				self.high_score = int(contents)
		except FileNotFoundError:
			self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
import pygame.mixer

class Settings:
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's static settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 10

		# Sound settings
		pygame.mixer.init()
		self.initialize_sounds()
		self.initialize_volume()

		# How quickly the game speeds up
		self.speedup_scale = 1.2

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

	def initialize_sounds(self):
		"""Initialize all sounds."""
		self.gun = pygame.mixer.Sound('sounds/ship_gun.wav')
		self.alien_hit = pygame.mixer.Sound('sounds/alien_hit.wav')
		self.game_over = pygame.mixer.Sound('sounds/game_over.wav')
		self.game_start = pygame.mixer.Sound('sounds/game_start.wav')
		self.ship_hit = pygame.mixer.Sound('sounds/ship_hit.wav')
		self.new_level = pygame.mixer.Sound('sounds/new_level.wav')

	def initialize_volume(self):
		"""Set volume for each sound."""
		self.gun.set_volume(0.15)
		self.alien_hit.set_volume(0.15)
		self.game_start.set_volume(0.3)
		self.ship_hit.set_volume(0.3)
		self.new_level.set_volume(0.5)
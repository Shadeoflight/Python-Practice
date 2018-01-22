
# Game

import pygame as pg # Rename for easier usage
import random

# Custom files
from settings import * # Import all variables
from sprites import *

class Game:
	def __init__(self):
		# Initialize the game window
		self.running = True
		
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		
		#pass # Python for do nothing, used as placeholder
		
	def new(self):
		# Starts a new game. Re-initializes game
		self.all_sprites = pg.sprite.Group()
		
		# To make adding collisions easier
		self.platforms = pg.sprite.Group()
		
		# Add platform
		p1 = Platform(0, HEIGHT-40, WIDTH, 40)
		self.all_sprites.add(p1)
		self.platforms.add(p1)
		
		# Add player
		self.player = Player()
		self.all_sprites.add(self.player)
		
		# Start the game loop
		self.run()
		
	def run(self):
		# Run the game loop
		self.playing = True
		
		while self.playing:
			self.clock.tick(FPS) # Loop run speed
			self.events()
			self.update()
			self.draw()
		
	#
	# Game loop components
	#
	
	def update(self):
		# Game loop - updater
		self.all_sprites.update()
		
	def events(self):
		# Game loop - events
		
		# Process input events
		for event in pg.event.get():
			# Check for closed window
			if(event.type == pg.QUIT):
				if(self.playing):
					self.playing = False
				self.running = False
		
	def draw(self):
		# Game loop - draw
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pg.display.flip()
		
	def show_start_screen(self):
		# Game start screen
		pass
		
	def show_go_screen(self):
		# Game over or continue
		pass
#
#	Main program
#
game_object = Game()
game_object.show_start_screen()
while game_object.running:
	game_object.new()
	game_object.show_go_screen()
	
pg.quit()
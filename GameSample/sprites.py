
# Sprite class

import pygame as pg

# Custom files
from settings import *

# Function assignments
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((30, 40))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)
		
		self.pos = vec(WIDTH/2,HEIGHT/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		
	def update(self):
		# Initialize acceleration
		self.acc = vec(0,0)
		
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_UP]:
			self.acc.y = -PLAYER_ACC
		if keys[pg.K_DOWN]:
			self.acc.y = PLAYER_ACC
		
		self.acc.x += self.vel.x * PLAYER_FRICTION # Friction for x
		self.acc.y += self.vel.y * PLAYER_FRICTION # Friction for y
		self.vel += self.acc # Acceleration adds to velocity
		self.pos += self.vel + 0.5 * self.acc
		
		self.rect.center = self.pos
		
		# Collision with wall - Wrap around
		#if self.pos.x > WIDTH:
		#	self.pos.x = 0
		#if self.pos.x < 0:
		#	self.pos.x = WIDTH
		#if self.pos.y > HEIGHT:
		#	self.pos.y = 0
		#if self.pos.y < 0:
		#	self.pos.y = HEIGHT
		
		# Collision with wall - Stop
		if self.pos.x > WIDTH:
			self.pos.x = WIDTH
		if self.pos.x < 0:
			self.pos.x = 0
		if self.pos.y > HEIGHT:
			self.pos.y = HEIGHT
		if self.pos.y < 0:
			self.pos.y = 0
		
class Platform(pg.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		
		
		
		
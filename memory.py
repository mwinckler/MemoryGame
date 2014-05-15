#!/usr/bin/python

# Things we need
# + A list of identifiers we'll use to match
#	- Later: a list of pictures associated with these numbers
# - A way to position the identifiers on a grid to display to the user
# + A function which takes two grid coordinates and returns true if the underlying identifiers match, else false
# + Some kind of state indicating which identifiers the user has already matched
# + Randomize the list of items
# - Positions the items in the grid
# - A way for the user to enter a guess (pick a box)

import random

class MemoryGame:
	
	def __init__(self, number_of_items, ui_provider):
		self.items = range(number_of_items)
		self.ui = ui_provider

	def new_game(self):
		self.current_guess = None
		self.correct_guesses = list()
		self.board_items = list(self.items)
		self.board_items.extend(self.board_items)
		random.shuffle(self.board_items)
		self.ui.initialize_board(self.board_items)
		self.ui.guess = guess

	def guess(self, value):
		'''Accepts a guess the user has made. If there's already an outstanding
		guess, then: if this new value matches, the user scores a point (both 
		remain open). If the new value doesn't match, then this method tells
		the UI to hide both values again. If a previous guess does not already
		exist, this method just stores the guess and does nothing else.'''

		if (self.current_guess != None):
			if (self.current_guess != value):
				# TODO: Insert a delay here so the user can see the second value he guessed
				self.ui.hide_values([self.current_guess, value])
			else:
				self.correct_guesses.append(value)
				if (len(set(self.correct_guesses) & set(self.items)) == len(self.items)):
					# User wins, all have been guessed

		else
			self.current_guess = value





class ConsoleUI:

	def __init__(self):
		self.game_is_running = False

	def initialize_board(self, board_items):
		self.board_items = board_items
		self.game_is_running = True
		self.start_loop()

	def start_loop(self):
		while (self.game_is_running):
			self.draw()

	def draw(self):
		# TODO: make this (re)draw on the same line, not a new line every time
		print " ".join(map(str, self.board_items))

		# When a user enters a cell:
		# 1. Look up the identifier associated with the coordinate
		# 2. Call self.guess(value) to tell the MemoryGame instance about this guess


	def hide_values(self, values):
		'''Hides all cells which contain the specified values.'''
		# TODO: Find the locations of the specified value, and hide them




game = MemoryGame(7, ConsoleUI())
game.new_game()
import pygame

class Functions(object):
	def __init__(self):
		pygame.init()
		self.bool_turn = True
		self.game_state = [1,2,3,4,5,6,7,8,9]
		self.isRunning = True
		self.move_count = 0
		self.mode = "human"
		self.ai_diff = "easy"
		self.mode_i = 0
		self.ai_diff_i = 0

	def take_turn(self, n):
		if self.bool_turn == True:
			for num in range(1,10):
				if num == n:
					if type(self.game_state[num - 1]) == int and self.isRunning == True:
						self.game_state[num - 1] = "X"
						self.bool_turn = not self.bool_turn
						self.move_count += 1
						return True

		elif self.bool_turn == False:
			for num in range(1,10):
				if num == n:
					if type(self.game_state[num - 1]) == int and self.isRunning == True:
						self.game_state[num - 1] = "O"
						self.bool_turn = not self.bool_turn
						self.move_count += 1
						return True


	def placement_grid(self, x, y):
		if x > 50 and x < 350:
			if y > 50 and y < 350:
				if x >= 50 and x < 150:
					if y >= 50 and y < 150:
						return(1)
					elif y >= 150 and y < 250:
						return(4)
					elif y >= 250 and y <= 350:
						return(7)
				elif x >= 150 and x < 250:
					if y >= 50 and y < 150:
						return(2)
					elif y >= 150 and y < 250:
						return(5)
					elif y >= 250 and y <= 350:
						return(8)
				elif x >= 250 and x <= 350:
					if y >= 50 and y < 150:
						return(3)
					elif y >= 150 and y < 250:
						return(6)
					elif y >= 250 and y <= 350:
						return(9)

	def reset_game(self, x, y):
		if x > 230 and x < 380:
			if y > 370 and y < 415:
				self.bool_turn = True
				self.game_state = [1,2,3,4,5,6,7,8,9]
				self.isRunning = True
				self.move_count = 0
				return True


import random

class Die():
	def __init__(self, sides):
		self.sides = sides
	
	def roll(self):
		rolled = random.randint(1, self.sides)
		print ("You rolled a {}-sided die and got a {}".format(self.sides, rolled))
		return rolled
		
sides = 20
test = Die(sides)
rolls = []
totalRolls = 0
while len(rolls) < sides:
	totalRolls += 1
	newRoll = test.roll()
	if not newRoll in rolls:
		rolls.append(newRoll)
print (rolls)
print ("It took {} rolls to roll all possible values!".format(totalRolls))
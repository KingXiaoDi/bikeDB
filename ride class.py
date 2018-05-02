import datetime
import pandas

class Ride():
	def __init__(self, date):
		self.date = date
		
	def setStart(self, start):
		self.start = start

	def setEnd(self, end):
		self.end = end
		
	def setDist(self, dist):
		self.dist = dist
		
	def getDate(self):
		if hasattr(self, 'date'):
			print ("Date: {}".format(self.date))
		else:
			print ("Attribute 'Date' not yet set")

	def getStart(self):
		if hasattr(self, 'start'):
			print ("Start: {}".format(self.start))
		else:
			print ("Attribute 'Start' not yet set")

	def getEnd(self):
		if hasattr(self, 'end'):
			print ("End: {}".format(self.end))
		else:
			print ("Attribute 'End' not yet set")
			
	def getDist(self):
		if hasattr(self, 'dist'):
			print ("Dist: {}".format(self.dist))
		else:
			print ("Attribute 'Dist' not yet set")
			
	def p(self):
		print (vars(self))
#		print ("{}: {}".format(each, self[each]))
		
today = datetime.datetime.now().date()
test = Ride(today)
test.setStart('8528 Fox')
test.setEnd('8528 Fox')
test.setDist(3.0)
test.getStart()
test.getEnd()
test.getDist()


test.p()
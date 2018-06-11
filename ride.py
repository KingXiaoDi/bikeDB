import datetime
import pandas

class Ride():
	def __init__(self, row):
		self.date = row['RideDate']
		self.start = row['LocationStart']
		self.end = row['LocationEnd']
		self.dist = row['Distance']
		if pandas.notnull(row['TimeStart']):
			self.timeStart = row['TimeStart']
		if pandas.notnull(row['TimeEnd']):
			self.timeEnd = row['TimeEnd']

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
		for each in self.__dict__:
			print ("{}: {}".format(each, self.__dict__[each]))

if __name__ == "__main__":
	pass
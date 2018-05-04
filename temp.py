import datetime
import pandas

file = 'c:/users/josh/documents/python/biking/biking.csv'

bikeDF = pandas.read_csv(file, index_col=0)
bikeDF['Date'] = pandas.to_datetime(bikeDF['Date'])
#bikeDF = bikeDF.replace(['Lnth LR'], 'Linthicum Light Rail')
bikeDF.to_csv(file)

for year in range(2017, 2018):
	pass
	df = bikeDF.loc[bikeDF['Date'].dt.year == year].reset_index(drop=True)
	#print ()
	#print ()
from mySQL import createConnection, closeConnection, query
from ride import Ride
import datetime
import pandas
import numpy

def loadCSV(name):
	bikeDF = pandas.read_csv(file, index_col=None).sort_values(by='RideDate')
	bikeDF['RideDate'] = pandas.to_datetime(bikeDF['RideDate'])
	return bikeDF

def uploadDFtoSQL(df, con):
	print ('Attempting to upload df to MySQL')
	try: 
		print (df)
		df.to_sql('rides', con, if_exists='append', index=False)
		print ('Upload successful.')
	except Error as e:
		print ('Upload failed.')
		print (e)

def prepareForUpload(df, con):
	for year in range(2016, 2019):
		df = bikeDF.loc[bikeDF['RideDate'].dt.year == year].reset_index(drop=True)
		uploadDFtoSQL(df, con)

def saveCSV(df, name):
	df.to_csv(file)
		
def doAll(file):
	connection = createConnection('bikeUpload', 'biking')
	#uploadDFtoSQL(loadCSV(file), connection)
	query(connection, 'SELECT * FROM rides WHERE RideID > 198')
	closeConnection(connection)	

#file = 'c:/users/josh/documents/python/biking/biking.csv'
file = 'c:/users/yoshi/documents/python_scripts/biking/biking.csv'
	
#connection = createConnection('bikeUpload', 'biking')
#query(connection, 'SELECT * FROM rides WHERE RideID > 198')
#closeConnection(connection)

#doAll(file)

bike = loadCSV(file)
print (bike)
for row in bike.iterrows():
	#print (row)
	temp = Ride(row[1])
	temp.p()
	print ()
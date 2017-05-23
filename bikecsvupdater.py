import sqlalchemy
import datetime
import pandas


con = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1/biking')

data = pandas.read_sql('select * from data', con)
details = pandas.read_sql('select * from details', con)
times = []
for start, stop in zip(data['Start_Time'], data['Stop_Time']):
	time = stop - start
	times.append(time.seconds/3600)
	
merged = pandas.merge(data, details, on=['Ride_ID', 'Ride_ID'])
keep = merged[['Date', 'Ride_From', 'Ride_To', 'Dist', 'Notes']]
keep['Time'] = times

keep.to_csv('c:/users/josh/documents/python_scripts/analyzer.csv')
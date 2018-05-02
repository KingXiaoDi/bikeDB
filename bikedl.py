import sqlalchemy
import datetime
import pandas

con = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1/biking')

data = pandas.read_sql('select * from data', con)

full = pandas.read_excel('c:/users/josh/downloads/biking.xlsx')
full.columns = ['Date', 'Ride_From', 'Ride_To', 'Dist', 'Start_Time', 'Stop_Time', 'Notes']
full['Notes'] = full['Notes'].fillna('N/A')
full[['Start_Time', 'Stop_Time']] = full[['Start_Time', 'Stop_Time']].fillna(datetime.time(0))

to_add = full

for row in full.iterrows():
	try:
		data.append(row[1], verify_integrity=True)
	except ValueError:
		to_add = to_add.drop(row[0], 0)

to_add.index += 1
data_add = to_add[['Date', 'Ride_From', 'Ride_To', 'Start_Time','Stop_Time', 'Dist', 'Notes']]

data_add.index.name = 'Ride_ID'
print (data_add) 
''' 
try:
	data_add.to_sql('data', con, if_exists='append')
except:
	print ("Data upload failed")''' 
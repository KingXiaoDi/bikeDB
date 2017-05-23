import sqlalchemy
import datetime
import pandas


con = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1/biking')

full = pandas.read_excel('c:/users/josh/downloads/biking.xlsx')
full.columns = ['Date', 'Ride_From', 'Ride_To', 'Dist', 'Start_Time', 'Stop_Time', 'Notes']
full['Notes'] = full['Notes'].fillna('N/A')
full[['Start_Time', 'Stop_Time']] = full[['Start_Time', 'Stop_Time']].fillna(datetime.time(0))
full.index += 1

full.index.name = 'Ride_ID'
data = full[['Date', 'Start_Time','Stop_Time', 'Dist', 'Notes']]
details = full[['Ride_From', 'Ride_To']]

for x in data['Date']:
	pandas.to_datetime(data["Date"])


try:
	con.connect()
	print ("Connection successful!")
except:
	print ("Connection failed!")
	quit()
#'''	
try:
	data.to_sql('data', con, if_exists='append')
except:
	print ("Data upload failed")
try:
	details.to_sql('details', con, if_exists='append', index=True)
except:
	print ("Details upload failed")
#	'''
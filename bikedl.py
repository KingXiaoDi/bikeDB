import sqlalchemy
import datetime
import pandas

con = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1/biking')

data = pandas.read_sql('select * from data', con)
details = pandas.read_sql('select * from details', con)
combined = data.merge(details, how = 'inner')

full = pandas.read_excel('c:/users/josh/downloads/biking.xlsx')
full.columns = ['Date', 'Ride_From', 'Ride_To', 'Dist', 'Start_Time', 'Stop_Time', 'Notes']
full['Notes'] = full['Notes'].fillna('N/A')
full[['Start_Time', 'Stop_Time']] = full[['Start_Time', 'Stop_Time']].fillna(datetime.time(0))

to_add = full

for row in full.iterrows():
	try:
		combined.append(row[1], verify_integrity=True)
	except ValueError:
		to_add = to_add.drop(row[0], 0)

to_add.index += 1
data_add = to_add[['Date', 'Start_Time','Stop_Time', 'Dist', 'Notes']]
details_add = to_add[['Ride_From', 'Ride_To']]

data_add.index.name = 'Ride_ID'
details_add.index.name = 'Ride_ID'
print (data_add) 
print (details_add)

try:
	data_add.to_sql('data', con, if_exists='append')
except:
	print ("Data upload failed")
try:
	details_add.to_sql('details', con, if_exists='append', index=True)
except:
	print ("Details upload failed")
from sqlalchemy import create_engine

def createConnection(user, db):
	engine = create_engine('mysql+mysqlconnector://{}:@localhost/{}'.format(user, db))
	return engine.connect()

def testQuery(connection):
	result = connection.execute('SELECT * FROM user')
	for row in result:
		print (row)

def query(connection, sql):
	result = connection.execute(sql)
	for row in result:
		print (row)

def closeConnection(connection):
	connection.close()
	
if __name__ == '__main__':
	connection = createConnection()
	testQuery(connection)
	closeConnection(connection)
import MySQLdb
import MySQLdb.cursors
import gc
from pymongo import MongoClient

gc.collect()

db = MySQLdb.connect({mysql_host},{mysql_root},{mysql_password},{database} cursorclass=MySQLdb.cursors.DictCursor)
cursor = db.cursor()

client = MongoClient('127.0.0.1:27017')
try:

	cursor.execute("select * from statusmessages")

	for row in range(cursor.rowcount):
		data = cursor.fetchone()
		db = client['thekarrier']
		collection = db['location']

		collection.insert_one(data).inserted_id
#		print data

except MySQLdb.Error, e:

	print "Error %d : %s" % (e.args[0], e.args[1])

	sys.exit(1)

db.close()
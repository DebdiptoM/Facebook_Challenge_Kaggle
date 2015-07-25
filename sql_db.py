import os
import sqlite3

db_filename = 'bid-small.csv'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'Need to create schema'
else:
    print 'Database exists, assume schema does, too.'

conn.close()
select(db_filename)
def select(db_filename):
	# db_filename = 'todo.db'

	with sqlite3.connect(db_filename) as conn:
	    cursor = conn.cursor()

	    cursor.execute("""
	    select * from bid-small.csv
	    """)

	    for row in cursor.fetchall():
	        task_id, priority, details, status, deadline = row
	        print '%2d {%d} %-20s [%-8s] (%s)' % (task_id, priority, details, status, deadline)
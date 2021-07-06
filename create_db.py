import sqlite3

connection = sqlite3.connect('phones.db')

cursor = connection.cursor()
sql_query = '''
CREATE TABLE IF NOT EXISTS phones
(contactName text, phoneValue text);
'''

cursor.execute(sql_query)
connection.commit()
connection.close()
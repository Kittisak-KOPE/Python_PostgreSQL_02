import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'boondocs',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

delete_sql_query = '''
    delete from customer where id=3
'''

pointer = connection.cursor()
pointer.execute(delete_sql_query)

connection.commit()
print('record is deleted')
connection.close()
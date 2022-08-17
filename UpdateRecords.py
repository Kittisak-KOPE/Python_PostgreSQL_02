import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'boondocs',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

update_sql_query = '''
    update customer set age=65 where id=2
'''

pointer = connection.cursor()
pointer.execute(update_sql_query)

connection.commit()
print('record is updated')
connection.close()
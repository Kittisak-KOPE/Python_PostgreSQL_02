import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'boondocs',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

insert_sql_query = '''
    insert into Customer(ID, name, age, address, LOAN_AMOUNT)
    values(4, 'Trump', 78, 'WD', 87654.45)
'''

pointer = connection.cursor()
pointer.execute(insert_sql_query)

connection.commit()
print('record is created')
connection.close()
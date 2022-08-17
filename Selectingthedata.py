import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'boondocs',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

table_select_query = '''
    select * from customer
'''
pointer = connection.cursor()
pointer.execute(table_select_query)
rows = pointer.fetchmany(3)       #fetch0ne #fetchall()
file = open('data.txt', 'w')
for each_row in rows:
    # print(each_row)
    # print(each_row[1], '------', each_row[-1])
    file.writelines(each_row[1])
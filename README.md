# PythonDatabasePG.py

Connect database

```
import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'boondocs',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)
print(connection)
```

Create table name Customer

```
connection = psycopg2.connect(
...
)

sql_query = '''
    CREATE TABLE Customer(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(100),
        LOAN_AMOUNT REAL
    )
'''
pointer = connection.cursor()
pointer.execute(sql_query)
connection.commit()
print("Table is created!")
```

validation code

```
import psycopg2
import logging

connection = psycopg2.connect(
...
)

table_customer_query = '''
...
    )
'''
pointer = connection.cursor()
try:
    pointer.execute(table_customer_query)
    connection.commit()
    logging.info("Table is created")
except Exception as e:
    logging.error("Table is duplicate ", e)
finally:
    pointer.close()
    connection.close()

```

# InsertData.py

```
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
```

# UpdateRecords.py

```
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
```

# Selectingthedata.py

```
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
rows = pointer.fetchall()
for each_row in rows:
    # print(each_row)
    print(each_row[1], '------', each_row[-1])
```

Create file and add data

```
pointer = connection.cursor()
pointer.execute(table_select_query)
rows = pointer.fetchmany(3)       #fetch0ne #fetchall()
file = open('data.txt', 'w')
for each_row in rows:
    # print(each_row)
    # print(each_row[1], '------', each_row[-1])
    file.writelines(each_row[1])
```

# DeleteRecord.py

```
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
```

Cr. : https://www.youtube.com/watch?v=d1atQKLFHgY

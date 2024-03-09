import sqlite3


## connect to SQLite 
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table
cursor=connection.cursor()

## create the table

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)


## Insert some more records

cursor.execute('''Insert Into STUDENT values('Shiva','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ram','Machine Learning','B',97)''')
cursor.execute('''Insert Into STUDENT values('Krishna','Artificial Intelligence','C',87)''')
cursor.execute('''Insert Into STUDENT values('Durga','Data Science','E',59)''')
cursor.execute('''Insert Into STUDENT values('Lakshmi','Charted Accounts','D',45)''')

## Display all the records


print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


## Commit your changes in the database
    
connection.commit()
connection.close()
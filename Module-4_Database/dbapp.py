import sqlite3

try:
    dbcon=sqlite3.connect("testdb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
"""tbl_create="create table studinfo(id int primary key, name text, sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)"""

# Insert Record
"""insert_data="insert into studinfo values(1,'sanket','python'),(2,'mitesh','angular'),(3,'hitesh','php'),(4,'ashok','ui-ux')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Record
"""update_data="update studinfo set sub='java' where id=2"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Record
"""delete_data="delete from studinfo where id=2"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Select Record
cur=dbcon.cursor()
select_data="select * from studinfo"
try: 
    cur.execute(select_data)
    #data=cur.fetchall()
    #data=cur.fetchmany(3)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)
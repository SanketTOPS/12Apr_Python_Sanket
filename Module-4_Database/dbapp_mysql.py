import pymysql
try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='topsdb')
    print("Database connected...!")
except Exception as e:
    print(e)


cur=dbcon.cursor()

# Table Create
tbl_create="create table studinfo(id int primary key, name text, sub text, city text)"
try:
    cur.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data

"""n=int(input("Enter number of students:"))

def insertData():
    for i in range(n):
        stid=input("Enter ID:")
        stnm=input("Enter Name:")
        stsub=input("Enter Subject:")
        stcity=input("Enter City:")

        insert_data=f"insert into studinfo values({stid},'{stnm}','{stsub}','{stcity}')"
        try:
            cur.execute(insert_data)
            dbcon.commit()
            print("Record inserted!")
        except Exception as e:
            print(e)

insertData()"""

# Update Data
"""update_data="update studinfo set city='Baroda' where id=102"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record Updated")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=104"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted")
except Exception as e:
    print(e)"""

# Show Data
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    #data=cur.fetchall()
    #data=cur.fetchmany(3)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)
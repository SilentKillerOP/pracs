import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

while True:
    i = int(
        input("ENTER 1 FOR INSERTION \n 2 FOR DELETION \n 3 TO SHOW DATA \n 4 TO EXIT:"))
    if i == 4:
        break
    elif i == 2:
        idd = int(input("ENTER ID:"))
        conn.execute(f'DELETE FROM COMPANY WHERE ID = {idd}')
    elif i == 1:
        id, name, age, loc, sal = (input().split())
        conn.execute(f"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES ({id}, {name}, {age},{loc} ,{sal})")
    else:
        cursor = conn.execute(
            "SELECT id, name,age , address, salary from COMPANY")
        for row in cursor:
            print(row)
    conn.commit()

conn.close()

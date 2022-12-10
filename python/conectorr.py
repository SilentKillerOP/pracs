import mysql.connector

constring = mysql.connector.connect(
    host='localhost', database='exp', user='root', password='Pass@123')
cursor = constring.cursor()
TABLES = {}
while(1):
    print("\nWelcome to database\n\nThe tables are: ")
    cursor.execute("Show tables")
    for table in cursor:
        print(table[0])
    print("\n1Create Table\n2)Insert into table\n3)Delete a row\n4)Display allrows\n5Update a row\n6Search a record\n7Exit")
    val = int(input("Your choice: "))
    print()
    if val == 1:
        string = input("Enter name of the table: ")
        print("It has 3 columns id, title, description")
        sql = f"Create table {string}(`id` int(5) not null auto_increment, `title` varchar(50),description` varchar(50), PRIMARY KEY(`id`)); "
        cursor.execute(sql)
        print("Table created successfully!")
    elif val == 2:
        string = input("Enter name of the table: ")
        tile = input("Enter the title: ")

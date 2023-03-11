from getpass import getpass
# from mysql.connector import connect, Error
import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="geolocation"
)

mycursor = db.cursor()

def create_db(name):
    mycursor.execute(f"CREATE DATABASE {name}")

mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()
for database in databases:
    print(database)

# mycursor.execute("CREATE TABLE location (id INT NOT NULL AUTO_INCREMENT, location VARCHAR(255), client VARCHAR(255), PRIMARY KEY (id))")
print("TABLES")
# query = "DROP TABLE location"
# mycursor.execute(query)
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()
for table in tables:
    print(table)


# query = "INSERT INTO location (location, client) VALUES (%s, %s)"
# ## storing values in a variable
# values = [
#     ("Nairobi, Kenya", "Peter"),
#     ("Accra, Ghana", "Amy"),
#     ("Fort Worth", "Michael"),
#     ("Khartoum", "Mennah"),
#     ("Times Tower", "KK"),
#     ("Eiffel Tower", "Kao"),
#     ("3129 Kingsley Drive, Pearland, Texas", "LABUSA"),
#     ("4419 Cedar Elm Ln, Manvel, TX", "Laster")
# ]

# query = "INSERT INTO location (location, client) VALUES (%s, %s)"
# values = [
#     ("njmhdflsg", "Gbrrzk"),
#     (" ", "Blank")
# ]

## executing the query with values
# mycursor.executemany(query, values)

# db.commit()

query = "SELECT * FROM location WHERE id>2 AND id<6"


## getting records from the table
mycursor.execute(query)

## fetching all records from the 'cursor' object
records = mycursor.fetchall()

## Showing the data
print("\n\n")
print("="*50)
print("TABLE RECORDS")
for id, location, user in records:
    print(location + "-->" + user)
# for record in records:
#     print(record)



# mycursor.execute("CREATE DATABASE ")

# try:
#     with mysql.connector.connect(
#         host="localhost",
#         user=input("Enter Username: "),
#         password=getpass("Enter password: "),
#     ) as connection:
#         print(connection)
# except OSError as e:
#     print(e)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dpatel",
  password="patel123",
  database="world"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM country where Name='India'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
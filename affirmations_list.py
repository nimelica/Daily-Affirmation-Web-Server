import sqlite3, requests

# Get data from the Mock API using GET HTTP method
# response data type will be byte

response = requests.get("https://mock-affirmations-api.herokuapp.com/affirmations")

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# Convert bytes into a JSON list data
affirmations = response.json()

# Create an empty database 
connection = sqlite3.connect('affirmations_list.db')

# communication with database via cursor with SQL commands
cursor = connection.cursor()

# Create table/s for our database
cursor.execute("create table drinks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Fill that table
for i in range(len(affirmations)):
  cursor.execute("insert into drinks (name) values (?)",[affirmations[i]])
  print("added to table->", affirmations[i])

# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()
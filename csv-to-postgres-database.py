import csv
import psycopg2

# Connect to an existing database
db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user': 'nagendraallam',
    'password': 'jPrSOy2EVw9b',
}

conn = psycopg2.connect(**db_params)

# create a table to store the data
cursor = conn.cursor()
# # Create a table to store the data (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS table_name
                  (id SERIAL PRIMARY KEY, word TEXT)''')

print("Table created successfully.")

with open('csv_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # if values are in row
    for row in csv_reader:
        print("adding row" + str(row))
        word = row[0]  # Assuming the word is in the first column
        cursor.execute("INSERT INTO table_name (word) VALUES (%s)", (word,))

    # if values are in column
    for column in csv_reader:
        print("adding column" + str(column))
        word = column[1]  # Assuming the word is in the first column
        cursor.execute("INSERT INTO table_name (word) VALUES (%s)", (word,))


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully.")

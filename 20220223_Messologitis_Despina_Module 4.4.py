import csv, sqlite3
import sys

conn_path = "C:/Users/dmessolo/OneDrive - Brown & Brown, Inc/Documents/COMP662/"
conn_filename = "customers.sqlite"
conn = sqlite3.connect(conn_path+conn_filename)
cur = conn.cursor()

import_filename = "customers.csv"

try:
    customers_import_file = open(import_filename)
except:
    print("No file found. Please add customers.csv to load the Customer table.")
    sys.exit()

records = csv.reader(customers_import_file)

records_list = list(records) #cast as a list to drop header row in file

try:
    # checks to see if the headers are in the first row; if they are, skip the first line on insert statement
    if records_list[0] == ['first_name', 'last_name', 'company_name', 'address', 'city', 'province', 'postal']:
        records_list = records_list[1:]
    else:
        records_list = records_list
except:
    print("No records in csv to import. Please update the customers.csv file.")
    sys.exit()

try:
    # delete the current records from the Customer table
    cur.execute("DELETE FROM Customer;")

    print("Customer Data Importer\n\n" +
          "CSV file:", import_filename, "\n" +
          "DB File:", conn_filename, "\n" +
          "Table name: Customer\n"
          )

    print("All old rows deleted from Customer table.\n")
except sqlite3.OperationalError:
    print("Database table doesn't exit. Review the data source.")
    sys.exit()

# insert records into the Customer table from the customers.csv import
cur.executemany("INSERT INTO Customer (firstName,lastName,companyName,address,city,province,postal) VALUES(?, ?, ?, "
                "?, ?, ?, ?);", records_list)

row_count = str(cur.execute("SELECT COUNT(*) FROM Customer;").fetchone()[0])

print(row_count, "row(s) inserted into Customer table.\n")

rows = cur.execute("SELECT * FROM Customer;")

title = [i[0] for i in cur.description] #gets the column names from the table
print(title)

rows = cur.fetchall()
for r in rows:
    print(r)

conn.commit()
conn.close()

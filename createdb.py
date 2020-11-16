# Database creation
import sqlite3

connector = sqlite3.connect("countries.db")  # Opening database connection
cur = connector.cursor()     # Creating a cursor object

# Creating database table and columns
create = """
    CREATE TABLE IF NOT EXISTS Covid (
    "Country,Other" TEXT,
    TotalCases TEXT,
    NewCases TEXT,
    TotalDeaths TEXT,
    NewDeaths TEXT,
    TotalRecovered TEXT,
    NewRecovered TEXT,
    ActiveCases TEXT,
    "Serious,Critical" TEXT
    )"""

cur.execute(create)     # Executing the creation with the cursor

connector.commit()      # Committing the creation to the database connection
connector.close()       # Closing the database connection

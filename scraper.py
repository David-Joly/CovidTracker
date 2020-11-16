# Script for scraping Covid-19 data from Worldometers.info
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3
import createdb

# Connecting to database so that information may be entered into it
connector = sqlite3.connect("countries.db")
cur = connector.cursor()

# Determines where to scrape the data from
html = requests.get('https://www.worldometers.info/coronavirus/').text
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.find_all('tr')


# Extracts all information contained in the websites table
def extract_text(row, tag):
    element = BeautifulSoup(row, 'html.parser').find_all(tag)
    text = [col.get_text() for col in element]
    return text


heading = rows.pop(0)
heading_row = extract_text(str(heading), 'th')[1:10]

# Organizes and saves the scraped data to a .csv file
with open('covid_data.csv', 'w') as f:
    f = csv.writer(f, delimiter=',')
    f.writerow(heading_row)
    for row in rows:
        data = extract_text(str(row), 'td')[1:10]
        f.writerow(data)

# Adds all data from the .csv file to a sqlite database
df = pd.read_csv('covid_data.csv', engine='python')
df = df.drop_duplicates(subset=['Country,Other'], keep='first')
df.to_sql('Covid', connector, if_exists='replace', index=False)
cur.close()
connector.close()




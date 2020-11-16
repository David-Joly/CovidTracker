"""
Covid-19 Data-Scraper
David Joly
Programming Language Research Project
"""

from tkinter import *
from datetime import datetime
import sqlite3
import pandas as pd
import scraper

# Database connection and cursor creation
connector = sqlite3.connect("countries.db")
cur = connector.cursor()

# Setting the height and width of the GUI window
HEIGHT = 600
WIDTH = 500


# Functions that allow the user to access specified data
def total_cases(country):  # Total cases
    country = entry.get()
    cur.execute('SELECT TotalCases FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())  # Fetching both specified row (country) and column (TotalCases) information from database
    s = ''.join(c for c in s if c not in '?:!/;)(')  # Removing extra symbols that are pulled from database
    f = s.replace("'", "").replace('"', '')  # Re-formatting the string for readability
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime(
        '%Y-%m-%d') + "\n\n" + country + "\n\nTotal Cases: " + result  # Displaying results in label box

    if result == "None":  # Displays alternate text if there are no results.
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere have been no Covid-19 cases in " + country


def new_cases(country):  # New cases
    country = entry.get()
    cur.execute('SELECT NewCases FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!+/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\n" + country + "\n\nNew Cases: " + result

    if result == "None":
        label['text'] = datetime.today().strftime(
            '%Y-%m-%d') + "\n\nThere are currently no new Covid-19 cases in " + country


def total_deaths(country):  # Total Deaths
    country = entry.get()
    cur.execute('SELECT TotalDeaths FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime(
        '%Y-%m-%d') + "\n\n" + country + "\n\nTotal Deaths: " + result

    if result == "None":
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere have been no Covid-19 deaths in " + country


def new_deaths(country):  # New Deaths
    country = entry.get()
    cur.execute('SELECT NewDeaths FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!+/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime(
        '%Y-%m-%d') + "\n\n" + country + "\n\nNew Deaths: " + result

    if result == "None":
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere are currently no new deaths in " + country


def total_recovered(country):  # Total Recoveries
    country = entry.get()
    cur.execute('SELECT TotalRecovered FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\n" + country + "\n\n" + "Total Recovered: " + result

    if result == "None":
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere have been no recoveries in " + country


def active_cases(country):  # Active Cases
    country = entry.get()
    cur.execute('SELECT ActiveCases FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!+/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime(
        '%Y-%m-%d') + "\n\n" + country + "\n\n" + "Active Cases: " + result

    if result == "None":
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere are no active cases in " + country


def serious_cases(country):  # Serious Cases
    country = entry.get()
    cur.execute('SELECT "Serious,Critical" FROM Covid WHERE "Country,Other"=? COLLATE NOCASE', (country,))
    connector.commit()
    s = str(cur.fetchone())
    s = ''.join(c for c in s if c not in '?:!/;)(')
    f = s.replace("'", "").replace('"', '')
    result = f.rstrip(',')
    label['text'] = datetime.today().strftime(
        '%Y-%m-%d') + "\n\n" + country + "\n\n" + "Patients in Critical Condition: " + result

    if result == "None":
        label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n\nThere are no serious cases in " + country


# Function that displays all stats for an entered country
def all_stats(country):
    df = pd.read_csv('covid_data.csv', engine='python')
    df = df.drop_duplicates(subset=['Country,Other'], keep='first')

    country = entry.get()
    info = {}
    for index, row in df.iterrows():
        if str.lower(row["Country,Other"]) == str.lower(country):
            info = row
            p = row.to_string()
            label['text'] = datetime.today().strftime('%Y-%m-%d') + "\n" + p


# Function that provides the user with options in a menu and activates specific functions dependant on their decision
def decision(x):
    if x == "Total Cases":
        total_cases(entry.get())
    elif x == "New Cases":
        new_cases(entry.get())
    elif x == "Total Deaths":
        total_deaths(entry.get())
    elif x == "New Deaths":
        new_deaths(entry.get())
    elif x == "Total Recovered":
        total_recovered(entry.get())
    elif x == "Active Cases":
        active_cases(entry.get())
    elif x == "Critical Condition":
        serious_cases(entry.get())
    elif x == "All Stats":
        all_stats(entry.get())


# Creation of the GUI
root = Tk()
root.title("Covid-19 Tracker | By: David Joly")  # Program title
root.iconbitmap('covid.ico')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Setting a background for the GUI
background_image = PhotoImage(file="covidBackground.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Frame placed behind entry
frame = Frame(root, bg='#000000', bd=5)
frame.place(relx=.36, rely=0.25, relwidth=0.5, relheight=0.1, anchor='n')

# Creates an area for users to enter a country name
entry = Entry(frame, font=40)
entry.place(relwidth=1, relheight=1)
entry.config(font="Arial 12 italic")

# Frame placed behind label
lower_frame = Frame(root, bg='#000000', bd=10)
lower_frame.place(relx=0.5, rely=.36, relwidth=.80, relheight=0.6, anchor='n')

# Creating a label where data is displayed
label = Label(lower_frame)
label.config(font="Arial 10 bold")
label.place(relwidth=1, relheight=1)

# Frame placed behind option menu
middle_frame = Frame(root, bg='#000000', bd=5)
middle_frame.place(relx=.74, rely=0.25, relwidth=0.31, relheight=0.1, anchor='n')

# Option menu contents
options = [
    "Total Cases",
    "New Cases",
    "Total Deaths",
    "New Deaths",
    "Total Recovered",
    "Active Cases",
    "Critical Condition",
    "All Stats"]
clicked = StringVar()
clicked.set(options[0])

# Creating option menu
drop = OptionMenu(middle_frame, clicked, *options, command=decision)
drop.config(bg='#2eab85', fg='white',
            activebackground='#ff8c00',
            activeforeground='black',
            font="Arial 10 bold")
drop.place(relwidth=1, relheight=1)

root.mainloop()  # End of program
connector.close()  # Closing database

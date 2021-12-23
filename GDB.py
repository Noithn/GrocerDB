import sqlite3
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')
dbname = 'groceries'
conn = sqlite3.connect(dbname + '.sqlite')

c = conn.cursor()

#This created the original database file.
#df = pd.read_csv('Groceries.csv')
#del df['#']
#df.info()
#df.to_sql(name='groceries', con = conn, if_exists='append', index=False)

##This was to try and rename columns with the CSV, and resave it as a SQLITE file
##Saving this for posterity so I can see my thought process, not the solution
#df.rename(columns={'item' : 0, 'Price':1, 'Type':2, 'Date':3}, inplace=True)
#df.to_csv('testing_col.csv', index=False)

##This space reserved for SQL commands - map to UI buttons
#c.execute('SELECT * FROM groceries WHERE item = "Kombucha" ')
#c.execute('SELECT * FROM groceries ')

#for row in c:
#    print(row)

#names = list(map(lambda x: x[0], c.description))
#print(names)

c.execute('SELECT item FROM groceries')
data = c.fetchall()
itemSelector = []
for row in data:
    itemSelector.append(row[0])
itemSelector.sort()
itemSelectorSort = []
for x in itemSelector:
    if x not in itemSelectorSort:
        itemSelectorSort.append(x)
#c.execute('SELECT date, price FROM groceries WHERE item LIKE "Tortillas" ')
#data = c.fetchall()

#item = []
#price = []
#date = []

#for row in data:
    #item.append(row[0])
#    price.append(row[1])
#    date.append(parser.parse(row[0]))
#sns.barplot(date, price)
#plt.show()
#c.close()
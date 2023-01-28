from datetime import datetime
import sqlite3
import matplotlib
import pandas as pd
import seaborn as sns
import numpy as np
import PyQt5.QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')
dbname = 'groceries'

#This created the original database file.
#df = pd.read_csv('Groceries.csv')
#del df['#']
#df.info()
#df.to_sql(name='groceries', con = conn, if_exists='append', index=False)

##This was to try and rename columns with the CSV, and resave it as a SQLITE file
##Saving this for posterity so I can see my thought process, not the solution
#df.rename(columns={'item' : 0, 'Price':1, 'Type':2, 'Date':3}, inplace=True)
#df.to_csv('testing_col.csv', index=False)


conn = sqlite3.connect(dbname + '.sqlite')

c = conn.cursor()
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
#Graphing function
def graphing(selected_item, start, end):
    # try:
    ###You need to have the dates as datetimes to have the query run
        c.execute("""SELECT date, price FROM groceries WHERE item = ? AND date BETWEEN ? AND ?;""", (selected_item[0],start,end))
        data = c.fetchall()
        #item = []
        price = []
        date = []
        for row in data:
            date.append(parser.parse(row[0]))
            price.append(row[1]) 
        dateFormat = []
        for date in date:
            dateFormat.append(datetime.strftime(date, '%y-%m-%d'))
        nameGraph = sns.barplot(dateFormat, price)
        nameGraph.set(xlabel = "Date", ylabel = "Price", title = "Groceries Over Time")
        # nameGraph.set_xticklabels(labels = dateFormat, rotation = 45)
        plt.show()
        # c.close()
        price.clear()
        date = 0
        dateFormat = 0
    # except:
    #     query_error = PyQt5.QtWidgets.QErrorMessage()
    #     query_error.showMessage('There was an error with the query')
import datetime
from dateutil.relativedelta import relativedelta
import urllib.request as urllib2
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

### Get today's day and one year before

today = datetime.date.today()
year_before = today + relativedelta(years = -1)


s_new=str(today)
date_new = s_new.split('-')
year_new = date_new[0]
month_new = date_new[1]
day_new =date_new[2]

s_old=str(year_before)
date_old = s_old.split('-')
year_old = date_old[0]
month_old = date_old[1]
day_old =date_old[2]

#print(year_new, year_old, month_new, month_old, day_new, day_old)

## acces web page

link = 'https://www.cursvalutar.ro/curs-eur/?curs_from_date='+day_old+'-'+month_old+'-'+year_old+'&curs_to_date='+day_new+'-'+month_new+'-'+year_new

## get the data from the html code


page = urllib2.urlopen(link)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table')
table_body = soup.find('tbody')
c = []
d = []
for td in table_body:
    for line in td:
        for item in line:
            c.append(item)
    d.append(c)
    c=[]

## create the data frame and delete the unnecessary info

a = DataFrame.from_records(d)
a.drop([0,2,4,5,6,7,8], axis = 1 , inplace=True)
a.rename(columns = {1:'Date',3:'Value'}, inplace=True)
b = a.replace(to_replace='None', value=np.nan).dropna()

c = b.reindex(index=b.index[::-1] )
c.reset_index(inplace = True)
c.drop(columns=['index'] , inplace= True)
date = c["Date"].tolist()
value = c["Value"].tolist()

##export the data to a .csv file

for item in c:
    c.to_csv('curs_euro.csv' , sep  = ",")

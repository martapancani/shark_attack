#!/usr/bin/env python
# coding: utf-8

# In[34]:


import csv
from datetime import datetime, timedelta
import pyodbc

sharkfile = r'c:\data\GSAF5.csv'

attack_dates = []
case = []
country = []
activity = []
age = []
gender = []
isfatal = []

with open(sharkfile, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        case.append(row['Case Number'])
        attack_dates.append(row['Date'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        gender.append(row['Sex '])
        age.append(row['Age'])
        isfatal.append(row['Fatal (Y/N)'])

data = zip(attack_dates, case, country, activity, age, gender, isfatal)
conn = pyodbc.connect('DSN=kubricksql;UID=DE14;PWD=password')
cur = conn.cursor()
cur.execute('truncate table marta.shark')
query = 'insert into marta.shark (attack_date, case_number, country, activity, age, gender, isfatal) values (?,?,?,?,?,?,?)'  
# ? = parameter placeholder
# p = ['2019-10-30', 'dummy123', 'UK', 'snorkeling', 41, 'M', 1]


# In[ ]:


for d in data:
    try:
        cur.execute(query,d)  # d becomes the list of parameters that are used instead of the ?'s
        conn.commit()
    except:
        conn.rollback()


# isfatal[:10]
# attack_dates[:20]

# clean_dates = []
# for a in range(0,len(attack_dates)):
#     if (attack_dates[a].isnumeric() & len(attack_dates[a]==4)):
#         try:
#             clean_dates.append(datetime.strptime('01-Jan-'+clean_dates[a], '%d-%b-%Y'))
# #             clean_dates[a] = datetime.strptime(clean_dates[a], '%d-%b-%Y')
# #             clean_dates[a] = clean_dates[a].strftime('%d-%b-%Y')
#         except:
#             pass
#     elif:
#         try:
#             clean_dates.append(attack_dates[a].replace('Reported ', ''))
#             clean_dates[a] = datetime.strptime(clean_dates[a], '%d-%b-%Y')
#             clean_dates[a] = clean_dates[a].strftime('%d-%b-%Y')
#         except:
#             pass


# datecount = {}
# for d in clean_dates:
#     datecount[d] = datecount.get(d,0)+1

# sorted(datecount.items(), key=lambda x: x[1], reverse=True)






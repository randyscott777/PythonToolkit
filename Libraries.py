'''
Python Libraries 

os: path TBD, getcwd() TBD, mkdir() TBD, listdir TBD, open? TBD
sys:
builtins:
datetime: date, now, strftime
collections: namedtuple(), Counter, defaultdict 
functools: reduce, partial TBD
itertools: count TBD, product TBD, permutations, combinations 
math: Eucler,pi,factorial,floor,gcd,log,log10,sqrt,sin
random: random, randint, choices, shuffle
RegEx: TBD
numpy: arange, reshape
pandas: pd.DataFrame(data)
sqlite3: TBD
matplotlib: pyplot
Scikit-learn: TBD
Requests: response = request.get(url)
BeautifulSoup: TBD
Pygame: TBD
flask: Flask, app.route('/'), app.run()
Django: TBD
Scrapy: TBD
Pytest: TBD
'''
print(__doc__)
print('----------- from datetime library --------')
from dataclasses import dataclass
from datetime import date 
date1 = date.today()
print('Today''s date is',date1)
import datetime as dt
print('Now datetime is',dt.datetime.now())
date2 = dt.date(2030,1,1)
print('Create date of 1/1/2030 is',date2)
print('Date difference between now and 1/1/30 in days is',(date2 - date1).days)
print('Now in mm/dd/yyyy format is',date1.strftime('%m/%d/%Y'))

print('\n---- from collections library ------')
from collections import namedtuple, Counter, defaultdict
# Named tuples
Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person('Alice', 30, 'New York')
print('Named tuple for person is',p.name)  # Output: Alice
# Counter (which sorts descending by value)
ctr = Counter('abrxcxdxbrx').most_common(3)
print('Top 3 counter of abrxcxdxbrx is:',ctr)
# defaultDict 
dftDict = defaultdict(int) # dft value for an int is 0
dftDict['a'] += 1; dftDict['b'] += 1; dftDict['a'] += 1
print('The dft dict for value c is',dftDict['c']) 
print('The dft dict is',dftDict)

print('\n---- from functtools library ------')
from functools import reduce
list1 = [2,4,7,9,1,3]
print('For 2,4,7,9,1,3 reduce to it''s sum',reduce(lambda a,b: a + b, list1))
list2 = ['a','x','c','s']
print('For a,x,c,s reduce to it''s highest value',reduce(lambda a,b: a if a>b else b, list2))

print('\n---- from itertools library ------')
from itertools import combinations, permutations
items = [1,2,3]
print('For 1,2,3, then combos of 2 are',list(combinations(items,2)))
print('For 1,2,3, then permutations of 2 are',list(permutations(items,2)))

print('\n---- from math library ------')
import math
print('Euler''s number is',math.e)
print('Pi is',math.pi)
print('The factorial of a 4 is',math.factorial(4))
print('The floor of 4.99 is',math.floor(4.99))
print('The greatest commmon divisor of 8 and 12 is',math.gcd(8,12))
print('Logarithmic value of 4 with a base 2 is',math.log(4,2))
print('Logarithmic value of 12 with a base 10 is',math.log10(12))
print('Square root of 49 is',math.sqrt(49))
print('Sine of 30 is',math.sin(30))

print('\n---- from random library ------')
import random
print('A random floating point number betwween 0 and 1 is',random.random())
print('A random integer betwween 1 and 100 is',random.randint(1,100))
list1to9 = list(range(10))
random.shuffle(list1to9) # Note: does in place
print('A random shuffling of 1 thru 9 is',end=' ')
for x in list1to9: print(x,end=' ')
print('\nA choice within the list a,e,i,o,u is',random.choice(['a','e','i','o','u']))

print('\n---- from numpy library ------')
import numpy as np
mtx = np.arange(15).reshape(3,5)
print('Numpy arange(15).reshape(3,5) is\n',mtx)

print('\n---- from pandas library ------')
import pandas as pd
data = {'Names':['Randy','Donna'],'Ages':[75,71]}
df = pd.DataFrame(data)
print(df)

print('\n---- from sqlite3 library ------')
import sqlite3 
conn = sqlite3.connect('movies.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS movie")
cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
conn.commit()
records = cur.execute("SELECT * FROM movie").fetchall()
for rcd in records: print(rcd)

print('\n---- from matplotlib library ------')
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

print('\n---- from requests library ------')
import requests
response = requests.get('https://raw.githubusercontent.com/randyscott777/PythonToolkit/main/README.md')
if response.status_code == 200:
    print(response.text)
else:
    print('Error, not found')    

print('\n---- from flask library ------')
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()
    

# Snippets of code not using any libraries
'''
SNIPPETS OF CODE

# Execute code from another module
with open("module_name.py") as f:
        code = f.read()
    exec(code)

----------------- List Snippets --------------------------

# List comprehension with filtering
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]

# Count occurrences of an element in a list
text = "Hello, World!"
count = text.count('llo')

# Find highest frequency element - TODO> max 2nd arg of key and list.count?
my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
print("Most frequent item:", max(set(my_list), key=my_list.count))

# Merge 2 or more lists into a list of lists
def merge(*args, missing_val = None):
    # Missing_val will be used when one of the smaller lists is shorter tham the others.
    # Get the maximum length within the smaller lists.
    max_length = max([len(lst) for lst in args])
    outList = []
    for i in range(max_length):
        outList.append([args[k][i] if i < len(args[k]) else missing_val for k in range(len(args))])
    return outList
    
# Flatten a list
ugly_list = [10,12,36,[41,59,63],[77],81,93]
flat = []
for i in ugly_list:
    if isinstance(i, list): flat.extend(i)
    else: flat.append(i)

# Remove an element where there are multiple occurrences
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits = [x for x in fruits if x != 'banana']

# Deep copy (needs from copy import deepcopy')
from copy import deepcopy
list1 = [1,2,3,4,5]
list2 = list1
list2.reverse()
print('list2=list1 (shallow copy), list2.reverse(), list1 is',list1)
list3 = deepcopy(list1) # which list1 is now 5,4,3,2,1
list3.sort()
    
# Transpose a nested list into list of tuples
my_list=[[1,2,3],[4,5,6]]
print('For [[1,2,3],[4,5,6]], transposed is',list(zip(*my_list)))
    
# Using map and lambda to add corresponding items in 2 lists')
list1=[1,2,3]
list2=[4,5,6]
list3 = map(lambda x,y: x+y,list1,list2)
  
# Using map and lambda to convert list of celsius to fahrenheit')
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)

------------------------ String List Snippets ---------------------------

# Sort a list of strings
my_list = ["blue", "red", "green"]
my_list.sort() #sorts alphabetically or in an ascending order for numeric data 
my_list = sorted(my_list, key=len) #sorts the list based on the length of the strings from shortest to longest. 

# Reversing a strings
string = "Python"
reversed_string = string[::-1]

# Convert list to string
items = ['apple', 'banana', 'cherry']
result = ', '.join(items)

# Split a string into characters
text = "Hello, World!"
characters = text.split('')

# Check if string contains only digits
text = "12345"
if text.isdigit(): print("The string contains only digits.")

# Check for substrings
addresses = ["123 Elm Street", "531 Oak Street", "678 Maple Street"]
street = "Elm Street"
for address in addresses:
    if street in address:
        print(address)
        
# Replace substring in string
text = "Hello, World!"
new_text = text.replace('Hello', 'Hi')

----------------- Dict Snippets --------------------------

# Dict comprehension
myDict = { k:v for (k,v) in zip(keys, values) }  
    
# Create a dict from 2 lists 
dict = dict(zip(keys, values))

# Create a dict where there are missing values: dict.get(key)')
dict2 = {'0' : '101', '1' : '102', '2' : '100', '4' : '100.5', '6' : '103'}
keys = ['0','1','2','3','4','5','6','7']
for k in keys:
    dict2[k] = dict2.get(k) # get(k) returns None if not found

# Counter of occurrences
def count_by(arr, fn=lambda x: x):
    counter = {}
    for elm in map(fn, arr):
        if elm not in counter:
            counter[elm] = 0 # incremented below
        counter[elm] += 1
    return counter
countsDict = count_by([1,2,3,4,4,3,2,2,1])
   
# Sort a list of dicts
persons.sort(key=lambda item: item.get("Age"))
or
persons = sorted(persons, key=lambda item: item.get("id"))

# Sort a dict by value
sort_dict = dict(sorted(dict.items(), key=lambda item: item[1])) 

# Map a list into a dict
my_list = [1, 2, 3, 4]
my_dict = dict(zip(my_list, map(lambda x: x**2, my_list)))
print(my_dict)

# Merge 2 or more dicts
my_dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
my_dict2 = {'d' : 4, 'e' : 5, 'f' : 6}
result = { **my_dict1, **my_dict2}
print(result)

# Enumerate a dictionary
my_dict = {'a' : 'one', 'b' : 'two', 'c' : 'three'}
for index,(key,value) in enumerate(my_dict.items()):
    print(index,key,value)
      
#Transpose a dictionary into list of keys and list of values')
my_dict = {'a' : 'one', 'b' : 'two', 'c' : 'three'}
print(list(zip(*my_dict.items())))
  
----------------- Tuple Snippets ------------------------------

# Swap values in 2 variables
a, b = 5, 10
a, b = b, a

# Sorting a list of tuples
tuples = [(2, 'banana'), (1, 'apple'), (3, 'cherry')]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
  
----------------- Set Snippets ------------------------------

# Check if a list has duplicates
def check_for_duplicates(input):
    return len(input) != len(set(input))
    
# Remove duplicates from a list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))    

print("\nSET check if all chars of 'hellx' is contained in other 'World, hello!")
list1 = list("hellx")
list2 = list("World, hello!")
good = set(list1).issubset(list2)
if good: print("All chars in substring are contained in the main string")
else: print('Not all chars in substring are in the main string')

print("\nSET check if any char in 12x34 is bad (not in '$0123456789.,)")
number = "12x34"
master = "$0123456789.,"
good = set(number).issubset(master)
if not good:print("The number contains bad char")
else: print('All chars are valid')


------------------- File Handling Snippets ---------------------------
        
# Check if a file exists
import os 
exists = os.path.isfile('/path/to/file')

# Open a file
f = open('filename.txt')

# Read from a file
f = open('filename.txt', 'r')

# To read the whole file
print(f.read())

# Read who;e file stripping whitespace and newline
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())

# To read single line
print(f.readline())

# Write to a file
f = open('filename.txt', 'w')
f.write('Writing into a file \n')

# Closing a file
f.close()

# Write JSON data to a file
import json
def write_json_to_file(data, filename):
	with open(filename, "w") as f:
		json.dump(data, f, indent=4) 

# Read a JSON file
import json
def read_json_from_file(filepath):
	with open(filepath, "r") as f:
    data = json.load(f) 
    
----------------- Decorator Snippets ----------------------
    
# Singleton decorator
def singleton(myClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return getInstance
@singleton
class TestClass(object):
	pass 

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times=3)
def greetName(name):
    print(f"Hello, {name}!")
greetName("Alice 3x")        

'''

from pickletools import string1


print(__doc__)

print('----------------- List Snippets --------------------------')

print('\nList comprehension with filtering - even numbers in range 0 to 19')
even_numbers = [n for n in range(20) if n % 2 == 0]
print(even_numbers)

print('\nList comprehension with lookups - [ch1 in str2 for ch1 in str1]')
str1 = "hellx"
str2 = "Hello world!"
bools = [ch1 in str2 for ch1 in str1]
print("Is 'hellx' in 'Hello world!'",bools)

print('\nList comprehension with 2 iterables - [(x, y) for x in range(3) for y in range(3)]')
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

print('\nList comprehension to flatten a matrix - [val for row in matrix for val in row]')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [val for row in matrix for val in row]
print(result)

print('\nList comprehension to produce tuples without duplicates - [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]')
combos = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combos)

print('\nCount occurrences of an element in a list - llo in Hello World!')
text = "Hello, World!"
count = text.count('llo')
print(count)

print('\nFind highest frequency element in [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]')
print('TODO: why max 2nd arg of key and list.count?')
my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
print("Most frequent item:", max(set(my_list), key=my_list.count))

print('\nMerge 2 or more lists into a list of lists')
def merge(*args, missing_val = None):
    # Missing_val will be used when one of the smaller lists is shorter tham the others.
    # Get the maximum length within the smaller lists.
    max_length = max([len(lst) for lst in args])
    outList = []
    for i in range(max_length):
        outList.append([args[k][i] if i < len(args[k]) else missing_val for k in range(len(args))])
    return outList
print(merge(['a','b','c','d'],[1,2,3]))
    
print('\nFlatten a list [10,12,36,[41,59,63],[77],81,93]')
ugly_list = [10,12,36,[41,59,63],[77],81,93]
flat = []
for i in ugly_list:
    if isinstance(i, list): flat.extend(i)
    else: flat.append(i)
print(flat)

print('\nRemove an element inplace if any multiple occurrences')
fruits = ['apple', 'banana', 'cherry', 'banana']
print('Where fruits id',fruits)
fruits = [x for x in fruits if x != 'banana']
print('Fruits now is',fruits)

print('\nDeep copy needs to create new,  but not from assignment')
list1 = [1,2,3,4,5]
list2 = list1
list2.reverse()
print('list2=list1 (shallow copy), list2.reverse(), note: list1 is',list1)
list3 = [n for n in list1] # deepcopy(list1) where list1 is now 5,4,3,2,1
list3.sort()
print('list3=[n for n in list1] and then list3.sorted is',list3)
print('Note: list1 was untouched on deep copy/create',list1)
    
print('\nTranspose a nested list into list of tuples')
my_list=[[1,2,3],[4,5,6]]
print('For [[1,2,3],[4,5,6]], transposed is',list(zip(*my_list)))
    
print('\nUsing map and lambda to add corresponding items in 2 lists')
list1=[1,2,3]
list2=[4,5,6]
list3 = map(lambda x,y: x+y,list1,list2)
print('For [1,2,3] and [4,5,6], map(lambda x,y: x+y,list1,list2) is',list(list3))
  
print('\nUsing map and lambda to convert list of celsius to fahrenheit')
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))

print('\n------------------ String List Snippets ---------------------------')

print('Sort a list of strings')
my_list = ["blue", "red", "green"]
my_list.sort() #sorts alphabetically or in an ascending order for numeric data 
my_list = sorted(my_list, key=len) #sorts the list based on the length of the strings from shortest to longest. 
print(my_list)

print('Reversing a strings')
string = "Python"
reversed_string = string[::-1]
print(reversed_string)

print('Convert list to string')
items = ['apple', 'banana', 'cherry']
result = ', '.join(items)
print(result)

print('Split a string into characters')
text = "Hello, World!"
characters = list(text) # text.split('')
print(characters)

print('Check if string contains only digits')
text = "12345"
if text.isdigit(): print("The string contains only digits.")

print('Check for substrings')
addresses = ["123 Elm Street", "531 Oak Street", "678 Maple Street"]
street = "Elm Street"
for address in addresses:
    if street in address:
        print(address)
print(addresses)
        
print('Replace Hello with substring Hi in string Hello, World!')
text = "Hello, World!"
new_text = text.replace('Hello', 'Hi')
print(new_text)

print("\nCheck if ALL chars of 'hellx' is contained in other 'World, hello!")
str1 = "Hello"
str2 = "Hello world!"
good = all(ch in str2 for ch in str1)
if good: print(f"All chars in {str1} are contained in {str2}")
else: print(f'Not all chars in {str1} are in {str2}')

print("\nCheck if ANY char in 12x34 is bad (not in '$0123456789.,)")
number = "12x34"
valids = "$0123456789.,"
bad = any([ch not in valids for ch in number])
if bad:print(f"The number {number} contains a bad char")
else: print(f'All chars in {number} are valid')

print('\n----------------- Dict Snippets --------------------------')

print('\nFor dict comprehension: {x: x**2 for x in range(10)}')
print('The number and squares are:',{x: x**2 for x in range(10)})
keys = ['a','b','c'] 
values = [1,2,3]
myDict = {k:v for (k,v) in zip(keys, values)} 
print('For {k:v for (k,v) in zip(keys, values)}',myDict)
   
print('Create a dict from 2 lists: dict(zip(keys, values)')
dict1 = dict(zip(keys, values))
print(dict1)
  
print('Create a dict where there are missing values: dict.get(key)')
dict2 = {'0' : '101', '1' : '102', '2' : '100', '4' : '100.5', '6' : '103'}
keys = ['0','1','2','3','4','5','6','7']
for k in keys:
    dict2[k] = dict2.get(k) # get(k) returns None if not found
print(dict2)

print('\nLike Counter in collections, count of occurrences')
def count_by(arr, fn=lambda x: x):
    counter = {}
    for elm in map(fn, arr):
        if elm not in counter:
            counter[elm] = 0 # incremented below
        counter[elm] += 1
    return counter
countsDict = count_by([1,2,3,4,4,3,2,2,1])
print('For 1,2,3,4,4,3,2,2,1',countsDict)
   
print('\nSort a list of dicts: persons.sort(key=lambda item: item.get("age"))')
persons = [{'id':2,'name':'Randy','age':75},{'id':1,'name':'Donna','age':71}]
persons.sort(key=lambda item: item.get("age"))
print('sort inplace',persons)
persons = sorted(persons, key=lambda item: item.get("id"))
print('result = sorted',persons)

print("Sort a dict by value - {'a': 3, 'b': 1, 'c': 2}")
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1])) 
print('Sorted by value/item[1]',sorted_dict)

print('\nMap a list into a dict using indices as keys')
my_list = ['apple', 'banana', 'cherry']
my_dict = {index: value for index, value in enumerate(my_list)}
print(my_dict)

print('\nMerge 2 or more dicts')
my_dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
my_dict2 = {'d' : 4, 'e' : 5, 'f' : 6}
result = { **my_dict1, **my_dict2 }
print(result)

print('\nEnumerate a dictionary')
my_dict = {'a' : 'one', 'b' : 'two', 'c' : 'three'}
for index,(key,value) in enumerate(my_dict.items()):
    print(index,key,value)
    
print('\nTranspose above dictionary into list of keys and list of values')
my_dict = {'a' : 'one', 'b' : 'two', 'c' : 'three'}
print(list(zip(*my_dict.items())))

print('\n----------------- Tuple Snippets ------------------------------')

print('Swap values in 2 variables')
a, b = 5, 10
a, b = b, a
print('Where a,b=5,10 and a,b = b,a is:',a,b)

print("Sorting a list of tuples [(2, 'banana'), (1, 'apple'), (3, 'cherry')]")
tuples = [(2, 'banana'), (1, 'apple'), (3, 'cherry')]
sorted_tuples = sorted(tuples, key=lambda x: x[0])
print('Sorted by 1st element',sorted_tuples)

print('\n----------------- Set Snippets ----------------------')

print('\nCheck if a list [1, 2, 2, 3, 4, 4, 5] has duplicates')
def check_for_duplicates(input):
    return len(input) != len(set(input))
print(check_for_duplicates([1,2,3,4,1]))
    
print('\nRemove duplicates from a list [1, 2, 2, 3, 4, 4, 5]')
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(unique_items)

print("\nUsing issubset, check if all chars of 'hellx' is contained in other 'World, hello!")
list1 = list("hellx")
list2 = list("World, hello!")
good = set(list1).issubset(list2)
if good: print("All chars in substring are contained in the main string")
else: print('Not all chars in substring are in the main string')

print("\nUsing issubset, check if any char in 12x34 is bad (not in '$0123456789.,)")
number = "12x34"
valids = "$0123456789.,"
good = set(number).issubset(valids)
if not good:print("The number contains bad char")
else: print('All chars are valid')

print("\nSet operators, where a=set('abracadabra') and b=set('alacazam')")
a=set('abracadabra')
b=set('alacazam')
print('a - b (in a but not b)',a-b)
print('a | b (in either a or b)',a|b)
print('a ^ b (in a or b, but not both)',a^b)
print('a & b (in both a and b)',a&b)

print("\nSet comprehension - {x for x in 'abracadabra' if x not in 'abc'}")
x = {x for x in 'abracadabra' if x not in 'abc'}
print(x)

print('\n-------------- File Handling Snippets ---------------------------')

print('\ntbd - see docstring')
  
print('\n----------------- Decorator Snippets ----------------------')
    
print('Singleton decorator')
def singleton(cls):
	instances = {}
	def getInstance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return getInstance
@singleton
class TestClass:
    def __init__(self):  
	    print('Initializing TestClass')       
t1 = TestClass()
t2 = TestClass()
print('t1 is t2',t1 is t2)

def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@simple_decorator
def greet():
    print("Hello, world!")
greet()

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
@repeat(num_times=3)
def greetName(name):
    print(f"Hello, {name}!")
greetName("Alice 3x")



   

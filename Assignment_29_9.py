"""
Write a Python script to store book data in a file. 
Book data is in the form of a dictionary in which book 
name is the key and price is its value. Use pickle to store
data into a file (say bookfile) 
"""

import pickle
book = {'Python' : 100, 'Java' : 200, 'Javascript' : 300, 'CPP' : 400}
f = open('bookfile.py', 'ab')
pickle.dump(book, f)
f.close()

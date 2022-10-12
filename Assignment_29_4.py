"""
Write a Python script to store a list of city names 
in a file cities.txt
"""

def writing(filename, text1):
    with open(filename, 'w') as c:
        c.write(text1)

writing('cities.txt', 'Surat')

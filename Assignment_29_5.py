"""
Write a Python script to append list of city names 
in a file cities.txt
"""

def writing(filename, text1):
    with open(filename, 'w') as c:
        c.write(text1)

writing('cities.txt', 'Surat')


def append(filename, txt):
    with open(filename, 'a') as city_list:
        city_list.write(txt)
    
append('cities.txt', ' , Delhi')
append('cities.txt', ' , Kolkata')
append('cities.txt', ' , Jodhpur')

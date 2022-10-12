"""
Write a Python script to search whether a particular city is there 
in the file cities.txt or not
"""

def serch(filename, city_name):
    try:
        f = open(filename, 'r')
        if city_name in f.read():
            print()
            print("Yes city exist in cities.txt file")
            print()
        else:
            print()
            print("No city is not exist in cities.txt file")
            print()
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()
serch('cities.txt', 'Ajmer')

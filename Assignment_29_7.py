def count(filename):
    import keyword
    y = keyword.kwlist
    print()
    # print(y)
    print()
    try:
        f = open(filename, 'r')
        r = f.readlines()
        print(r)
        print()
        c = 0
        for line in r:
            l1 = line.split(' ')
            for e in l1:
                if e in y:
                    c += 1
        print("Count is:",c)
        print()
    except FileNotFoundError:
        print("File not found")
        print()
    finally:
        f.close()
count('Assignment_29_6.py')

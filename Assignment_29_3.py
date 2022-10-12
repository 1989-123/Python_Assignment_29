
def writing(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

writing('myfile.txt', 'My trible chif')


def reading(filename):
    try:
        f = open(filename, 'r')
        txt = f.read()
        print()
        print(txt)
        print()
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()

reading('myfile.txt')

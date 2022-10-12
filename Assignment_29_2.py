def writing(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

writing('myfile.txt', 'My trible chif')

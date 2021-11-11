try:
    with open('E:\\Github\\Introducao-python-brocode\\Python\\Aulas 31-40\\Aula 32\\text.txt') as file: 
        print(file.read())
        file.close()
        print(file.closed)
except FileNotFoundError:
    print("That file was not found.")
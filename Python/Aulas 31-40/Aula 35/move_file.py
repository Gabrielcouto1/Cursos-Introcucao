import os

source = "test.txt"
destination = "E:\\Github\\Introducao-python-brocode\\Python\\Aulas 31-40\\Aula 35"

try:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + "was not found")
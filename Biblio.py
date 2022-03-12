import csv
from statistics import mode

with open('Libros.csv', 'r') as libro:
    libro_reader = csv.reader(libro)   # list of everything on the Libros file

    for line in libro_reader:
         libros = list(line)

with open('autores.csv', 'r') as author:
    author_reader = csv.reader(author)  # list of autores file

    for line in author_reader:
        authors = line

directorio = list(zip(libros, authors))  # list of tuples

# Functions


def prestamo(libro, autor, dia, fecha):

    check = (libro, autor)

    for x in directorio:

        if check == x:
            presto = (libro, autor, dia, fecha)
            with open('prestamos.csv', 'a', newline="") as presta:   # adding elements to the csv file
                writer = csv.writer(presta)
                writer.writerow(presto)
                return True


def tot_libros(autor):

    cont = 0

    with open('prestamos.csv', 'r') as presta:
        presta_reader = csv.DictReader(presta)

        for line in presta_reader:
            if autor == line['autor']:
                cont += 1

        return cont


def dia_mas_presta():

    dias = []

    with open('prestamos.csv', 'r') as prestamous:
        presta_reader = csv.DictReader(prestamous)

        next(presta_reader)

        for line in presta_reader:
            x = line['dia']
            dias.append(x)

    mas = mode(dias)

    return mas


def autor_mas_soli():

    autor_mas = []

    with open('prestamos.csv', 'r') as prestamous:
        author_read = csv.DictReader(prestamous)

        next(author_read)

        for line in author_read:
            x = line['autor']
            autor_mas.append(x)

    mas = mode(autor_mas)

    return mas


def libro_mas_soli():

    lib_mas = []

    with open('prestamos.csv', 'r') as libs:
        lib_reader = csv.DictReader(libs)

        next(lib_reader)

        for line in lib_reader:
            x = line['libro']
            lib_mas.append(x)

    mas = mode(lib_mas)

    return mas

# info functions

def libros():
    with open('Libros.csv', 'r') as libro:
        libro_reader = csv.reader(libro)  # list of everything on the Libros file

        for line in libro_reader:
            libros = line
        print(libros)

def autores():
    with open('autores.csv', 'r') as author:
        author_reader = csv.reader(author)  # list of autores file

        for line in author_reader:
            authors = line
        print(authors)



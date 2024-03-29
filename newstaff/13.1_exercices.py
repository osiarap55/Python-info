# Explain the difference between map, filter, and reduce

# map es usado para transformar los elementos de una lista en otros, su sintaxis en (funcion, lista)
# filter es usado para filtrar la lista segun una funcion como por ejemplo los numeros pares de una lista, su sintaxis es igual a la de map.
# reduce esta en el modulo functools, es usado como dice el propio nombre para reducir la lista en un unico valor, por ejemplo la suma de todos los numeros de una lista.

# ejemplo map
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

# ejemplo reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# ejemplo filter
numbers = [1, 2, 3, 4, 5, 6, 7]
def even_numbers_func(num):
    if num % 2 == 0:
        return True
    else:
        return False
even_numbers = filter(even_numbers_func, numbers)
print(list(even_numbers))

# Explain the difference between higher order function, closure and decorator

# higher order function es aquella que toma una o mas funciones como argumentos o devulve una funcion como resultado, se usa para pasar funciones como parametros, devilver funciones desde otras funciones y almacenar funciones en estructura de datos.
# closure es un objeto de funcion que tiene acceso a variables en su ambito lexico, incluso cunado la funcion se llama fuera de su ambito. Esto permite una forma de encapsulacion de datos, se utiliza para crear variables privadas o para mantener el estado en la programacion funcional. Los cierres o closures se crean cuando una funcion anidada hace referencia a unaw variable de us funcion contenedora.
# Decorator es un tipo especial de funcion se utiliza para cambiar el comportamiento de otras funciones. Los decoradores se aplican mediante la sintaxis @decorador en python. Permiten envolver o modificar la funcionalidad de una funcion si cambiar su codigo.  Los decoradores se utilizan comúnmente para tareas como el registro, la memorización, el control de acceso o la instrumentación de código.


# ejemplo closure funcion
def funcion_ext(x):
    def funcion_int(y):
        return x + y
    return funcion_int

ejemplo_de_cierre = funcion_ext(10)
print(ejemplo_de_cierre(5)) 


# ejemplo Decorator
def mi_decorador(func):
    def envoltura():
        print("Algo esta sucediendo enates de llamar a la función")
        func()
        print("Algo esta sucediendo despues de llamar a la función")
    return envoltura

@mi_decorador
def decir_hola():
    print("hola")

decir_hola()

# ejercicio 4

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

# ejercicio 5

for name in names:
    print(name)

# ejercicio 6

for number in numbers:
    print(number)

# ejecrcio 7

def upper_case(country):
    country = country.upper()
    return country
upper_case_map = map(upper_case, countries)
print(list(upper_case_map))

# ejercia 8

def squared_numbers_1(num):
        return num ** 2
squred_num_map = map(squared_numbers_1, numbers)
print(list(squred_num_map))

# ejercia 9

def upper_case_name(name):
    name = name.upper()
    return name
upper_case_name_1 = map(upper_case_name, names)
print(list(upper_case_name_1))

# ejercicio 10

def add_land_end(country):
    if "land" in country:
        return True
    else:
        return False
add_land_country = filter(add_land_end, countries)
print(list(add_land_country))

# ejercico 11

def filter_len_6(country):
    if len(country) <= 6:
        return True
    else:
        return False
len_6_countries = filter(filter_len_6, countries)
print(list(len_6_countries))

# ejercicio 11

def starting_countries_with_E(country):
    if country.startswith("E"):
        return True
    else:
        return False
starting_function = filter(starting_countries_with_E, countries)
print(list(starting_function))

#ejercico level 3

from countriesss import countriesss 

def sort_countries(parameter):
    return lambda country: country[parameter]
        
sort_by_name = sorted(map(lambda country: country["name"], countriesss))
print(sort_by_name)

sort_by_capital = sorted(map(lambda country: country["capital"], countriesss))
print(sort_by_capital)

sort_by_population = sorted(map(lambda country: country["population"], countriesss))
print(sort_by_population)
                    
sort_by_all = sorted(map(lambda country: (country["name"], country["capital"], country["population"]), countriesss))
print(sort_by_all)

# ejercicio level 3 / 1

from functools import reduce
from collections import Counter
import time

all_language = map(lambda country1: country1["languages"], countriesss)
all_language_flat = reduce(lambda x, y: x + y, all_language)
languages_counter = Counter(all_language_flat)
top_languages = languages_counter.most_common(10)

print("Ten most spoken languges by location:")
for language, count in top_languages:
    print(f"{language}: {count} countries")


#all_language = map(lambda country: country["languages"], countriesss)
#flat_list = reduce(lambda x, y: x + y, all_language)
#print(flat_list)
#print(languages_counter)

# ejercicio level 3 / 2

time.sleep(2)

sorted_countries = sorted(countriesss, key=lambda x: x['population'], reverse=True)

print("Ten most populated countries: ")
for country in sorted_countries[:10]:
    print(f"{country['name']} - Population: {country['population']}")


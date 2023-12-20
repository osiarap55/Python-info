# Primer ejercicio

empty_tuple = tuple()

tuple_fammily = ("mavi", "Sara", "javi", "Guille")
print(tuple_fammily)

sisters = (tuple_fammily[0:2])
print(sisters)
brothers = (tuple_fammily[2:])
print(brothers)
siblings = sisters + brothers
print(siblings)

print(len(siblings))

lista_temporal = list(siblings)
print(lista_temporal)
mis_padres = ["Javier", "Mavi"]
mi_familia = lista_temporal + mis_padres
print(mi_familia)
mi_familia = tuple(mi_familia)
print(type(mi_familia))
print(mi_familia)

# Segundo ejercicio

mis_padres = mi_familia[-2:]
siblings = mi_familia[:3]
print(mis_padres)
print(siblings)







employee_file = open("leer_archivos_ej.txt", "r+")

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.read())


employee_file.close()

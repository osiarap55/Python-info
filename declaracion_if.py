#condicional or = o uno o otro o los dos
is_male = False
is_tall = True

if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you neither male nor tall")

#condicional and = o los dos son verdadero o los dos falsos
is_male1 = True
is_tall1 = False

if is_male1 and is_tall1:
    print("you are a tall male")
else:
    print("you are either not male or not tall or both")

#condicional and y and not = si uno es falso y otro verdadero habra otra respuesta
is_male2 = True
is_tall2 = False

if is_male2 and is_tall2:
    print("you are a tall male")
elif is_male2 and not(is_tall2):
    print("you are a short male")
elif not(is_male2) and is_tall2:
    print("your are not a male but you are tall")
else:
    print("you are not male and not tall")


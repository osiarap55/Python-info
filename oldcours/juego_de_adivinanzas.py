# es un juego de adividanza donde hay una palabra que adivinar, tres oportunidas.
# estan son las variables de loop while que vamos a plantear
# la palabra que hay que adivinar es giraffe, dentro de la variable secret_world
secret_word = "giraffe"
# la variable guess esta vacia, y sera en input para que el usuario pueda poner la palabra que crea
guess = ""
# guess_count es la variable que cuenta las oportunidades y empieza en 0 y se ira sumando en el loop while hasta que llegue a 3.
guess_count = 0
# guess_limit es la variable limite de oportunidades que es 3, que en el momento que se llegue = 3 termina el juego
guess_limit = 3
# out_of_guesse es la variable que dice que se han acabado las oportunidade la cual es falsa ahora, en el momento que haya 3 intentos sera True
out_of_guesse = False
# dentro del while es el loop y a la derecha de while son las condiciones que tiene que cumplir el loop 
# guess != secret_world significa que esas son las condiciones, el loop continuara si son distintas las variables guess y secret_world
# and not(out_of_guesse) sera cierto mas adelante cuando se cumpla las 3 oportunidades y el loop terminara.
while guess != secret_word and not(out_of_guesse):
    # el condicional if dice que si la variable guess_cout que empieza en 0, es menor que que guess_limit que son 3, entonces continua el loop
    if guess_count < guess_limit:
        #si dentro del loop y de la condicion anterior el usuario tiene 3 oportunidades para adivinar la palabra mediante el comando input
        guess = input("enter guess: ")
        # guess_count significa que += 1 va sumando +1 oportunidades cada vez que vuelve a empezar el loop
        guess_count += 1 
    # si no se cumple las condiciones indicadas arriba entonces out_of_guesses sera = True lo que significa que se han cumplido las 3 oportunidades y se acaba el juego
    else:
        out_of_guesse = True
# el condiciona if infica aqui o una o otra, se imprimira "Out of guesses, YOU LOSE!" si out_of_guesses es true lo que significa que lo has intentado 3 veces.
if out_of_guesse:
    print("Out of guesses, YOU LOSE!")
# si no, de lo contrario significara que has acertado la palabra en tres oportunidades y has ganado
else:
    print("You win!")

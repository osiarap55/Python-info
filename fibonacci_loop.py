def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

# Ejemplo: Imprimir los primeros 10 términos de la serie de Fibonacci
n = 10
fib_result = fibonacci(n)
print(f"Los primeros {n} términos de la serie de Fibonacci son: {fib_result}")


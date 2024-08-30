def fibonacci(numero):
    fibonnaci1, fibonnaci2 = 0, 1

    if numero == fibonnaci1 or numero == fibonnaci2:
        return f"O numero {numero} pertence a sequencia de Fibonacci"
    
    while fibonnaci2 < numero:
        fibonnaci1, fibonnaci2 = fibonnaci2, fibonnaci1 + fibonnaci2
        if fibonnaci2 == numero:
            return f"O numero {numero} pertence a sequencia de Fibonacci"
        elif fibonnaci2 > numero:
            return f"O numero {numero} não pertence a sequencia de Fibonacci"

numero = int(input("informe o número: "))
print(fibonacci(numero))  

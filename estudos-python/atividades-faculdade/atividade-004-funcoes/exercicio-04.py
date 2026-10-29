def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = int(input("Quantos números deseja mostrar? "))
print(fibonacci(n))

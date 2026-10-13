def resumir_chamados(estados):
    total = len(estados)
    urgentes = estados.count("urgente")
    return total, urgentes

estados = input("Digite os estados: ").split()

total, urgentes = resumir_chamados(estados)

print("Total de chamados:", total)
print("Urgentes:", urgentes)
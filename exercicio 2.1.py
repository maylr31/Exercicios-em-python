def calcular_diferenca(A, B, C, D):
    #A docstring "" descreve o que a função faz e podem ser chamadas pela função help()
    """
    Função que calcula a diferença entre o produto de A e B
    e o produto de C e D.
    """
    return (A * B) - (C * D)

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

DIFERENCA = calcular_diferenca(A, B, C, D)


print(f"DIFERENCA = {DIFERENCA}")

# Leitura dos valores
A = int(input('Digite um valor:'))
B = int(input('Digite um valor:'))
C = int(input('Digite um valor:'))
D = int(input('Digite um valor:'))

# Verificação das condições
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    # Se todas as condições forem verdadeiras, os valores são aceitos
    print("\nValores aceitos")
else:
    # Caso contrário, os valores não são aceitos
    print("\nValores não aceitos. Verifique as condições.")

#não usei a condição def main()

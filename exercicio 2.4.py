# dados de entrada, a fun split divide uma string em várias partes com uma virgula ou espaço em branco etc.
codigo1, quantidade1, valor_unitario1 = input().split() 
codigo2, quantidade2, valor_unitario2 = input().split()

# Convertendo os valores de entrada para os tipos adequados
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
valor_unitario1 = float(valor_unitario1)

codigo2 = int(codigo2)
quantidade2 = int(quantidade2)
valor_unitario2 = float(valor_unitario2)

# Calculando o valor a ser pago
valor_a_pagar = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)

# Exibindo o resultado formatado
print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")

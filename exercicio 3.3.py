salario_atual = float(input('Por favor, digite o valor do seu salario R$:'))

# Verificar a faixa salarial e aplicar o reajuste

if salario_atual <= 400:
    percentual_reajuste = 15
elif salario_atual <= 800:
    percentual_reajuste = 12
elif salario_atual <= 1200:
    percentual_reajuste = 10
elif salario_atual <= 2000:
    percentual_reajuste = 7
else: 
    percentual_reajuste = 4 

# Calcular o valor do reajuste e o novo salário
valor_reajuste = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + valor_reajuste

# Imagora vai imprimir os resultados
print(f'''Novo salario:\n{novo_salario:.2f}
Reajuste ganho:\n{valor_reajuste:.2f}
Em percentual:\n{percentual_reajuste} %''')

#usei aspas triplas
# Entrada dos dados, eu não uso a função def pois ela é para chamar em novos codigos e deixar esse salvo,não vejo necessidade
numero = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada
print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")

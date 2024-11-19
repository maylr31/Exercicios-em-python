def calcular_salario_com_bonus(nome, salario_fixo, total_vendas):

    # Calcula o bônus de 15% sobre o total de vendas
    comissao = total_vendas * 0.15
    
    # Calcula o total a receber
    total_a_receber = salario_fixo + comissao
    
    # como fica
    print(f"O vendedor(ª){nome}, vendeu o TOTAL = R$ {total_a_receber:.2f}")

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês: "))

calcular_salario_com_bonus(nome, salario_fixo, total_vendas)

def main():
#def é usada para definir uma função, e main ou o nome que você der para utilizar ela novamente.
# Leitura do código e quantidade

    codigo, quantidade = map(int, input('Digite o codigo e a quantidade: ').split())
    
#A função input().split() divide a entrada em duas partes
# Tabela de preços

    tabela_precos = {
        1: 4.00,  # Cachorro Quente
        2: 4.50,  # X-Salada
        3: 5.00,  # X-Bacon
        4: 2.00,  # Torrada simples
        5: 1.50   # Refrigerante
    }

    # Verifica se o código é válido e calcula o total
    if codigo in tabela_precos:
        total = tabela_precos[codigo] * quantidade
        print(f"Total: R$ {total:.2f}")
    else:
        print("Código inválido!")

# Chamada da função principal
main()

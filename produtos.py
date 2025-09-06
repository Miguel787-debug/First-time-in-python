''' 2 - Desenvolva um programa que solicite ao usuário os dados 
de um produto (nome, valor e quantidade) e armazene-os em 
um arquivo de texto chamado "produtos.txt".
'''

letra = 's'
while letra == 's':
    nome_produto = input('Digite o nome do produto: ')
    valor_produto = float(input('Digite o valor do produto (em R$): '))
    quantidade_produto = int(input('Digite a quantidade do produto: '))

    with open('produtos.txt', 'a') as arquivo:
        arquivo.write(f"{nome_produto} | R$ {valor_produto:.2f} | Quantidade: {quantidade_produto}\n")
        print(f"Produto {nome_produto} adicionado com sucesso!")
    letra = input('Deseja adicionar outro produto [s/n]? ').lower()
    if letra not in ['s', 'n']:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        letra = 'n'
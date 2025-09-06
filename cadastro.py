letra = "s"
while letra.lower() == "s":
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")

    arquivo = open("pessoa.txt", "a")
    arquivo.write(f"{nome} | {email}\n")
    arquivo.close()

    letra = input("Deseja realizar um novo cadastro - [S/N]: ")

print("Cadastro encerrado.")

biblioteca = [] #biblioteca como uma lista de listas


def adicionar_livro():
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    ano = input("Informe o ano do livro: ")
    biblioteca.append([titulo, autor, ano])
    print(f"'{titulo}' adicionado com sucesso!")


def listar_livros():
    if not biblioteca:
        print("Nenhum livro na biblioteca.")
    else:
        for livro in biblioteca:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")


def buscar_livro():
    titulo = input("Digite o título do livro que deseja buscar: ")
    encontrados = [livro for livro in biblioteca if livro[0].lower() == titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")
    else:
        print(f"Nenhum livro com esse título encontrado '{titulo}'.")

while True:
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Sair")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    if escolha == '1':
        adicionar_livro()
    elif escolha == '2':
        listar_livros()
    elif escolha == '3':
        buscar_livro()
    elif escolha == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")

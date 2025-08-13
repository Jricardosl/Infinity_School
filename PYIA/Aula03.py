#ATIVIDADE 5
# Faça um programa que, dado um conjunto de N
# números, determine o menor valor, o maior valor e a
# soma dos valores.

# def quantidade_numeros():
#     N = int(input("Quantos números você deseja inserir? "))  # Lê a quantidade de números
#     if N <= 0:
#         print("A quantidade de números deve ser maior que zero.")
#         return

#     numeros = set() #Criando conjunto vazio
    
#     # Lê os N números
#     for i in range(N):
#         numero = int(input(f"Digite o {i+1}º número: "))
#         numeros.add(numero)

#     # Calcula menor, maior e soma
#     C

#     # Exibe os resultados
#     print("\nResultados:")
#     print(f"Conjunto informado {numeros}")
#     print(f"Menor valor: {menor}")
#     print(f"Maior valor: {maior}")
#     print(f"Soma dos valores: {soma}")

# # Executa o programa
# quantidade_numeros()

# OU

# N = int(input("Quantos números você deseja inserir? "))  # Lê a quantidade de números

# numeros = set() #Criando conjunto vazio

# for i in range(N):
#         numero =float(input(f"Digite o {i+1}º número: "))
#         numeros.add(numero)

# menor = min(numeros)
# maior = max(numeros)
# soma = sum(numeros)

# print("\nResultados:")
# print(f"Conjunto informado {numeros}")
# print(f"Menor valor: {menor}")
# print(f"Maior valor: {maior}")
# print(f"Soma dos valores: {soma}")


# DESAFIO PRÁTICO

# Gerenciamento de Compras de Produtos

# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,

# incluindo:

# A) O total gasto na compra.

# B) A quantidade de produtos que custam mais de R$1000.

# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

# Utilizando função

# def gerenciamento_compras():
#     produtos = []

#     continuar = 'S'

#     while continuar == 'S':
#         nome = input("Nome do produto: ")
#         preco = float(input("Preço do produto (R$): "))

#         # Adiciona um dicionário com as infos do produto
#         produtos.append({"nome": nome, "preco": preco})

#         continuar = input("Deseja adicionar outro produto? (S/N): ").strip().upper()
#         while continuar not in ['S', 'N']:
#             continuar = input("Resposta inválida. Digite 'S' para sim ou 'N' para não: ").strip().upper()

#     # Processamento dos dados
#     total_gasto = sum(p["preco"] for p in produtos)
#     produtos_maior_1000 = sum(1 for p in produtos if p["preco"] > 1000)
#     produto_mais_barato = min(produtos, key=lambda p: p["preco"])

#     # Exibição dos resultados
#     print("\n===== RESUMO DA COMPRA =====")
#     print(f"Total gasto na compra: R${total_gasto:.2f}")
#     print(f"Quantidade de produtos acima de R$1000: {produtos_maior_1000}")
#     print(f"Produto mais barato: {produto_mais_barato['nome']} (R${produto_mais_barato['preco']:.2f})")

# Executa a função
# gerenciamento_compras()

# Sem usar função:

# produtos = [] #Criando uma lista vazia
# continuar = 'S'

# while continuar == 'S':
#     nome = input("Nome do produto: ")
#     preco = float(input("Preço do produto (R$): "))

#     produtos.append({"nome": nome, "preco": preco})

#     continuar = input("Deseja adicionar outro produto? (S/N): ").strip().upper() #Pergunta se deseja continuar inserindo produtos 
#     #método .strip = Remove espaços em branco do início e do fim da string.
#     #método .upper = Converte todos os caracteres da string para letras maiúsculas.

#     while continuar not in ['S', 'N']: #Verifica se foi informado S ou N, caso digite diferente solicite que repita a resposta
#         continuar = input("Resposta inválida. Digite 'S' para sim ou 'N' para não: ").strip().upper()

# # Processamento dos dados
# total_gasto = sum(p["preco"] for p in produtos)
# produtos_maior_1000 = sum(1 for p in produtos if p["preco"] > 1000)
# produto_mais_barato = min(produtos, key=lambda p: p["preco"])

# # Exibição dos resultados
# print("\n===== RESUMO DA COMPRA =====")
# print(f"Total gasto na compra: R$ {total_gasto:.2f}")
# print(f"Quantidade de produtos acima de R$ 1000: {produtos_maior_1000}")
# print(f"Produto mais barato: {produto_mais_barato['nome']} (R$ {produto_mais_barato['preco']:.2f})")

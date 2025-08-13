#SET    
# set1 = {"Infinity", "School", "202"}
# set1 ={letra for letra in "infinity" if letra not in "aeiou"}
# convidados = {"João", "Maria", "Eduarda"}
# convidados.add("Marcela")
# print (convidados)

# ATIVIDADE PRATICA 01
# Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele:
# "maça", "banana", "uva", "laranja", "morango"
# Em seguida, imprima o conjuto.

# Criar conjunto vazio
# frutas = set()

# # Adicionar as frutas
# frutas.add("maçã")
# frutas.add("banana")
# frutas.add("uva")
# frutas.add("laranja")
# frutas.add("morango")

# # Imprimir o conjunto
# print(frutas)

#Ou usando update

# frutas = set()
# frutas.update(["maça", "banana", "uva", "laranja", "morango"])
# print(frutas)

# ATIVIDADE PRÁTICA 2

# Verifique se a fruta "banana"está presente no conjunto
# frutas e imprima o resultado.

# Conjunto criado anteriormente
# frutas = {"maçã", "banana", "uva", "laranja", "morango"}

# # Verificar se "banana" está presente
# if "banana" in frutas:
#     print("Sim, 'banana' está presente no conjunto.")
# else:
#     print("Não, 'banana' não está presente no conjunto.")


# ATIVIDADE PRÁTICA 3

# Crie um conjunto chamado frutas_vermelhas e adicione
# as seguintes frutas a ele:"morango","cereja"e"framboesa". 
# Em seguida, imprima o conjunto.

# Criar conjunto vazio
# frutas_vermelhas = set()

# Adicionar frutas ao conjunto
# frutas_vermelhas.add("morango")
# frutas_vermelhas.add("cereja")
# frutas_vermelhas.add("framboesa")

# # Imprimir o conjunto
# print(frutas_vermelhas)

#Ou usando update

# frutas_vermelhas=set()
# frutas_vermelhas.update(["morango"], ["cereja"],["framboesa"])
# print(frutas_vermelhas)

# # ATIVIDADE PRÁTICA 4

# # Remova a fruta "cereja" do conjunto frutas_vermelhas e
# # imprima o conjunto atualizado.

# # Conjunto inicial
# frutas_vermelhas = {"morango", "cereja", "framboesa"}

# # Remover "cereja"
# # frutas_vermelhas.remove("cereja")
# # ou, alternativamente, usar discard para evitar erro se não existir
# frutas_vermelhas.discard("cereja")

# # Imprimir conjunto atualizado
# print(frutas_vermelhas)

# ATIVIDADE PRÁTICA 5
# Crie dois conjuntos, A e B, e realize a união dos dois
# conjuntos.

# Criar dois conjuntos A e B
# A = {"Ana", "Bruno", "Junior"}
# B = {"Daniela", "Eduardo", "Junior"}

# # Realizar a união dos dois conjuntos
# uniao = A.union(B)  # ou A | B

# # Imprimir o resultado
# print("Conjunto A:", A)
# print("Conjunto B:", B)
# print("União dos conjuntos:", uniao)

# ATIVIDADE PRÁTICA 6
# Crie um programa que recebe dois conjuntos e exibe a
# interseção deles

# # Criar dois conjuntos
# A = {"Ana", "Bruno", "Junior", "Fernanda"}
# B = {"Junior", "Eduardo", "Fernanda", "Gabriel"}

# Calcular a interseção
# intersecao = A.intersection(B)  # ou A & B

# # Imprimir resultados
# print("Conjunto A:", A)
# print("Conjunto B:", B)
# print("Interseção dos conjuntos:", intersecao)

# A interseção pega apenas os elementos que existem nos dois conjuntos.

# ATIVIDADE PRÁTICA 7
# Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando
# conjuntos.

# Criar duas listas
# lista1 = ["Ana", "Bruno", "Junior", "Ana"]
# lista2 = ["Junior", "Eduardo", "Fernanda", "Bruno"]

# # Converter listas para conjuntos (remove duplicatas)
# conjunto1 = set(lista1)
# conjunto2 = set(lista2)

# # Calcular a união
# uniao = conjunto1.union(conjunto2)  # ou conjunto1 | conjunto2

# # Exibir resultados
# print("Lista 1:", lista1)
# print("Lista 2:", lista2)
# print("União dos elementos únicos:", uniao)

# ATIVIDADE PRÁTICA 8
# Escreva um programa que EXIBA um dicionário contendo
# informações de pessoas (nome, idade) e exiba essas
# informações.

# Criar um dicionário com informações de pessoas
# pessoas = {
#     "Pessoa1": {"nome": "Ana", "idade": 25},
#     "Pessoa2": {"nome": "Bruno", "idade": 30},
#     "Pessoa3": {"nome": "Carla", "idade": 22}
# }

# # Exibir as informações
# for chave, dados in pessoas.items():
#     print(f"{chave}: Nome = {dados['nome']}, Idade = {dados['idade']}")

# ATIVIDADE PRÁTICA 9
# Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

# Dicionário de exemplo
# pessoas = {
#     "Ana": 25,
#     "Bruno": 30,
#     "Carla": 22
# }

# # Percorrendo as chaves
# print("Chaves:")
# for chave in pessoas.keys():
#     print(chave)

# # Percorrendo os valores
# print("\nValores:")
# for valor in pessoas.values():
#     print(valor)

# ATIVIDADE PRÁTICA 10
# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já
# existir.

# Função para adicionar ou atualizar chave e valor no dicionário
# def adicionar_ou_atualizar(dicionario, chave, valor):
#     dicionario[chave] = valor
#     print(f"Chave '{chave}' atualizada para o valor: {valor}")

# # Dicionário inicial com alguns dados
# meu_dicionario = {"Ana": 25, "Bruno": 30}

# # Receber dados do usuário
# nova_chave = input("Digite a chave que deseja adicionar ou atualizar: ")
# # Como idade é número, vamos converter para int, mas pode adaptar para outro tipo
# novo_valor = int(input("Digite o valor correspondente (número): "))

# # Atualizar o dicionário
# adicionar_ou_atualizar(meu_dicionario, nova_chave, novo_valor)

# print("Dicionário atualizado:", meu_dicionario)


# ATIVIDADE PRÁTICA 11
# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso
# contrário

# def verificar_chaves(dicionario, lista_chaves):
#     for chave in lista_chaves:
#         if chave not in dicionario:
#             return False
#     return True

# # Exemplo de uso
# meu_dicionario = {"Ana": 25, "Bruno": 30, "Carla": 22}
# lista_de_chaves = ["Ana", "Carla"]

# resultado = verificar_chaves(meu_dicionario, lista_de_chaves)
# print(f"Todas as chaves existem? {resultado}")

# ATIVIDADE PRÁTICA 12
# Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os
# resultados finais.

# # Opções disponíveis para votação
# opcoes = {
#     1: "Candidato A",
#     2: "Candidato B",
#     3: "Candidato C"
# }

# # Dicionário para contar votos, inicializado com zero
# votos = {1: 0, 2: 0, 3: 0}

# print("Sistema de votação iniciado!")
# print("Digite o número da opção para votar ou 0 para encerrar.")

# while True:
#     # Mostrar opções para o usuário
#     print("\nOpções disponíveis:")
#     for numero, nome in opcoes.items():
#         print(f"{numero} - {nome}")
#     print("0 - Encerrar votação")

#     # Receber voto
#     try:
#         escolha = int(input("Seu voto: "))
#     except ValueError:
#         print("Por favor, digite um número válido.")
#         continue

#     # Condição para encerrar
#     if escolha == 0:
#         print("\nVotação encerrada!")
#         break

#     # Verificar se a escolha é válida
#     if escolha in opcoes:
#         votos[escolha] += 1
#         print(f"Voto registrado para {opcoes[escolha]}!")
#     else:
#         print("Opção inválida. Tente novamente.")

# # Exibir resultados finais
# print("\nResultados finais da votação:")
# for numero, nome in opcoes.items():
#     print(f"{nome}: {votos[numero]} votos")


# ATIVIDADE PRÁTICA 13
# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas e
# exiba-a.

# Dicionário com nomes dos alunos e suas notas
# notas = {
#     "Ana": 8.5,
#     "Bruno": 7.0,
#     "Carla": 9.0,
#     "Daniel": 6.5
# }

# # Calcular a média das notas
# media = sum(notas.values()) / len(notas)

# # Exibir a média
# print(f"A média das notas da turma é: {media:.2f}")


# ATIVIDADE PRÁTICA 14
# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

# Lista com números, incluindo duplicatas
# lista_numeros = [2, 5, 7, 2, 3, 5, 8, 9, 3]

# # Remover duplicatas usando conjunto
# conjunto_numeros = set(lista_numeros)

# # Converter de volta para lista (se quiser manter ordem, precisa um pouco mais de código)
# lista_sem_duplicatas = list(conjunto_numeros)

# # Exibir resultados
# print("Lista original:", lista_numeros)
# print("Lista sem duplicatas:", lista_sem_duplicatas)

# ATIVIDADE PRÁTICA 15
# Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.

# # Lista com vários conjuntos
# conjuntos = [
#     {"maçã", "banana"},
#     {"banana", "laranja"},
#     {"uva", "morango"},
#     {"laranja", "abacaxi"}
# ]

# # União de todos os conjuntos
# uniao_geral = set()  # conjunto vazio para começar

# for c in conjuntos:
#     uniao_geral = uniao_geral.union(c)

# # Exibir resultado
# print("União dos múltiplos conjuntos:", uniao_geral)

# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 1
# Cadastro de Alunos: O programa deve permitir ao usuário
# cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno
# devem ser armazenados em um dicionário com as
# seguintes chaves:'nome','idade','notas'. As notas devem
# ser armazenadas em uma tupla.

# Lista para armazenar os alunos
alunos = []

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    
    print("Digite as notas nas disciplinas:")
    matematica = float(input("Matemática: "))
    ciencias = float(input("Ciências: "))
    historia = float(input("História: "))
    
    notas = (matematica, ciencias, historia)
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")

# Loop para cadastrar vários alunos
while True:
    cadastrar_aluno()
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break

# Exibir todos os alunos cadastrados
print("\nAlunos cadastrados:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}")

# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 2
# Visualização de Alunos: O programa deve permitir ao usuário
# visualizar todos os alunos cadastrados, exibindo suas informações
# de forma organizada.
# Média de Notas: O programa deve calcular a média das
# notas de cada aluno e exibi-la.
# Aluno com Melhor Média: O programa deve identificar e
# exibir o aluno com a melhor média de notas.

# Lista para armazenar os alunos
# alunos = []

# # Função para cadastrar um aluno
# def cadastrar_aluno():
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input("Digite a idade do aluno: "))
    
#     print("Digite as notas nas disciplinas:")
#     matematica = float(input("Matemática: "))
#     ciencias = float(input("Ciências: "))
#     historia = float(input("História: "))
    
#     notas = (matematica, ciencias, historia)
    
#     aluno = {
#         "nome": nome,
#         "idade": idade,
#         "notas": notas
#     }
    
#     alunos.append(aluno)
#     print(f"Aluno {nome} cadastrado com sucesso!\n")

# # Função para calcular a média das notas de um aluno
# def calcular_media(notas):
#     return sum(notas) / len(notas)

# # Função para exibir os alunos com suas médias
# def exibir_alunos():
#     print("\nLista de alunos cadastrados:")
#     for aluno in alunos:
#         media = calcular_media(aluno["notas"])
#         print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Média: {media:.2f}")

# # Função para encontrar o aluno com a melhor média
# def aluno_melhor_media():
#     if not alunos:
#         print("Nenhum aluno cadastrado.")
#         return
#     melhor_aluno = alunos[0]
#     melhor_media = calcular_media(melhor_aluno["notas"])
#     for aluno in alunos[1:]:
#         media = calcular_media(aluno["notas"])
#         if media > melhor_media:
#             melhor_media = media
#             melhor_aluno = aluno
#     print(f"\nAluno com a melhor média: {melhor_aluno['nome']} - Média: {melhor_media:.2f}")

# # Loop principal para o sistema
# while True:
#     print("\nMenu:")
#     print("1 - Cadastrar aluno")
#     print("2 - Visualizar alunos")
#     print("3 - Exibir aluno com melhor média")
#     print("0 - Sair")

#     escolha = input("Escolha uma opção: ")

#     if escolha == "1":
#         cadastrar_aluno()
#     elif escolha == "2":
#         exibir_alunos()
#     elif escolha == "3":
#         aluno_melhor_media()
#     elif escolha == "0":
#         print("Encerrando o sistema. Até mais!")
#         break
#     else:
#         print("Opção inválida, tente novamente.")
#FUNÇÃO FOR
# for i in range(5):
#     print(i)
    
#Break no for

# numero_procurado = 7
# for i in range(1,11):
#     if i == numero_procurado:
#         print(f"Número {numero_procurado} encontrado!")
#         break
#     print(i)
    
#Continue no for
# for i in range(1,11):
#     if i %2 !=0:
#         continue
#     print(i)

# Break e continue

# for num in range(2, 20):              # Loop de num indo de 2 até 19 (20 não incluso)
#     for i in range(2, num):           # Testa todos os divisores de 2 até num-1
#         if num % i == 0:              # Se num for divisível por i (resto 0)...
#             break                     # ...então num NÃO é primo, interrompe o laço
#     else:                             # Esse 'else' está ligado ao 'for', NÃO ao 'if'
#         print(f"{num} é um número primo!")  # Se o 'for' não foi interrompido (break), num é primo

# ATIVIDADE 1
# Faça a definição de uma lista contendo os números de 1 até 5. 
# Finalmente, utilize o print() para exibir os valores da lista.

# Criando a lista com números de 1 a 5
# lista_numero = [1, 2, 3, 4, 5]
# print(lista_numero)  # Exibindo a lista

# ATIVIDADE 2
# Faça a definição de uma lista contendo as vogais. 
# Finalmente, utilize o print() para exibir os valores da lista.

# Criando a lista com números de a, e , i, o, u
# lista_vogal = ["a", "e", "i", "o", "u"]
# print(lista_vogal)  # Exibindo a lista

# ATIVIDADE 3
#Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferente.
#Utilize o print() para exibir o terceiro elemento dessa lista

# minha_lista = [10, "Olá", 3.14, True, [1, 2, 3]]
# print(minha_lista[2])

#Adicionando itens ao final da lista com método .append()
# numeros = [1,2,3,4,5]
# numeros.append(6)
# print(numeros)

#Adicionando itens em dada posição da lista com método .insert()
# numeros = [10,30,40,50]
# letras = ["a","e","o","u"]
# pesos = [1.2,3.4,5.3,6.7]

# Inserindo valores nas respectivas posições das listas
# numeros.insert(1,20) #Inserindo 20 na posição 2
# letras.insert(2,"i") #Inserindo "i na posição 3
# pesos.insert(2,4.0) #Inserindo 4.0 na posição 3

# Exibindo as inserções dos valores
# print(numeros)
# print(letras)
# print(pesos)

# ATIVIDADE 4
#Crie uma tupla para representar as informações de três palestrantes,
#cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados.
#Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição

# palestrante1 = ("Ricardo Lima", "Inteligência Artificial", "Infinity")
# palestrante2 = ("Antonio José", "Análise de dados", "Senac")
# palestrante3 = ("Marcos André", "Banco de Dados", "Cesar School")

# print("Informações do terceiro palestrante:")
# print(f"Nome: {palestrante3[0]}")
# print(f"Tema: {palestrante3[1]}")
# print(f"Instituição: {palestrante3[2]}")

#Desafio prático
#Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas 
#representando os resultados das equipes em diferentes modalidades. Cada tupla contém o nome da equipe,
#Seguido por uma lista de pontuações obtidas em cada rodada da competição

#1 Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias.
#2 Ordene a lista medias em ordem descrescente.
#3 Crie uma nova lista chamada classificação que contém tuplas, onde cada tupla contém o nome da equipe
#e sua média de pontuações.
#4 Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a
#pontuação mais alta para a mais baixa

# # Dados das equipes
# equipe1 = ("Equipe Alpha", [6.5, 7.5, 8.0])
# equipe2 = ("Equipe Ômega", [7.5, 5.6, 9.0])
# equipe3 = ("Equipe Beta", [9.5, 7.0, 7.0])

# # Lista com todas as equipes - Assim, podemos percorrer todas as equipes de uma vez com um for.
# equipes = [equipe1, equipe2, equipe3]

# # 1. Calcular a média das pontuações e armazenar em 'medias'
# medias = []
# for equipe in equipes:
#     nome = equipe[0] # Pega o nome da equipe
#     pontuacoes = equipe[1] # Pega a lista de pontuações
#     media = sum(pontuacoes) / len(pontuacoes) # Soma os pontos e divide pela quantidade
#     medias.append((nome, media))  # Tupla com (nome, média) - # Salva o nome e a média numa nova tupla

# # 2 e 3. Ordenar por média em ordem decrescente (classificação)
# classificacao = sorted(medias, key=lambda x: x[1], reverse=True)

# # 4. Exibir a classificação final
# print("Classificação Final:")
# for equipe in classificacao:
#     print(f"{equipe[0]} - Média: {equipe[1]:.2f}")

#REVISÃO DA AULA - 29.07.2025

#CADASTRO DE NOTAS DE ALUNOS
#Faça um programa que solicite 3 notas ao usuário
#Armazene as notas numa lima
#Repita esta ação para 3 alunos
#Itere sobre a lista e calcule a média
#Mostre a média de cada aluno obtida no terminal

# notas_todos_alunos = []

# qtde_alunos =3

# qtde_notas =3



# for i in range(qtde_alunos):

# #Faça um programa que solicite 3 notas ao usuário

#     notas_cada_aluno = []

#     for j in range(qtde_notas):

#         nota = float(input(f"Digite o{j+1}ª nota do{i+1}º aluno: "))

#         notas_cada_aluno.append(nota)

# #Armazene as notas numa lista

#     notas_todos_alunos.append(notas_cada_aluno)

# print(notas_todos_alunos)



# #itere sobre a lista e calcule a média

# for notas_aluno in notas_todos_alunos:

#     soma=0

#     for nota in notas_aluno:

#         soma += nota

#     media = soma / qtde_notas

# # Mostre a média de cada alunos obtida

#     print(media)






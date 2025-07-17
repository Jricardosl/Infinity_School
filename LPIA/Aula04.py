# FOR
# for i in range (5):
#     print (i)

# palavra = "Python"
# for letra in palavra:
#     print (letra)
    
# Três forma de usar o for:

# for i in range (5):
#    print (i)

#Utilizando o While

# contador = 0

# while contador <5:
#     print (contador)
#     contador +=1


# for i in range (2, 7):
#    print (i)

#Utilizando o While   
# contador = 2

# while contador <7:
#     print (contador)
#     contador +=1

   
# for i in range (1, 10, 2):
#    print (i)

#Utilizando o While

# contador = 1

# while contador <10:
#     print (contador)
#     contador +=2


#Atividade 01:
#Tabuada de um número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

# numero = int(input("Digite um número para ver a tabuada: "))
# print(f"Segue a tabuada de {numero}:\n")

# for contador in range(1, 11):
#     resultado = numero * contador
#     print(f"{numero} x {contador} = {resultado}")
    
#Atividade 02:
# Soma de Números de 1 a 100:
# Crie um programa que use um laço for para somartodos os números de 1 a 100
# e exiba o resultado.

# soma = 0

# for numero in range(1, 101):
#     soma += numero  # soma = soma + numero

# print(f"A soma dos números de 1 a 100 é: {soma}")


# Atividade 03:
# Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.

# palavra = input("Digite uma palavra: ")
# for letra in palavra:
#     print (letra)
    
# Atividade 04:
# Contagem Regressiva de 10 a 1:
# Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 
# e, em seguida, exiba "Feliz Ano Novo!".

# print("Contagem Regressiva")
# for i in range(10, 0, -1):  # vai de 10 até 1, decrementando de 1 em 1
#     print(i)
# print("Feliz Ano Novo!")

# Funcionamento do for com condicionais

# Imprima números pares de 1 a 10:
# for i in range (1, 11):
#     if i %2 == 0:
#         print(f"{i} é par")
        
# Exemplo:
# Contagem de Vogais em uma String
# Explicação: Este loop for conta o número de vogais
# na string texto eimprime o total

# texto="Programação em Python"
# contador_vogais = 0
# for caractere in texto:
#     if caractere.lower() in "aeiou":
#         contador_vogais += 1
# print (f"A palavra {texto} tem {contador_vogais} vogais: ")

# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

# positivos = 0
# negativos = 0

# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: ")) 
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

#     # Se for zero, não conta como positivo nem negativo

# print(f"\nQuantidade de números positivos: {positivos}")

# print(f"Quantidade de números negativos: {negativos}")


# Atividade 06:
# Soma de Números Pares:
# Escreva um programa que use um laço for para somar
# todos os números pares de 1 a 50 e exiba o resultado final.


# soma = 0

# for numero in range(1, 51):
#     if numero % 2 == 0:
#         soma += numero   
# print("A soma dos números pares entre 1 a 50 é:",soma)


# # ou 

# soma = 0

# for numero in range(2, 51, 2):  # Começa em 2, vai até 50, de 2 em 2
#     soma += numero
# print("A soma dos números pares entre 1 e 50 é:", soma)


# Atividade 07:

# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


# palavra = input ("Digite uma palavra: ")

# contador_vogais = 0

# for caractere in palavra:
#     if caractere.lower() in "aeiou":
#         contador_vogais += 1
# print (f"A palavra {palavra} tem {contador_vogais} vogais: ")


# Atividade 08:

# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,
# "Reprovado" para média < 6).

# soma = 0

# for i in range(5):
#     nota = float(input(f"Digite o {i+1}ª nota: "))
#     soma += nota
# media = soma / 5
# print ("Sua média é",media)
# if media >= 6:
#     print ("Classificação: Aprovado")
# else:
#     print ("Classificação: Reprovado")

#Utilizando o While

# soma = 0
# i = 0
# total_notas = 5

# while i < total_notas:
#     nota = float(input(f"Digite a {i+1}ª nota: "))
#     soma += nota
#     i += 1  # incrementa o contador
# media = soma / total_notas
# print("Sua média é", media)

# if media >= 6:
#     print("Classificação: Aprovado")
# else:
#     print("Classificação: Reprovado")


#FOR + IF + BREAK
#Exemplo
# for numero in range (10):
#     if numero == 5:
#         break
#     print(numero)
# print("Laço interrompido")


# #Outro exemplo
# for numero in range (1, 10):
#     if numero %2 ==0:
#         print(f"Número par encontrado: {numero}, interrompendo o laço.")
#         break
#     else:
#         print(f"{numero} é impar, continuando.") 
# else:
#     print ("Todos os números foram impares")

#EXEMPLO MENU INTERATIVO
# while True:
#     print("Menu")
#     print("1. Contar de 1 a 5")
#     print("2. Sair")
#     opcao = input("Escolha uma opção: ")
    
#     if opcao == "1":
#         for i in range (1,6):
#             print(i)
#     elif opcao == "2":
#         print ("Saindo do programa.")
#         break
#     else:
#         print("Opção invalida, tente novamente")

# #FOR + Condicional + BREAK e Continue

# #Exemplo: Encontrar o primeiro número divisível por 3 e pular números divisíveis por 2.
# for numero in range (1,20):
#     if numero % 2 == 0:
#         continue #pular números divisiveis por 2
#     if numero % 3 == 0:
#         print (f"Número {numero} é o primeiro divisível por 3 (não é divisível por 2).")
#         break
#     print(f"Número não divisível por 2: {numero}")

#ANINHAMENTO DE FOR 
#Exemplo: Filtrar Pares e Ímpares em um Intervalo

# for i in range (1,6):
#     for j in range (1,6):
#         if (i + j) % 2 ==0:
#             print(f"{i} + {j} é par")
#         else:
#             print(f"{i} + {j} é ímpar")

# Atividade 09:
# Verificar Números Pares e Impares com Interrupção:
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

# for i in range(1, 21):
#     if i == 15:
#         print(f"{i} é ímpar, processo interrompido.")
#         break
#     elif i % 2 == 0:
#         print(f"{i} é par")
#     else:
#         print(f"{i} é ímpar")
        

# Atividade 10:
# Contar Números Positivos e Negativos:
# Peça ao usuário para inserir 10 números. Use um laço for com condicionais 
# para contar quantos são positivos e quantos são negativos.
# Pare o loop se o número 0 for inserido, usando break.

# positivos = 0
# negativos = 0

# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     if numero ==0:
#         print(f"O número digitado é zero. Encerrando a contagem.")
#         break 
#     elif numero > 0:
#         positivos += 1
#     else:
#         negativos += 1

#     # Se for zero, não conta como positivo nem negativo

# print(f"\nQuantidade de números positivos: {positivos}")

# print(f"Quantidade de números negativos: {negativos}")



# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.

# for i in range(1, 31):  # Vai de 1 até 30 (inclusive)
#     if i > 20:
#         print(f"{i} é maior que 20. Encerrando o loop.")
#         break
#     if i % 5 == 0:
#         print(f"{i} é múltiplo de 5")
#     else:
#         print(i)


# Atividade 12:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. 
# Use um laço for para calcular o total. Aplique um desconto de 10% 
# se o total ultrapassar 100 e interrompa o loop com break.

# soma = 0

# for i in range(5):
#     preco = float(input(f"Digite o {i+1}º preço do produto: "))
#     soma += preco

#     if soma > 100:
#         desconto = soma * 0.10
#         total_com_desconto = soma - desconto
#         print(f"O total R$ {soma:.2f} ultrapassou R$ 100,00.")
#         print(f"Desconto de 10% aplicado: R$ {desconto:.2f}")
#         print(f"Total com desconto: R$ {total_com_desconto:.2f}")
#         print("Processo interrompido.")
#         break
# else:
#     print(f"\nTotal dos produtos: R$ {soma:.2f}")
#     print("Sem desconto aplicado.")

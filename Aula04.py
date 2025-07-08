# FOR
# for i in range (5):
#     print (i)

# palavra = "Python"
# for letra in palavra:
#     print (letra)
    
# Três forma de usar o for:
# for i in range (5):
#    print (i)

# for i in range (2, 7):
#    print (i)
   
# for i in range (1, 10, 2):
#    print (i)

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

texto="Programação em Python"
contador_vogais = 0
for caractere in texto:
    if caractere.lower() in "aeiou":
        contador_vogais += 1
print (f"A palavra {texto} tem {contador_vogais} vogais: ")
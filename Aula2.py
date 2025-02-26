"""Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda."""

"""idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print(f"A primeira idade ({idade1}) é maior que a segunda idade ({idade2}).")
elif idade1 < idade2:
    print(f"A primeira idade ({idade1}) é menor que a segunda idade ({idade2}).")
else:
    print(f"As duas idades são iguais ({idade1}).") """


"""Atividade 02:
Verificar Igualdade de Strings:
Peça ao usuário duas palavras e use operadores
de comparação para verificar se elas são iguais"""

"""palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavra1 == palavra2:
    print("As palavras são iguais.")
else:
    print("As palavras são diferentes.")"""
    
"""Atividade 03:
Verificação de Maioridade e Habilitação:
Crie um programa que peça a idade do usuário e se ele possui habilitação
(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
(>= 18) e possui habilitação."""

"""idade = int(input("Qual sua idade? "))
habilitacao = input("Você possui habilitação? (sim/não): ").strip().lower()

if idade >= 18 and habilitacao == "sim":
    print("Você é maior de idade e possui habilitação.")
elif idade >= 18 and (habilitacao == "não" or habilitacao == "nao"):
    print("Você é maior de idade, mas não possui habilitação.")
elif idade < 18 and habilitacao == "sim":
    print("Você possui habilitação, mas não tem idade suficiente para dirigir.")
else:
    print("Você não é maior de idade e também não possui habilitação.")"""


"""Atividade 04:
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 6."""

"""nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

if nota1 == 6 and nota2 == 6:
    print("As duas notas são iguais a 6.")
    print(f"A primeira nota é {nota1} e a segunda nota é {nota2}.")
elif nota1 >= 6 and nota2 >= 6:
    print("As duas notas são maiores ou iguais a 6.")
    print(f"A primeira nota é {nota1} e a segunda nota é {nota2}.")
elif nota1 < 6 and nota2 < 6:
    print("As duas notas são menores que 6.")
    print(f"A primeira nota é {nota1} e a segunda nota é {nota2}.")
else:
    print("Uma das notas é menor que 6.")
    print(f"A primeira nota é {nota1} e a segunda nota é {nota2}.")"""


"""Atividade 05:
Desconto em Preço:
Peça ao usuário para inserir o preço de um produto e, em seguida,
use o operador de atribuição -= para aplicar um desconto de 5%."""
    

"""preco_original = float(input("Qual o preço do produto? "))
preco_com_desconto = preco_original 
preco_com_desconto -= preco_com_desconto * 0.05

print(f"Preço original: R$ {preco_original:.2f}")
print(f"Preço com 5% de desconto: R$ {preco_com_desconto:.2f}")
"""



"""Atividade 06:
Dobro do Valor:
Solicite ao usuário um número e use o operador de
atribuição *= para dobrar o valor e exibir o resultado.
"""
"""preco_original = float(input("Qual o preço do produto? "))
preco_dobrado = preco_original 
preco_dobrado *= 2 

print(f"Preço original: R$ {preco_original:.2f}")
print(f"Dobrando o valor: R$ {preco_dobrado:.2f}")"""

"""Atividade 07:
Verificação de Caracteres em uma String:
Crie um programa que peça ao usuário uma frase e um caractere.
Use o operador de associação in para verificar se o caractere está
<<<<<<< HEAD
presente na frase."""

=======
presente na frase.

frase = input("Digite uma frase: ")
print (f"A frase digitada foi: {frase}")

# Garantir que o usuário insira apenas um caractere
letra = input("Escreva um caractere: ")
while len(letra) != 1:
    letra = input("Por favor, insira apenas um caractere: ")

# Ignorar diferenças entre maiúsculas e minúsculas
resposta = "Sim" if letra.lower() in frase.lower() else "Não"

# Exibir o resultado
print(f"O caractere '{letra}' está na frase? {resposta}") """
>>>>>>> 588cb77 (Atividades de 7 a 10)
"""Atividade 08:
Verificação de Palavras em uma Frase:
Peça ao usuário para inserir uma frase e uma palavra.
<<<<<<< HEAD
Use in para verificar se a palavra está na frase."""
=======
Use in para verificar se a palavra está na frase.

frase1 = input("Digite uma frase: ")
print (f"A frase digitada foi: {frase1}")

palavra1 = input("Digite uma palavra: ")

resposta = "Sim" if palavra1.lower() in frase1.lower() else "Não"

print(f"A palvra '{palavra1}' está na frase? {resposta}") """

"""Atividade 9
Crie um programa que peça ao usuário número e use a estrutura condicional 
if para verificar se ele é par ou ímpar.

numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:  # se o resto da divisão por 2 for igual a zero
    print(f"O número {numero} é Par.")
else:
    print(f"O número {numero} é Ímpar.")"""

"""Atividade 10

Verificar Nota para Aprovado:

Crie um programa que peça a nota de um aluno e use if para verificar se ele foi aprovado (nota >=6)"""

nota = float(input("Digite sua nota: "))

if nota >= 6:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
>>>>>>> 588cb77 (Atividades de 7 a 10)


#FUNÇÕES I

# ATIVIDADE PRÁTICA 1
# Crie uma função que receba um nome e imprima uma saudação personalizada.

# nome = input("Digite seu nome: ")

# def saudacao (nome):
#     print (f"Seja bem vindo {nome}")

# saudacao(nome)

#Ou
# def saudacao():
#     nome = input("Digite seu nome: ")
#     print(f"Seja bem-vindo {nome}")

# saudacao()  # Agora não precisa passar nada

# ATIVIDADE PRÁTICA 2
# Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.

# def saudacao_por_horario(hora):
#     if 0 <= hora < 12:
#         print("Bom dia!")
#     elif 12 <= hora < 18:
#         print("Boa tarde!")
#     elif 18 <= hora <= 23:
#         print("Boa noite!")
#     else:
#         print("Horário inválido!")

# # Programa principal
# hora_atual = int(input("Digite a hora atual (0 a 23): "))
# saudacao_por_horario(hora_atual)

# ATIVIDADE PRÁTICA 3
# Crie uma função que receba dois números e retorne asoma deles.


# Função que recebe dois números e retorna a soma
# def soma_dois_numeros(num1, num2):
#     return num1 + num2

# # Entrada de dados
# numeros = []  # Lista para armazenar os números
# for i in range(2):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     numeros.append(numero)
    


# # Chamada da função
# resultado = soma_dois_numeros(numeros[0], numeros[1])

# # Saída
# print(f"A soma é: {resultado}")

# #Utilizando o SUM

# # Entrada de dados: pedindo 2 números e guardando em uma lista
# numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(2)]

# # Soma usando a função sum()
# resultado = sum(numeros)

# # Saída
# print(f"A soma é: {resultado}")


# ATIVIDADE PRÁTICA 4
# Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

# Função que recebe dois números e retorna a soma
# def subtrair_dois_numeros(num1, num2):
#     return num1 - num2

# Entrada de dados
# numeros = []  # Lista para armazenar os números
# for i in range(2):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     numeros.append(numero)
    
# # Chamada da função
# resultado = subtrair_dois_numeros(numeros[0], numeros[1])

# # Saída
# print(f"A subtração é: {resultado}")

# ATIVIDADE PRÁTICA 5
# Crie uma função que receba dois números e retorne a multiplicação deles.

# Função que recebe dois números e retorna a soma
# def multiplica_dois_numeros(num1, num2):
#     return num1 * num2

# # Entrada de dados
# numeros = []  # Lista para armazenar os números
# for i in range(2):
#     numero = float(input(f"Digite o {i+1}º número: "))
#     numeros.append(numero)
    
# # Chamada da função
# resultado = multiplica_dois_numeros(numeros[0], numeros[1])

# # Saída
# print(f"A multiplicação é: {resultado}")

# DESAFIO PRÁTICO - Calculadora

# Crie uma calculadora com opções de soma, multiplicação,
# subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para
# realizar os cálculos.

# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse
# exercício.

# --- Funções de unidade lógica (cálculos) ---
# def soma(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# def multiplicacao(a, b):
#     return a * b

# def divisao(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Erro: Divisão por zero!"

# # --- Função de rotina: ler dois números ---
# def ler_numeros():
#     a = float(input("Digite o 1º número: "))
#     b = float(input("Digite o 2º número: "))
#     return a, b

# # --- Função de rotina: mostrar menu ---
# def mostrar_menu():
#     print("\nEscolha uma operação:")
#     print("1 - Soma")
#     print("2 - Subtração")
#     print("3 - Multiplicação")
#     print("4 - Divisão")
#     print("5 - Sair")

# # --- Programa principal ---
# while True:
#     mostrar_menu()
#     opcao = input("Digite a opção desejada: ")
    
#     if opcao == "5":
#         print("Saindo da calculadora. Até logo!")
#         break
    
#     if opcao in ["1", "2", "3", "4"]:
#         n1, n2 = ler_numeros()
        
#         if opcao == "1":
#             print(f"Resultado: {soma(n1, n2)}")
#         elif opcao == "2":
#             print(f"Resultado: {subtracao(n1, n2)}")
#         elif opcao == "3":
#             print(f"Resultado: {multiplicacao(n1, n2)}")
#         elif opcao == "4":
#             print(f"Resultado: {divisao(n1, n2)}")
#     else:
#         print("Opção inválida! Tente novamente.")

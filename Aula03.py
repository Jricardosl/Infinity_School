# Exemplos:

# soma = 0
# numero = 1
# while numero <= 10:
#     soma += numero
#     numero += 1
# print("A soma dos números de 1 a 10 é:",soma)

# senha = ""
# while senha != "1234":
#     senha = input("Digite a senha: ")
# print("Senha correta")

# Atividade 01:
# Contagem de 1 a 10:
# Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.

# contador = 1
# while contador <=10:
#    print(contador)
#    contador +=1

# Atividade 02:
# Soma de números de 1 a 100:
# Escreva um programa que use um laço while para somar os números de 01 a 100 e exiba o resultado.

# soma = 0
# numero = 1
# while numero <= 100:
#     soma += numero
#     numero += 1
# print("A soma dos números de 1 a 100 é:",soma)

#Atividade 03:
#Tabuada de um número:
# Faça um programa que solicite um número ao usuário e use um laço
# while para exibir a tabuada desse número (de 01 a 10).

# numero = int(input("Digite um número para ver a tabuada: "))
# contador = 1
# print(f"Segue a tabuada de {numero}:\n")
# while contador <= 10:
#     resultado = numero * contador
#     print(f"{numero} x {contador} = {resultado}")
#     contador += 1

# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# um contagem regressiva de 10 até 1 e, em seguinda, exiba "Feliz Ano Novo".

# contador = 10
# print("Contagem regressive em ... ")

# while contador >= 1:
#     print(contador)
#     contador -= 1
    
# print("Feliz Ano Novo")

# Um implemento no programa de contagem:
# Um programa de contagem regressiva que:
# Conta de 1 em 1 (você pode mudar o passo)
# Dá uma pausa de 1 segundo entre os números
# No final mostra “Feliz Ano Novo!” colorido
# E toca um som simples (no Windows)

# import time #para usar time.sleep(1) e pausar 1 segundo.

# try:
#     import winsound  # Só funciona no Windows, toca um beep no Windows.
#     som_disponivel = True
# except ImportError:
#     som_disponivel = False

# contador = 10
# passo = 1  # Pode mudar para 2, 3, 5 etc. Obs: controla de quanto em quanto a contagem diminui.

# print("\033[1;33mContagem regressiva...\033[m\n")  # Texto amarelo com ANSI escape Obs: comandos para deixar o texto colorido no terminal.

# while contador >= 1:
#     print(contador)
#     if som_disponivel:
#         winsound.Beep(1000, 300)  # Frequência 1000Hz, duração 300ms Obs: Se o módulo não estiver disponível (exemplo: Linux/macOS), o som será ignorado.


#     time.sleep(1)  # Pausa de 1 segundo
#     contador -= passo

# print("\033[1;32mFeliz Ano Novo! 🎆🎉\033[m")  # Texto verde
# if som_disponivel:
#     for i in range(3):
#         winsound.Beep(1500, 500)
#         time.sleep(0.2)

#Exemplo: Veficação de Senha

# senha = ""
# while senha != "12345":
#     senha = input("Digite a senha: ")
#     if senha == "12345":
#         print("Acesso condedido")
#     else:
#         print("Senha incorreta, tente novamente")

#Exemplo: Menu interativo

# opcao = ""
# while opcao != "sair":
#     print("Menu:")
#     print("1. Opção 1")
#     print("2. Opção 2")
#     print("Digite 'sair' para encerrar")
#     opcao = input("Escolha uma opção: ")
#     if opcao == "1":
#         print("Você escolheu a Opção 1.")
#     elif opcao == "2":
#         print("Você escolheu a Opção 2.")
#     elif opcao == "sair":
#         print("Encerrando o programa.")
#     else:
#         print("Opção inválida, tente novamente.")
    
#Atividade 05:
# Contagem até o número inserido:
#     Crie um programa que solicite um número ao usuário e Use
#     um laço while para contar de 1 até o número inserido
#     exibindo apenas os números impares.

# num = int(input ("Digite um número: ")) # Solicita ao usuário um número e converte para inteiro com int()
# contador = 1
# print ("Números ímpares de 1 até", num,":")
# while contador <= num:
#     if contador % 2 !=0:
#         print (contador)
#     contador +=1


# Atividade 06:
# Soma de números positivos:
#     Escreva um programa que solicite números ao usuário até
#     que ele digite um número negativo, somando apenas os números positivos inseridos.

# soma = 0
# while True:
#     numero = int(input ("Digite um número (negativo para sair): "))
#     if numero < 0:
#         break
#     soma += numero
# print("A soma dos números positivos é:", soma)

#Mostrando os números digitados
# soma = 0
# numeros_digitados = []

# while True:
#     numero = int(input("Digite um número (negativo para sair): "))
    
#     if numero < 0:
#         break

#     soma += numero
#     numeros_digitados.append(numero)

# print("\nNúmeros positivos digitados:", numeros_digitados)
# print("Soma dos números positivos:", soma)

#Atidade 07:
# Tabuada com condicional:
#     Faça um programa que solicite um número ao usuário e Use
#     um laço while para exibir a tabuada desse número (de 1 a 10),
#     mas apenas para os resultados que forem múltiplos de 3.

# numero = int(input("Digite um número para ver a tabuada (somente múltiplos de 3): "))
# contador = 1
# print(f"\nSegue a tabuada de {numero} (múltiplos de 3):\n")
# while contador <= 10:
#     resultado = numero * contador
#     if resultado % 3 == 0: # Verifica se o resultado é múltiplo de 3 (ou seja, se o resto da divisão por 3 é 0).
#        print(f"{numero} x {contador} = {resultado}")
#     contador += 1


# Atividade 08:
# Média de notas:
#     Desenvolva um programa que solicite as notas dos alunos até
#     que o usuário digite -1. Calcule e exiba a média das notas inseridas.

# soma = 0 #somará as notas.
# quantidade =0 #contará quantas notas foram inseridas.
# while True:
#     nota = float(input ("Digite a nota do aluno (-1 para encerrar): "))
#     if nota == -1:
#         break
#     soma += nota
#     quantidade +=1

# if quantidade > 0:
#     media = soma / quantidade
#     print (f"\nMédia das notas: {media:.2f}")
# else:
#     print("\nNenhuma nota foi inserida")

#Exemplo: Jogo de adininhação

# numero_secreto = 7
# palpite = None

# while palpite != numero_secreto:
#     palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))   
#     if palpite == numero_secreto:
#         print("Parabéns! Você acertou.")
#         break
#     else:
#         print ("Errado, tente novamente.")

#Extra:
#Jogo de adivinhação aleatório    
# import random

# numero_secreto = random.randint(1, 10)  # número aleatório entre 1 e 10
# tentativas_restantes = 3  # limite de tentativas

# print("🎯 Jogo de Adivinhação")
# print("Você tem 3 tentativas para adivinhar o número secreto entre 1 e 10.\n")

# while tentativas_restantes > 0:
#     try:
#         palpite = int(input("Digite seu palpite: "))
#     except ValueError:
#         print("⛔ Por favor, digite um número válido.")
#         continue

#     if palpite == numero_secreto:
#         print("🎉 Parabéns! Você acertou o número secreto!")
#         break
#     else:
#         tentativas_restantes -= 1
#         if palpite < numero_secreto:
#             print("🔼 O número secreto é **maior**.")
#         else:
#             print("🔽 O número secreto é **menor**.")
        
#         if tentativas_restantes > 0:
#             print(f"❗ Você ainda tem {tentativas_restantes} tentativa(s).\n")
#         else:
#             print(f"💥 Fim de jogo! O número secreto era {numero_secreto}.")


# Atividade 09:
# Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10 
# e termine quando atigir 10.          

# contador = 1 #Inicializa o contador com 1.
# while contador <=10: #Executa o bloco de código enquanto o valor do contador for menor ou igual a 10.
#     print(contador) #Mostra o valor atual do contador.
#     contador +=1 #Incrementa o contador em 1 a cada repetição.
# print("Fim da contagem!")


# Atividade 10:
# Soma até 50:
# Escreva um programa que use um laço while para somar 
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.

# soma = 0
# numero = 1
# while soma < 50: #Assim que soma atingir ou ultrapassar 50, o laço termina.
#      soma += numero
#      numero += 1 #Isso faz com que o próximo número a ser somado seja o próximo consecutivo (2, 3, 4...).
# print("A soma acumulada é:", soma)
# print("Último número somado foi:", numero - 1)

#Atividade 11:
#Entrada Válida:
#Crie um programa que solicite ao usuário um número entre 1 e 10.
#Continue pedido até o usuário forneça um valor válido.

# numero = int(input("Digite um número entre 1 e 10: "))
# while numero < 1 or numero > 10: #Enquanto o número não estiver entre 1 e 10, o laço continua. uso do or (ou), indicando duas condições
#     print("Número inválido! Tente novamente.")
#     numero = int(input("Digite um número entre 1 e 10: "))

# print("Entrada válida:", numero)

#Atividade 12:
#Senha correta:
#Desenvolva um programa que peça ao usuário para digitar uma senha e continue pedindo até que 
#a senha correta(previamente definida) seja inserida.

# senha = ""
# senha = input("Digite a senha: ")
# while senha != "1234":
#     print("Senha incorreta, tente novamente!")
#     senha = input("Digite a senha: ")
# print("Senha correta")

#DESAFIOS PRÁTICOS

#PAGINA 27
#1-Soma de números pares:
#Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

# soma = 0
# numero = 1
# while numero <= 100:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1
# print("A soma dos números pares entre 1 a 100 é:",soma)

#Outra forma
# soma = 0
# numero = 2
# while numero <= 100:
#     soma += numero
#     numero += 2
# print("A soma dos números pares entre 1 a 100 é:", soma)

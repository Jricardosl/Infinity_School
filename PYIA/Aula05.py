# ATIVIDADE 1


# Crie um programa que solicita ao usuário que insira três
# notas e, em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como argumentos e retornar a média. Por fim, o
# programa deve imprimir a média calculada.


# def calcular_media(nota1, nota2, nota3):
#     media = (nota1 + nota2 + nota3) / 3
#     return media

# nota1 = float(input("Digite a primeira nota: "))

# nota2 = float(input("Digite a segunda nota: "))

# nota3 = float(input("Digite a terceira nota: "))

# media = calcular_media(nota1, nota2, nota3)

# print(f"A média das notas é: {media:.2f}")


# ATIVIDADE PRÁTICA 2

# Crie um programa que define uma função
# calcular_area_retangulo que recebe dois argumentos,
# comprimento e largura de um retângulo, e retorna a
# área desse retângulo. Em seguida, o programa deve
# solicitar ao usuário que insira o comprimento e a
# largura e imprimir a área calculada.


# def calcular_area_retangulo(comprimento, largura):

#     area = comprimento * largura

#     return area

# comprimento = float(input("Digite o comprimento do retângulo: "))
# largura = float(input("Digite a largura do retângulo: "))
# area = calcular_area_retangulo(comprimento, largura)
# print(f"A área do retângulo é: {area:.2f}")


# # args

# def somar_numeros(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado
# print(somar_numeros(1, 2, 3, 4, 5))  # Saída: 15
# print(somar_numeros(10, 20))        # Saída: 30

# kargs

# def imprimir_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")
# imprimir_info(nome="Alice", idade=30, cidade="São Paulo")

# programa deve chamar a função e exibir o resultado.
# Saída:
# nome: Alice   
# idade: 30
# cidade: São Paulo

# #args e kargs juntos

# def funcao_exemplo(*args, **kwargs):

#     print("Argumentos posicionais (args):", args)
#     print("Argumentos nomeados (kwargs):", kwargs)

# funcao_exemplo(1, 2, 3, nome="Alice", idade=30)

# # Saída:

# Argumentos posicionais (args): (1, 2, 3)      

# Argumentos nomeados (kwargs): {'nome': 'Alice', 'idade': 30}


# ATIVIDADE PRÁTICA 3

# Crie uma função chamada concatenar_strings que
# aceita um número variável de strings como argumentos
# posicionais (usando *args). A função deve concatenar
# todas as strings em uma única string e retorná-la.

# def concatenar_strings(*args):
#     resultado = ""
#     for string in args:
#         resultado += string
#     return resultado

# # print(concatenar_strings("Olá, ", "mundo", "!"))  # Saída: "Olá, mundo!"
# # print(concatenar_strings("Python", " é ", "incrível.")) # Saída: "Python é incrível."


# Outro exemplo de uso da função:

# O programa deve solicitar ao usuário que insira
# várias strings, chamar a função concatenar_strings
# com essas strings e imprimir o resultado.

# strings_usuario = input("Digite várias strings separadas por vírgula: ").split(",")
# resultado_concatenado = concatenar_strings(*[s.strip() for s in strings_usuario])
# print("Strings concatenadas:", resultado_concatenado)

# # Saída:

# Digite várias strings separadas por vírgula: Olá, mundo, !    

# Strings concatenadas: Olá, mundo!

# ATIVIDADE PRÁTICA 4

# Crie uma função que aceita uma lista de números e use
# a função map para retornar uma nova lista contendo o
# dobro de cada número na lista de entrada.

# def dobrar_numeros(numeros):
#     return list(map(lambda x: x * 2, numeros))

# numeros = [1, 2, 3, 4, 5]

# print(dobrar_numeros(numeros))  # Saída: [2, 4, 6, 8, 10]


# Outro exemplo de uso da função:

# O programa deve solicitar ao usuário que insira
# vários números separados por vírgula, chamar a
# função dobrar_numeros com esses números e imprimir o
# resultado.


# entrada_usuario = input("Digite vários números separados por vírgula: ")
# lista_numeros = [int(num.strip()) for num in entrada_usuario.split(",")]    
# resultado_dobrado = dobrar_numeros(lista_numeros)
# print("Números dobrados:", resultado_dobrado)

# # Saída:

# Digite vários números separados por vírgula: 1, 2, 3, 4, 5

# Números dobrados: [2, 4, 6, 8, 10]


# ATIVIDADE PRÁTICA 5

# Crie uma função que aceita uma lista de números e use
# a função filter para retornar uma nova lista contendo

# apenas os números pares da lista de entrada.

# def filtrar_numeros_pares(numeros):
#     return list(filter(lambda x: x % 2 == 0, numeros))  

# # numeros = [1, 2, 3, 4, 5, 6]
# # print(filtrar_numeros_pares(numeros))  # Saída: [2, 4, 6]


# # Outro exemplo de uso da função:  

# # O programa deve solicitar ao usuário que insira
# # vários números separados por vírgula, chamar a
# # função filtrar_numeros_pares com esses números e
# # imprimir o resultado.

# entrada_usuario = input("Digite vários números separados por vírgula: ")

# lista_numeros = [int(num.strip()) for num in entrada_usuario.split(",")]    

# resultado_pares = filtrar_numeros_pares(lista_numeros)

# print("Números pares:", resultado_pares)    

# # # Saída:

# # Digite vários números separados por vírgula: 1, 2, 3          

# # Números pares: [2, 4, 6], 4, 5, 6

# Números pares: [2, 4, 6]

# # ATIVIDADE PRÁTICA 6

# # Crie uma função que aceita uma lista de strings e use a
# # função reduce (importada de functools) para encontrar
# # a maior string na lista.

# from functools import reduce

# def encontrar_maior_string(strings):
#     return reduce(lambda a, b: a if len(a) > len(b) else b, strings)
# strings = ["maçã", "banana", "abacaxi", "laranja"]
# print(encontrar_maior_string(strings))  # Saída: "abacaxi"


# Outro exemplo de uso da função:

# O programa deve solicitar ao usuário que insira
# várias strings separadas por vírgula, chamar a
# função encontrar_maior_string com essas strings e
# imprimir o resultado.

# entrada_usuario = input("Digite várias strings separadas por vírgula: ")
# lista_strings = [s.strip() for s in entrada_usuario.split(",")]
# resultado_maior = encontrar_maior_string(lista_strings)
# print("A maior string é:", resultado_maior)    

# # Saída:

# Digite várias strings separadas por vírgula: maçã, banana, abac   axi, laranja

# A maior string é: abacaxi    


# ATIVIDADE PRÁTICA 7

# Crie uma função chamada criar_lista_de_compras que
# aceita um número variável de itens de compras como
# argumentos posicionais (usando *args). A função deve
# criar e retornar uma lista de compras que contenha
# todos os itens fornecidos.

# def criar_lista_de_compras(*args):
#     lista_de_compras = list(args)
#     return lista_de_compras 

# Exemplo de uso da função: 
# print(criar_lista_de_compras("maçã", "banana", "leite"))  # Saída: ["maçã", "banana", "leite"]    
# print(criar_lista_de_compras("pão", "ovos"))              # Saída: ["pão", "ovos"]

# Outro exemplo de uso da função:   
    
# O programa deve solicitar ao usuário que insira
# vários itens de compras separados por vírgula,    
# chamar a função criar_lista_de_compras com esses
# itens e imprimir o resultado. 

# entrada_usuario = input("Digite vários itens de compras separados por vírgula: ")
# lista_itens = [item.strip() for item in entrada_usuario.split(",")]     
# resultado_lista = criar_lista_de_compras(*lista_itens)
# print("Lista de compras:", resultado_lista)         


# ATIVIDADE PRÁTICA 8

# Crie uma função que aceite dois números e uma
# operação (por exemplo, adição, subtração,
# multiplicação, divisão) como argumentos e use funções
# lambda para realizar a operação especificada. A função
# deve retornar o resultado da operação.
# def calcular(num1, num2, operacao):
#     operacoes = {
#         "adição": lambda x, y: x + y,
#         "subtração": lambda x, y: x - y,
#         "multiplicação": lambda x, y: x * y,
#         "divisão": lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
#     }
#     if operacao in operacoes:
#         return operacoes[operacao](num1, num2)
#     else:
#         return "Operação inválida"
# # Exemplo de uso da função:
# # print(calcular(10, 5, "adição"))          # Saída:    15      
# # print(calcular(10, 5, "subtração"))       # Saída:    5
# # print(calcular(10, 5, "multiplicação"))    # Saída:    50
# # print(calcular(10, 5, "divisão"))          # Saída:    2.0
# # print(calcular(10, 0, "divisão"))          # Saída:   "Erro: Divisão por zero"    
# # print(calcular(10, 5, "modulo"))           # Saída:   "Operação inválida"     

# # Outro exemplo de uso da função:   

# # O programa deve solicitar ao usuário que insira
# # dois números e uma operação, chamar a função      
# # calcular com esses valores e imprimir o resultado.  
      
# # num1 = float(input("Digite o primeiro número: "))
# # num2 = float(input("Digite o segundo número: "))    
# # operacao = input("Digite a operação (adição, subtração, multiplicação, divisão): ").strip().lower()
# # resultado = calcular(num1, num2, operacao)      
# # print("Resultado:", resultado)  

# # DESAFIO PRÁTICO

# # Processador de Texto - passo 1

# # Crie um processador de texto simples que realiza várias operações
# # em um texto de entrada, como contar palavras, contar letras,
# # inverter o texto e substituir palavras-chave.

# # Requisitos:

# # Crie uma função chamada processador_texto que aceite uma
# # string de texto como argumento.

# # def processador_texto(texto):
    
# #     def contar_palavras(texto):
# #         palavras = texto.split()
# #         return len(palavras)

# #     def contar_letras(texto):
# #         letras = [char for char in texto if char.isalpha()]
# #         return len(letras)

# #     def inverter_texto(texto):
# #         return texto[::-1]

# #     def substituir_palavra(texto, palavra_antiga, palavra_nova):
# #         return texto.replace(palavra_antiga, palavra_nova)

# #     num_palavras = contar_palavras(texto)
# #     num_letras = contar_letras(texto)
# #     texto_invertido = inverter_texto(texto)
# #     texto_substituido = substituir_palavra(texto, "Python", "Java")

# #     return {
# #         "Número de palavras": num_palavras,
# #         "Número de letras": num_letras,
# #         "Texto invertido": texto_invertido,
# #         "Texto com substituição": texto_substituido
# #     } 
          
# # A função deve realizar as seguintes operações:    
# # Contar o número de palavras no texto.
# # Contar o número de letras no texto.   
# # Inverter o texto.
# # Substituir todas as ocorrências de uma palavra-chave por outra palavra.   
# # A função deve retornar um dicionário contendo os resultados de cada operação.     
# # O programa deve solicitar ao usuário que insira um texto,
# # chamar a função processador_texto com esse texto e imprimir os resultados.   
 
# # Exemplo de uso da função:     
# # texto_entrada = "Python é uma linguagem de programação incrível."
# # resultados = processador_texto(texto_entrada)     
# # for chave, valor in resultados.items():
# #     print(f"{chave}: {valor}")    
        
# # Saída:
# # Número de palavras: 7 
# # Número de letras: 39
# # Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# # Texto com substituição: Java é uma linguagem de programação incrível. 

# # Outro exemplo de uso da função:       
# # O programa deve solicitar ao usuário que insira
# # um texto, chamar a função processador_texto com
# # esse texto e imprimir os resultados.
    
# # texto_entrada = input("Digite um texto: ")
# # resultados = processador_texto(texto_entrada)     
# # for chave, valor in resultados.items():
# #     print(f"{chave}: {valor}")    
# # # Saída:    
# # Digite um texto: Python é uma linguagem de programação incrível.
# # Número de palavras: 7
# # Número de letras: 39      
# # Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# # Texto com substituição: Java é uma linguagem de programação incrível. 
        

# # DESAFIO PRÁTICO

# # Processador de Texto - passo 2

# # A função deve aceitar uma série de operações como argumentos
# # de palavra-chave, usando **kwargs. As operações podem incluir
# # "contar_palavras","contar_letras","inverter_texto" e "substituir_palavra".

# # Use funções lambda para realizar as operações de acordo com
# # as palavras-chave especificadas nos argumentos de palavra-chave.

# def processador_texto(texto, **kwargs):
#     resultados = {}

#     if kwargs.get("contar_palavras"):
#         contar_palavras = lambda t: len(t.split())
#         resultados["Número de palavras"] = contar_palavras(texto)

#     if kwargs.get("contar_letras"):
#         contar_letras = lambda t: len([char for char in t if char.isalpha()])
#         resultados["Número de letras"] = contar_letras(texto)

#     if kwargs.get("inverter_texto"):
#         inverter_texto = lambda t: t[::-1]
#         resultados["Texto invertido"] = inverter_texto(texto)

#     if "substituir_palavra" in kwargs:
#         palavra_antiga, palavra_nova = kwargs["substituir_palavra"]
#         substituir_palavra = lambda t, old, new: t.replace(old, new)
#         resultados["Texto com substituição"] = substituir_palavra(texto, palavra_antiga, palavra_nova)

#     return resultados
# Exemplo de uso da função:
# texto_entrada = "Python é uma linguagem de programação incrível."
# resultados = processador_texto(texto_entrada, contar_palavras=True, contar_letras=True, inverter_texto=True, substituir_palavra=("Python", "Java"))
# for chave, valor in resultados.items():   
#     print(f"{chave}: {valor}")    
# Saída:        
# Número de palavras: 7
# Número de letras: 39      
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# Texto com substituição: Java é uma linguagem de programação incrível.

# Outro exemplo de uso da função:       
# O programa deve solicitar ao usuário que insira
# um texto e as operações desejadas, chamar a   
# função processador_texto com esses valores e
# # imprimir os resultados.               
# texto_entrada = input("Digite um texto: ")
# contar_palavras = input("Contar palavras? (s/n): ").strip().lower   
# contar_letras = input("Contar letras? (s/n): ").strip().lower()
# inverter_texto = input("Inverter texto? (s/n): ").strip().lower()
# substituir = input("Substituir palavra? (s/n): ").strip().lower
# kwargs = {}
# if contar_palavras == 's':  
#     kwargs["contar_palavras"] = True
# if contar_letras == 's':
#     kwargs["contar_letras"] = True  
# if inverter_texto == 's':
#     kwargs["inverter_texto"] = True
# if substituir == 's':
#     palavra_antiga = input("Digite a palavra a ser substituída: ").strip()
#     palavra_nova = input("Digite a nova palavra: ").strip()
#     kwargs["substituir_palavra"] = (palavra_antiga, palavra_nova)
# resultados = processador_texto(texto_entrada, **kwargs)
# for chave, valor in resultados.items():
#     print(f"{chave}: {valor}")  
# Saída:
# Digite um texto: Python é uma linguagem de programação incrível.  
# Contar palavras? (s/n): s
# Contar letras? (s/n): s   
# Inverter texto? (s/n): s
# Substituir palavra? (s/n): s      
# Digite a palavra a ser substituída: Python
# Digite a nova palavra: Java       
# Número de palavras: 7
# Número de letras: 39      
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP        
# Texto com substituição: Java é uma linguagem de programação incrível. 
# O programa deve solicitar ao usuário que insira
# um texto, chamar a        
# função processador_texto com esse texto e imprimir os resultados.   
# Saída:        
# Digite um texto: Python é uma linguagem de programação incrível.  
# Número de palavras: 7
# Número de letras: 39      
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# Texto com substituição: Java é uma linguagem de programação incrível. 


# DESAFIO PRÁTICO

# Processador de Texto - passo 3

# Se a operação "substituir_palavra" for especificada, a função
# deve aceitar uma palavra-chave adicional, como "substituir_palavra" e "nova_palavra", 
# para realizar a substituição em todo o texto.

# A função deve retornar o texto resultante após todas as operações.

# def processador_texto(texto, **kwargs):
#     resultados = {}

#     if kwargs.get("contar_palavras"):
#         contar_palavras = lambda t: len(t.split())
#         resultados["Número de palavras"] = contar_palavras(texto)

#     if kwargs.get("contar_letras"):
#         contar_letras = lambda t: len([char for char in t if char.isalpha()])
#         resultados["Número de letras"] = contar_letras(texto)

#     if kwargs.get("inverter_texto"):
#         inverter_texto = lambda t: t[::-1]
#         resultados["Texto invertido"] = inverter_texto(texto)

#     if "substituir_palavra" in kwargs and "nova_palavra" in kwargs:
#         palavra_antiga = kwargs["substituir_palavra"]
#         palavra_nova = kwargs["nova_palavra"]
#         substituir_palavra = lambda t, old, new: t.replace(old, new)
#         resultados["Texto com substituição"] = substituir_palavra(texto, palavra_antiga, palavra_nova)

#     return resultados
# Exemplo de uso da função:
# texto_entrada = "Python é uma linguagem de programação incrível."     
# resultados = processador_texto(texto_entrada, contar_palavras=True, contar_letras=True, inverter_texto=True, substituir_palavra="Python", nova_palavra="Java")
# for chave, valor in resultados.items():
#     print(f"{chave}: {valor}")
# Saída:        
# Número de palavras: 7
# Número de letras: 39      
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# Texto com substituição: Java é uma linguagem de programação incrível. 
# Outro exemplo de uso da função:       
# O programa deve solicitar ao usuário que insira   
# um texto e as operações desejadas, chamar a
# função processador_texto com esses valores e
# imprimir os resultados.   
# texto_entrada = input("Digite um texto: ")
# contar_palavras = input("Contar palavras? (s/n): ").strip().lower 
# contar_letras = input("Contar letras? (s/n): ").strip().lower()
# inverter_texto = input("Inverter texto? (s/n): ").strip().lower()
# substituir = input("Substituir palavra? (s/n): ").strip().lower       
# kwargs = {}
# if contar_palavras == 's':
#     kwargs["contar_palavras"] = True
# if contar_letras == 's':      
#     kwargs["contar_letras"] = True
# if inverter_texto == 's':     
#     kwargs["inverter_texto"] = True
# if substituir == 's': 
#     palavra_antiga = input("Digite a palavra a ser substituída: ").strip()
#     palavra_nova = input("Digite a nova palavra: ").strip()   
#     kwargs["substituir_palavra"] = palavra_antiga 
#     kwargs["nova_palavra"] = palavra_nova
# resultados = processador_texto(texto_entrada, **kwargs)   
# for chave, valor in resultados.items():
#     print(f"{chave}: {valor}")    
# # Saída:    
# Digite um texto: Python é uma linguagem de programação incrível.  
# Contar palavras? (s/n): s 
# Contar letras? (s/n): s   
# Inverter texto? (s/n): s
# Substituir palavra? (s/n): s
# Digite a palavra a ser substituída: Python
# Digite a nova palavra: Java   
# Número de palavras: 7
# Número de letras: 39  
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# Texto com substituição: Java é uma linguagem de programação incrível. 
# O programa deve solicitar ao usuário que insira
# um texto, chamar a        
# função processador_texto com esse texto e imprimir os resultados.   
# Saída:    
# Digite um texto: Python é uma linguagem de programação incrível.  
# Número de palavras: 7     
# Número de letras: 39
# Texto invertido: .elbirnic oãçargorp ed agnemal a amu é nohtyP
# Texto com substituição: Java é uma linguagem de programação incrível.
 
 
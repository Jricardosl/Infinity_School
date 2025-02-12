"""Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda."""

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print(f"A primeira idade ({idade1}) é maior que a segunda idade ({idade2}).")
elif idade1 < idade2:
    print(f"A primeira idade ({idade1}) é menor que a segunda idade ({idade2}).")
else:
    print(f"As duas idades são iguais ({idade1}).") 


"""Atividade 02:
Verificar Igualdade de Strings:
Peça ao usuário duas palavras e use operadores
de comparação para verificar se elas são iguais"""

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavra1 == palavra2:
    print("As palavras são iguais.")
else:
    print("As palavras são diferentes.")

#Pratique e Aprenda

"""Objetivo: Criar um Programa que Peça as 4 Notas
Bimestrais e Mostre a Média
Instruções:
1 - Solicitar as Notas do Usuário:
Use a função input() para pedir ao usuário que insira
cada uma das quatro notas bimestrais. Converta a
entrada do usuário de string para um número (float)
para permitir cálculos.
2 - Calcular a Média das Notas:
Some as quatro notas e divida o resultado
por quatro para obter a média.
3 - Mostrar a Média Calculada para o Usuário:
Use a função print() para exibir a média das notas
calculada."""

nota1 = float(input("Informe a nota do primeiro bimestre: "))
nota2 = float(input("Informe a nota do segundo bimestre: "))
nota3 = float(input("Informe a nota do terceiro bimestre: "))
nota4 = float(input("Informe a nota do quarto bimestre: "))
media = ((nota1+nota2+nota3+nota4)/4)

print ("Média final:", media)

"""Para formatar a média em duas casas decimais"""

print(f"Média final: {media:.2f}")


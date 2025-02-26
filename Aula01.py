# print("Olá, mundo!")

#Atividade 1
# Criando a variável chamada 'saudacao'
#saudacao = "Hello World"

# Imprimindo o valor da variável
#print(saudacao)

# Verificando o tipo da variável
#print(type(saudacao))

#Atividade 2

# Crie um programa que peça ao usuário para digitar:
#1.Seu nome;
#2.Sua idade;
#3.Sua altura;
#4.Em seguida, imprima esses valores e seus respectivos tipos.

#Objetivo: Praticar a declaração e uso de variáveis de diferentes tipos,
#além de aprender a verificar e imprimir seus tipos em Python.
#Observação: Conhecer e utilizar diferentes tipos de variáveis
#é fundamental para manipular dados de maneira eficaz.

nome = input("Meu nome é: ")
idade = input("Tenho a idade de: ")
altura = input("e minha altura é de: ")

print(type(nome))
print(type(idade))
print(type(altura))

#Pratica 1

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

<<<<<<< HEAD
print(f"Média final: {media:.2f}")
=======
>>>>>>> 588cb77 (Atividades de 7 a 10)

#Prática 2

#Pratique e Aprenda

"""Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
20 dias no mês)."""

"""Instruções:
1 - Solicitar o Salário Mensal:
Use a função input() para pedir ao usuário que insira quanto
ele ganha por mês. Converta a entrada do usuário de string
para um número (float) para permitir cálculos.
2 - Solicitar o Número de Horas Trabalhadas na Semana:
Use a função input() para pedir ao usuário que insira o número
de horas trabalhadas na semana. Converta a entrada do
usuário de string para um número (float) para permitir
cálculos.
3 - Calcular o Total de Horas Trabalhadas no Mês:
Multiplique o número de horas trabalhadas na semana por 4
para obter o total de horas trabalhadas no mês.
4 - Calcular o Salário por Hora:
Divida o salário mensal pelo total de horas
trabalhadas no mês para obter o salário por
hora.
5 - Mostrar o Salário por Hora Calculado
para o Usuário:
Use a função print() para exibir o salário por
hora calculado."""

salariomensal = float(input("Quanto você ganha por mês: "))
horasemana = float(input("Número de Horas Trabalhadas na Semana: "))
horatrabmes = horasemana * 4
salarioporhora = salariomensal / horatrabmes

print (f"Salário por hora calculado: {salarioporhora:.2f}")

#Prática 3

"""Pratique e Aprenda"""

"""Objetivo: Peça ao usuário para digitar seu nome, idade e cidade
natal. Use uma f-string para formatar e exibir uma mensagem
com essas informações.
Instruções:
1 - Solicitar o Nome do Usuário:
Use a função input() para pedir ao usuário que insira seu nome.
2 - Solicitar a Idade do Usuário:
Use a função input() para pedir ao usuário que insira sua idade.
Converta a entrada do usuário de string para um número (int).
3 - Solicitar a Cidade Natal do Usuário:
Use a função input() para pedir ao usuário que insira sua cidade
natal.
4 - Formatar e Exibir a Mensagem com f-string:
Use uma f-string para formatar a mensagem com as informações
fornecidas pelo usuário e exiba a mensagem usando a função
print()"""

nome = input("Qual seu nome: ")
idade = int(input("qual sua idade: "))
cidade = input("Qual sua cidade natal: ")

print (f"Me chamo {nome} tenho {idade} anos e moro em {cidade}.")

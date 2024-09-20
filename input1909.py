# a = input("Digite algo: ") #input não é muito usado
# print(a) #foi atribuído o valor a uma variável e mostrou na tela
# print("Fim")

#exibir o nome do usuario e idade
# nomeUsuario = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# print ("O meu nome é", nomeUsuario, "e tenho", idade, "anos")

#imprima a
# num1 = int(input("Digite um número inteiro: "))
# #outra forma de fazer: num1 = int(num1)
# num2 = int(input("Digite outro número inteiro: "))
# print("Essa é a soma de dois números inteiros:", num1+num2)

#calcule o valor de u bonus por anos de serviço
# anos = int(input("Digite quantos anos trabalhou na empresa: "))
# valorano = 700
# print("O seu bônus é: ", valorano*anos)

#ler o valor em metros e exibir convertido em milímetros
# metro= float(input("Digite o valor em metros: "))
# print("O valor de metros em milímetros é: ", metro*1000)

#calcule o tempo de uma viagem de carro
# dist = float(input("Digite a distância: "))
# vm = float(input("Digite a velocidade média: "))
# print("O tempo da viagem será: ", dist/vm)

#qtd km percorridos pelo carro e a qtd de dia
#calcular o preço a pagar
# 60 por dia 0,15km rodado
# km = float(input("Digite quantos km percorreu: "))
# dia = float(input("Digite quantos dias utilizou o carro: "))
# carro = 60*dia + 0.15*km
# print("O preço a pagar é: ", carro)

#ler dois int e imprima true se forem diferentes e

# n1 = int(input("Digite o n1: "))
# n2 = int(input("Digite o n2: "))
# res = (n1%2==0 and n2%2 ==1) or (n1%2==1 and n2%2 ==0)
# res = n1%2 != n2%2
# print(res)

#if else
# n1 = int(input("Digite o n1: "))
# n2 = int(input("Digite o n2: "))
#
# if n1 > n2:
#     print("O número 1 é maior")
#
# if n2 > n1:
#     print("O número 2 é maior")
#
# print("Os números são iguais")

#caso o carro ultrapassar 80km, cobrar 5reais por km
# vcarro = float(input("Digite a velocidade: "))
# limite = 80
# if vcarro > limite:
#     print("Você foi multado. O valor da multa é: ", 5*(vcarro-80)) #parenteses para fazer primeiro


# a = int(input("Digite um número"))
# b = int(input("Digite outro número"))
# if a>b:
#     print(a)
# else:
#     print(b)

#print se o cliente pode contratar um empréstimo

# salario= float(input("Digite o salário: "))
# idade= int(input("Digite a idade: "))
#
# #quando não usar lógico, coloca if dentro de if
# if salario > 1500:
#     if idade > 18:
#         print("Você pode fazer o empréstimo")
#     else:
#         print("Você não pode fazer o empréstimo")

num = int(input("Digite um número: "))
par= (num%2)
#quando iguala alguma coisa, vai ser T ou F, logo
# não vai ter sentido comparar dnv com um número de verdade, vai "repetir"

if par == 0:
    if num <= 100:
        print("O número é par e menor que 100")
    else:
        print("O número é par e maior que 100")
else:
    if num <= 100:
        print("O número é ímpar e menor que 100")
    else:
        print(("O número é ímpar e maior que 100"))






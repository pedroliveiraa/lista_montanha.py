#Lista 1 Python Brasil

#1
print('Olá Mundo!')

#2
numero = int(input('Escreva um número: '))
print('O número escrito é:',numero)

#3
numero1 = int(input('Escreva um número: '))
numero2 = int(input('Escreva outro número: '))

soma = numero1 + numero2;

print('A soma dos dois números é igual a:',soma)

#4
nota1 = float(input('Escreva a primeira nota bimestral: '))
nota2 = float(input('Escreva a segunda nota bimestral: '))
nota3 = float(input('Escreva a terceira nota bimestral: '))
nota4 = float(input('Escreva a quarta nota bimestral: '))

media = (nota1 + nota2 + nota3 + nota4)/4;

print('A média é igual a:',media)

#5
medida_m = float(input('Escreva uma medida em metros: '))

medida_c = medida_m * 100;

print('A medida em centímetros é:',medida_c,'cm')

#6
raio = float(input('Digite o raio do círculo: '))

area = 3.14 * (raio ** 2);

print('A área do círculo é:', area)

#7
lado = float(input('Informe o valor de um lado do quadrado: '))

area = lado * lado;

print('A área do quadrado é:',area,'m²')

print('O dobro desta área é:',(area * 2),'m²')

#8
valor_h = float(input('Digite o valor do salário por hora: '))
horas_t = float(input('Digite o número de horas trabalhadas no mês: '))

salario_t = valor_h * horas_t;

print('O total do seu salário no mês é:', salario_t)

#9
temp_f = float(input('Digite a temperatura em Fahenheit: '))

temp_c = 5 * ((temp_f - 32)/9);

print('A temperatura em Celsius é:',temp_c)

#10
temperatura_c = float(input('Digite a temperatura em graus Celsius: '))

temperatura_f = (temperatura_c * 9/5) + 32;

print('A temperatura em graus Fahrenheit é:', temperatura_f)

#11
num_int_1 = int(input('Digite o primeiro número inteiro: '))
num_int_2 = int(input('Digite o segundo número inteiro: '))
num_real = float(input('Digite o número real: '))

produto = (2 * num_int_1) * (num_int_2/2);
soma = (3 * num_int_1) + num_real;
cubo = num_real ** 3;

print('O produto do dobro do primeiro com metade do segundo é:',produto)
print('A soma do triplo do primeiro com o terceiro é:',soma)
print('O terceiro elevado ao cubo é:',cubo)

#12
altura = float(input('Digite sua altura em metros: '))

peso_ideal = (72.7*altura) - 58;

print(f'Seu peso ideal é: {peso_ideal:.2f} kg')

#13
altura = float(input('Digite sua altura em metros: '))

peso_ideal_h = (72.7*altura) - 58;
peso_ideal_m = (62.1*altura) - 44.7;

print(f'Seu peso ideal se for homem é: {peso_ideal_h:.2f} kg')
print(f'Seu peso ideal se for mulher é: {peso_ideal_m:.2f} kg')

#14
peso = float(input('Digite o peso de peixes em quilos: '))

limite_peso = 50;
excesso = peso - limite_peso;

valor_multa = 0;
if excesso > 0:
    valor_multa = excesso * 4.00;

if excesso <= 0:
    print('Não há excesso de peso')
else:
    print(f'Excesso de peso: {excesso:.2f} kg')
    print(f'Valor da multa a ser pago: {valor_multa:.2f} R$')

#15
valor_hora = float(input('Digite o valor do seu salário por hora: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas;

imposto_renda = salario_bruto * 0.11;
inss = salario_bruto * 0.08;
sindicato = salario_bruto * 0.05;

salario_liquido = salario_bruto - imposto_renda - inss - sindicato;

print(f'Salário Bruto: {salario_bruto:.2f} R$')
print(f'Imposto de Renda: {imposto_renda:.2f} R$')
print(f'INSS: {inss:.2f} R$')
print(f'Sindicato: {sindicato:.2f} R$')
print(f'Salário Líquido: {salario_liquido:.2f} R$')

#16
tamanho_area = float(input('Digite o tamanho da área a ser pintada (em metros quadrados): '))

litros_tinta = tamanho_area / 3;

latas_tinta = int(litros_tinta / 18);
if litros_tinta % 18 != 0:
    latas_tinta += 1;

preco_lata = 80.00;
preco_total = latas_tinta * preco_lata;

print(f'Quantidade de latas de tinta: {latas_tinta}')
print(f'Preço total: {preco_total:.2f} R$')

#17
import math

tamanho_area = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))

litros_tinta = tamanho_area / 6 * 1.1;

latas_18_l = math.ceil(litros_tinta / 18);
preco_latas_18_l = latas_18_l * 80;

galoes_3_6_l = math.ceil(litros_tinta / 3.6);
preco_galoes_3_6_l = galoes_3_6_l * 25;

latas_mistura = math.floor(litros_tinta / 18);
resto_tinta = litros_tinta % 18;
galoes_mistura = math.ceil(resto_tinta / 3.6);
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25);

print(f'Situação 1 - Comprar apenas latas de 18 litros:')
print(f'Quantidade de latas: {latas_18_l}')
print(f'Preço total: R$ {preco_latas_18_l:.2f}')

print(f'Situação 2 - Comprar apenas galões de 3,6 litros:')
print(f'Quantidade de galões: {galoes_3_6_l}')
print(f'Preço total: R$ {preco_galoes_3_6_l:.2f}')

print(f'Situação 3 - Misturar latas e galões:')
print(f'Quantidade de latas: {latas_mistura}')
print(f'Quantidade de galões: {galoes_mistura}')
print(f'Preço total: R$ {preco_mistura:.2f}')

#18
tamanho_arquivo = float(input('Digite o tamanho do arquivo para download em MB: '))

velocidade_internet = float(input('Digite a velocidade do link de internet em Mbps: '))

tamanho_arquivo_mb = tamanho_arquivo * 8;

temp_download_m = tamanho_arquivo_mb / velocidade_internet / 60;

print(f'O tempo de download do arquivo é de {temp_download_m:.2f} min.')

#Lista 2 Python Brasil

#1
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
  print('O maior número é:',num1)

if num1 < num2:
  print('O maior número é:',num2)

if num1 == num2:
  print('Os números são iguais.')

#2
valor = float(input('Digite um valor qualquer: '))

if valor > 0:
    print('O valor é positivo.')
elif valor < 0:
    print('O valor é negativo.')
else:
    print('O valor é zero.')

#3
sexo = input('Digite uma letra F ou M: ')

if sexo == 'F' or sexo == 'f':
    print('F - Feminino')
elif sexo == 'M' or sexo == 'm':
    print('M - Masculino.')
else:
    print('Sexo Inválido.')

#4
letra = str(input('Digite uma letra qualquer: '))

lista = ('a','e','i','o','u','A','E','I','O','U')

if letra in lista:
  print('A letra digitada é uma vogal.')
else:
  print('A letra digitada é uma consoante.')

#5
notap1 = float(input('Digite a primeira nota: '))
notap2 = float(input('Digite a segunda nota: '))

media_a = (notap1 + notap2) / 2;

if media_a == 10:
  print('Aprovado com Distinção!')
elif media_a >= 7:
  print('Aprovado!')
else:
  print('Reprovado!')

#6
numer1 = float(input('Digite um número: '))
numer2 = float(input('Digite outro número: '))
numer3 = float(input('Digite mais um número: '))

if numer1 > numer2 and numer1 > numer3:
  print('O maior número é:',numer1)
if numer2 > numer1 and numer1 > numer3:
  print('O maior número é:',numer1)
if numer3 > numer2 and numer3 > numer1:
  print('O maior número é:',numer1)
if numer1 == numer2 and numer1 == numer3:
  print('Os 3 números são iguais.')

#7
numer1 = float(input('Digite um número: '))
numer2 = float(input('Digite outro número: '))
numer3 = float(input('Digite mais um número: '))

maior = max(numer1, numer2, numer3)
menor = min(numer1, numer2, numer3)

print('O maior número é:', maior)
print('O menor número é:', menor)

#8
produto1 = float(input('informe o preço do primeiro produto: '))
produto2 = float(input('informe o preço do segundo produto: '))
produto3 = float(input('informe o preço do terceiro produto: '))

menor_val = min(produto1, produto2, produto3)

print(f'Você deve comprar o produto no valor de:{menor_val:.2f}R$')

#9
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
    if numero2 >= numero3:
        medio = numero2
        menor = numero3
    else:
        medio = numero3
        menor = numero2
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
    if numero1 >= numero3:
        medio = numero1
        menor = numero3
    else:
        medio = numero3
        menor = numero1
else:
    maior = numero3
    if numero1 >= numero2:
        medio = numero1
        menor = numero2
    else:
        medio = numero2
        menor = numero1

print('A ordem decrescente é:', maior, medio, menor)

#10
turno = str(input('Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: '))

if turno.upper() == 'M':
    print('Bom Dia!')
elif turno.upper() == 'V':
    print('Boa Tarde!')
elif turno.upper() == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

#11
salario_atual = float(input('Digite o salário atual do funcionário: '))

if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print('Salário antes do reajuste:', salario_atual,'R$')
print('Percentual de aumento aplicado:',percentual_aumento,'%')
print('Valor do aumento:',valor_aumento,'R$')
print('Novo salário após o aumento:',novo_salario,'R$')

#12
valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11

if salario_bruto <= 900.00:
    ir_desconto = 0
elif salario_bruto <= 1500.00:
    ir_desconto = salario_bruto * 0.05
elif salario_bruto <= 2500.00:
    ir_desconto = salario_bruto * 0.1
else:
    ir_desconto = salario_bruto * 0.2

inss_desconto = salario_bruto * 0.1
total_descontos = ir_desconto + inss_desconto
salario_liquido = salario_bruto - total_descontos

print('Salário Bruto:',salario_bruto,'R$')
print('IR:',ir_desconto,'R$')
print('INSS:',inss_desconto,'R$')
print('FGTS:',fgts,'R$')
print('Total de descontos:',total_descontos,'R$')
print('Salário Líquido:',salario_liquido,'R$')

#13
numero_s = int(input('Digite um número de 1 a 7: '))

if numero_s == 1:
  print('Domingo!')
elif numero_s == 2:
  print('Segunda!')
elif numero_s == 3:
  print('Terça!')
elif numero_s == 4:
  print('Quarta!')
elif numero_s == 5:
  print('Quinta!')
elif numero_s == 6:
  print('Sexta!')
elif numero_s == 7:
  print('Sábado!')
else:
  print('Valor inválido!')

#14
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

conceito = ''
aprovado = False

if media >= 9.0:
    conceito = 'A'
    aprovado = True
elif media >= 7.5:
    conceito = 'B'
    aprovado = True
elif media >= 6.0:
    conceito = 'C'
    aprovado = True
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

print('Notas:', nota1, 'e', nota2)
print('Média:', media)
print('Conceito:', conceito)

if aprovado:
    print('Aprovado!')
else:
    print('Reprovado!')

#15
lado_1 = int(input('Valor do preimeiro lado do triangulo: '))
lado_2 = int(input('Valor do segundo lado do triangulo: '))
lado_3 = int(input('Valor do terceiro lado do triangulo: '))

if lado_1 == lado_2 == lado_3:
    print('O triângulo é equilátero!')
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!')

#16
import math

a = float(input('Digite o valor de a: '))

if a == 0:
    print('A equação não é do segundo grau. Encerra o programa.')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    delta = b**2 - 4*a*c

    if delta < 0:
        print('A equação não possui raízes reais. Encerra o programa.')
    elif delta == 0:
        raiz = -b / (2*a)
        print('A equação possui uma raiz real:', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print('A equação possui duas raízes reais:', raiz1, 'e', raiz2)

#17
ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(ano,'é um ano bissexto.')
else:
    print(ano,'não é um ano bissexto.')

#18
from datetime import datetime

data_str = str(input('Digite uma data no formato dd/mm/aaaa: '))

try:
    data = datetime.strptime(data_str, "%d/%m/%Y")
    print("A data", data_str, "é uma data válida.")
except ValueError:
    print("A data", data_str, "não é uma data válida.")

#19
def imprimir_quantidade(num):
    if num < 1 or num >= 1000:
        print('O número deve ser maior que 0 e menor que 1000.')
        return

    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = (num % 100) % 10

    resultado = ''

    if centenas > 0:
        resultado += str(centenas)
        resultado += 'centena' if centenas == 1 else 'centenas'

    if dezenas > 0:
        if resultado != '':
            resultado += ','
        resultado += str(dezenas)
        resultado += 'dezena' if dezenas == 1 else 'dezenas'

    if unidades > 0:
        if resultado != '':
            resultado += 'e'
        resultado += str(unidades)
        resultado += 'unidade' if unidades == 1 else 'unidades'

    print(resultado)


numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for num in numeros:
    imprimir_quantidade(num)

#20
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f'Aprovado com Distinção. Média: {media:.2f}')
elif media >= 7:
    print(f'Aprovado. Média: {media:.2f}')
else:
    print(f'Reprovado. Média: {media:.2f}')

#21
valor_saque = int(input('Digite o valor do saque (entre 10 e 600 reais): '))

if valor_saque < 10 or valor_saque > 600:
    print('Valor de saque inválido.')
else:
    notas_disponiveis = [100, 50, 10, 5, 1]

    print('Notas a serem fornecidas:')
    for nota in notas_disponiveis:
        quantidade_notas = valor_saque // nota
        valor_saque %= nota

        if quantidade_notas > 0:
            print('{} nota(s) de {} R$'.format(quantidade_notas, nota))

#22
nume_ro = float(input('Digite um número qualquer: '))

if nume_ro % 2 == 0:
  print('O número é par!')
else:
  print('O número é ímpar!')

#23
numer_o = float(input('Digite um número qualquer: '))

numero_arredondado = round(numer_o)

if numer_o == numero_arredondado:
    print('O número é inteiro.')
else:
    print('O número é decimal.')

#24
nume_ro1 = float(input('Digite o primeiro número: '))
nume_ro2 = float(input('Digite o segundo número: '))

operacao = str(input('Digite a operação desejada:(+, -, *, /)'))

if operacao == '+':
    resultado = nume_ro1 + nume_ro2
elif operacao == '-':
    resultado = nume_ro1 - nume_ro2
elif operacao == '*':
    resultado = nume_ro1 * nume_ro2
elif operacao == '/':
    resultado = nume_ro1 / nume_ro2
else:
    print('Operação inválida.')

if resultado % 2 == 0:
    par_ou_impar = 'par'
else:
    par_ou_impar = 'ímpar'

if resultado >= 0:
    positivo_ou_negativo = 'positivo'
else:
    positivo_ou_negativo = 'negativo'

if resultado.is_integer():
    inteiro_ou_decimal = 'inteiro'
else:
    inteiro_ou_decimal = 'decimal'

print('Resultado da operação: ', resultado)
print('O número é', par_ou_impar + ", " + positivo_ou_negativo + " e " + inteiro_ou_decimal + ".")

#25
print('Responda as seguintes perguntas Sim ou Não: ')
pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')

respostas_positivas = 0

if pergunta1.lower() == 'sim':
    respostas_positivas += 1

if pergunta2.lower() == 'sim':
    respostas_positivas += 1

if pergunta3.lower() == 'sim':
    respostas_positivas += 1

if pergunta4.lower() == 'sim':
    respostas_positivas += 1

if pergunta5.lower() == 'sim':
    respostas_positivas += 1

if respostas_positivas == 2:
    print('Suspeita!')
elif 3 <= respostas_positivas <= 4:
    print('Cúmplice!')
elif respostas_positivas == 5:
    print('Assassino!')
else:
    print('Inocente!')

#26
preco_gasolina = 2.50
preco_alcool = 1.90

litros = float(input('Digite o número de litros vendidos: '))
tipo_combustivel = str(input('Digite o tipo de combustível A para álcool ou G para gasolina: '))

if tipo_combustivel.upper() == 'A':
    if litros <= 20:
        valor_total = litros * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_total = litros * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel.upper() == 'G':
    if litros <= 20:
        valor_total = litros * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_total = litros * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print('Tipo de combustível inválido.')

print(f'O valor a ser pago pelo cliente é: {valor_total:.2f} R$')

#27
morango_kg = float(input('Digite a quantidade de morangos em Kg: '))
maca_kg = float(input('Digite a quantidade de maçãs em Kg: '))

if morango_kg <= 5:
  preco_morango = 2.50
else:
  preco_morango = 2.20

if maca_kg <= 5:
  preco_maca = 1.80
else:
  preco_maca = 1.50

valor_total = (morango_kg * preco_morango) + (maca_kg * preco_maca)

if (morango_kg + maca_kg) > 8 or valor_total > 25.00:
    desconto = valor_total * 0.10
    valor_total -= desconto

print(f'O valor a ser pago é: {valor_total:.2f} R$')

#28
file_duplo_ate_5kg = 4.90
file_duplo_acima_5kg = 5.80
alcatra_ate_5kg = 5.90
alcatra_acima_5kg = 6.80
picanha_ate_5kg = 6.90
picanha_acima_5kg = 7.80

tipo_carne = str(input('Digite o nome do tipo de carne File Duplo, Alcatra ou Picanha: '))
quantidade_carne = float(input('Digite a quantidade de carne em Kg: '))

if tipo_carne.lower() == 'file duplo':
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * file_duplo_ate_5kg
    else:
        preco_total = quantidade_carne * file_duplo_acima_5kg
elif tipo_carne.lower() == 'alcatra':
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * alcatra_ate_5kg
    else:
        preco_total = quantidade_carne * alcatra_acima_5kg
elif tipo_carne.lower() == 'picanha':
    if quantidade_carne <= 5:
        preco_total = quantidade_carne * picanha_ate_5kg
    else:
        preco_total = quantidade_carne * picanha_acima_5kg
else:
    print('Tipo de carne inválido!')

tipo_pagamento = input('Digite o tipo de pagamento Cartão Tabajara ou outro: ')

if tipo_pagamento.lower() == "cartão tabajara":
    desconto = 0.05 * preco_total
    valor_a_pagar = preco_total - desconto
else:
    desconto = 0
    valor_a_pagar = preco_total


print('    Cupom Fiscal    ')
print('Tipo de carne:', tipo_carne)
print('Quantidade:', quantidade_carne,'kg')
print('Preço total:', preco_total,'R$')
print('Tipo de pagamento:', tipo_pagamento)
print('Valor do desconto:', desconto,'R$')
print('Valor a pagar:', valor_a_pagar,'R$')

#Lista 8 Python Brasil

#1
class Bola:
  def __init__(self, cor, circunf, material):
    self.cor = cor
    self.circunf = circunf
    self.material = material

  def trocaCor(self, nova_cor):
    self.cor = nova_cor

  def mostraCor(self):
    return self.cor

#2
class Quadrado:
  def __init__(self, lado):
    self.lado = lado

  def mudarLado(self, novo_lado):
    self.lado = novo_lado

  def retornarLado(self):
    return self.lado

  def calcularArea(self):
    return self.lado ** 2

#3
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

def calcularPisosERodapes(retangulo, tamanho_piso, altura_rodape):
    area_local = retangulo.calcularArea()
    perimetro_local = retangulo.calcularPerimetro()

    qtd_pisos = area_local / tamanho_piso
    qtd_rodapes = perimetro_local / altura_rodape

    return qtd_pisos, qtd_rodapes

comprimento = float(input('Digite o comprimento do local: '))
largura = float(input('Digite a largura do local: '))

local = Retangulo(comprimento, largura)

tamanho_piso = float(input('Digite o tamanho do piso: '))
altura_rodape = float(input('Digite a altura do rodapé: '))

qtd_pisos, qtd_rodapes = calcularPisosERodapes(local, tamanho_piso, altura_rodape)

print('Quantidade de pisos necessários:', qtd_pisos)
print('Quantidade de rodapés necessários:', qtd_rodapes)

#4
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

#5
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')

#6
class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 5

    def alterarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print('Canal inválido.')

    def aumentarVolume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print('Volume máximo alcançado.')

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Volume mínimo alcançado.')

#7
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        humor = self.fome + self.saude
        return humor

#8
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if len(self.bucho) == 0:
            print('O bucho de', self.nome, 'está vazio.')
        else:
            print('O bucho de', self.nome, 'contém:', self.bucho)

    def digerir(self):
        if len(self.bucho) == 0:
            print('O bucho de', self.nome, 'está vazio. Não há nada para digerir.')
        else:
            print('Digerindo.')
            self.bucho = []

#9
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("({}, {})".format(self.x, self.y))

class Retangulo:
    def __init__(self, largura, altura, ponto_inicio):
        self.largura = largura
        self.altura = altura
        self.ponto_inicio = ponto_inicio

    def centro(self):
        x_centro = self.ponto_inicio.x + self.largura/2
        y_centro = self.ponto_inicio.y + self.altura/2
        return Ponto(x_centro, y_centro)


retangulos = []

while True:
    print("\nMenu:\n")
    print("1 - Criar novo retângulo")
    print("2 - Alterar valores de um retângulo existente")
    print("3 - Imprimir centro de um retângulo existente")
    print("4 - Sair\n")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("\nCriando novo retângulo\n")
        x = int(input("Digite o valor de x do ponto de início: "))
        y = int(input("Digite o valor de y do ponto de início: "))
        ponto_inicio = Ponto(x, y)
        largura = int(input("Digite a largura do retângulo: "))
        altura = int(input("Digite a altura do retângulo: "))
        retangulo = Retangulo(largura, altura, ponto_inicio)
        retangulos.append(retangulo)
        print("Retângulo criado com sucesso!\n")

    elif opcao == 2:
        if len(retangulos) == 0:
            print("\nNão há retângulos cadastrados.\n")
        else:
            print("\nAlterando valores de um retângulo existente\n")
            for i, retangulo in enumerate(retangulos):
                print("Retângulo {}".format(i+1))
                print("- Ponto de início: ", end="")
                retangulo.ponto_inicio.imprimir()
                largura = int(input("- Digite a nova largura do retângulo: "))
                altura = int(input("- Digite a nova altura do retângulo: "))
                retangulo.largura = largura
                retangulo.altura = altura
                print("Valores alterados com sucesso!\n")
                break

    elif opcao == 3:
        if len(retangulos) == 0:
            print("\nNão há retângulos cadastrados.\n")
        else:
            print("\nImprimindo centro de um retângulo existente\n")
            for i, retangulo in enumerate(retangulos):
                print("Retângulo {}".format(i+1))
                print("- Centro: ", end="")
                retangulo.centro().imprimir()
                print("")
                break

    elif opcao == 4:
        print("\nSaindo...")
        break

    else:
        print("\nOpção inválida!\n")

#10
class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self, valorAbastecido):
        qtdLitros = valorAbastecido / self.valorLitro
        print(f'Foram abastecidos {qtdLitros:.2f} litros de {self.tipoCombustivel}.')
        self.quantidadeCombustivel -= qtdLitros
        
    def abastecerPorLitro(self, qtdLitros):
        valorPagar = self.valorLitro * qtdLitros
        print(f'O cliente deve pagar R${valorPagar:.2f} pelo abastecimento.')
        self.quantidadeCombustivel -= qtdLitros
        
    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        
    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        
    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade

#11
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0
        
    def andar(self, distancia):
        combustivel_gasto = distancia / self.consumo
        if combustivel_gasto > self.combustivel:
            print('O carro não tem combustível suficiente para rodar essa distância!')
        else:
            self.combustivel -= combustivel_gasto
            print(f'O carro percorreu {distancia} km e gastou {combustivel_gasto:.2f} litros de combustível.')
        
    def obterGasolina(self):
        return self.combustivel
    
    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade
        print(f'Tanque abastecido com {quantidade} litros de combustível. O carro agora tem {self.combustivel} litros no tanque.')

#12
class ContaInvestimento:
    def __init__(self, saldoInicial, taxaJuros):
        self.saldo = saldoInicial
        self.taxaJuros = taxaJuros
        
    def adicioneJuros(self):
        juros = self.saldo * (self.taxaJuros / 100)
        self.saldo += juros
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')
            
    def consultarSaldo(self):
        return self.saldo

#13
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario

#14
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def aumentarSalario(self, porcentualDeAumento):
        aumento = self.salario * (porcentualDeAumento / 100)
        self.salario += aumento
        print(f'Salário atualizado: R${self.salario:.2f}')

#15
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50
        
    def alimentar(self, quantidade):
        self.fome -= quantidade / 2
        
    def brincar(self, duracao):
        self.tedio -= duracao / 10
        
    def humor(self):
        if self.fome <= 0 or self.tedio <= 0:
            return 'mal-humorado'
        elif self.fome < 20 or self.tedio < 20:
            return 'triste'
        elif self.fome > 80 or self.tedio > 80:
            return 'feliz'
        else:
            return 'satisfeito'

#16
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50
    
    def alimentar(self, quantidade):
        self.fome -= quantidade / 2
        
    def brincar(self, duracao):
        self.tedio -= duracao / 10
        
    def humor(self):
        if self.fome <= 0 or self.tedio <= 0:
            return 'mal-humorado'
        elif self.fome < 20 or self.tedio < 20:
            return 'triste'
        elif self.fome > 80 or self.tedio > 80:
            return 'feliz'
        else:
            return 'satisfeito'

    def __str__(self):
        return f'Bichinho {self.nome} - Fome: {self.fome}, Tédio: {self.tedio}'

#17
import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)
    
    def alimentar(self, quantidade):
        self.fome -= quantidade / 2
        
    def brincar(self, duracao):
        self.tedio -= duracao / 10
        
    def humor(self):
        if self.fome <= 0 or self.tedio <= 0:
            return 'mal-humorado'
        elif self.fome < 20 or self.tedio < 20:
            return 'triste'
        elif self.fome > 80 or self.tedio > 80:
            return 'feliz'
        else:
            return 'satisfeito'

    def __str__(self):
        return f'Bichinho {self.nome} - Fome: {self.fome}, Tédio: {self.tedio}'
        

class FazendaBichinhos:
    def __init__(self, numBichinhos):
        self.bichinhos = []
        for i in range(numBichinhos):
            nome = f'Bichinho{i+1}'
            self.bichinhos.append(BichinhoVirtual(nome))
        
    def alimentarTodos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)
        
    def brincarTodos(self, duracao):
        for bichinho in self.bichinhos:
            bichinho.brincar(duracao)
    
    def ouvirTodos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

numBichinhos = int(input('Quantos bichinhos deseja criar? '))
fazenda = FazendaBichinhos(numBichinhos)

while True:
    
    print('O que deseja fazer?')
    print('1 - Alimentar todos os bichinhos')
    print('2 - Brincar com todos os bichinhos')
    print('3 - Ouvir todos os bichinhos')
    print('4 - Sair')
    opcao = int(input())
    
    if opcao == 1:
        quantidade = int(input('Quantas unidades de comida deseja dar? '))
        fazenda.alimentarTodos(quantidade)
    elif opcao == 2:
        duracao = int(input('Por quanto tempo deseja brincar (em minutos)? '))
        fazenda.brincarTodos(duracao)
    elif opcao == 3:
        fazenda.ouvirTodos()
    else:
        break

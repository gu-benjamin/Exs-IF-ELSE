# -*- coding: utf-8 -*-
"""Aula Funcoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S9uwTVozrJTybXqwqD7psZDpTBL_8QDe

# **Aula 8**

## Atividade 1

Implemente o código abaixo e teste-o com diversos nomes.
"""

def saudacao(nome):
  print(f'Olá {nome}')

nome = input('Entre com seu nome: ')

saudacao(nome)

"""## Atividade 2

Crie a função alterna(n) que imprime a sequência crescente de números naturais com
mudança de sinal alternadamente até n.
"""

def alterna(n):
  fator, mult = -1,-1
  for i in range(n+1):
    print(i*mult, end=' ')
    mult *= fator
  print()

alterna(5)
alterna(9)
alterna(12)

"""## Atividade 3

Implemente uma função que calcula o perímetro de um retângulo de
lados a e b. Note o uso do termo ‘return’ no exemplo anterior para
retornar o perímetro calculado pela função:

perimetro_retangulo(a, b)

Lembre-se de que o perímetro do retângulo é dado por 2 × a + 2 × b:
print(perimetro_retangulo(2,3)) # Saída esperada: 10
"""

def perimetro_retangulo(base,altura):
  return (base*2)+(altura*2)

print(perimetro_retangulo(2,3))

"""## Atividade 4

Os parâmetros posicionais são passados na ordem em que foram definidos na função
(nome e mensagem). Os parâmetros nomeados são especificados explicitamente com
seus nomes ao chamar a função (mensagem="Tudo bem?" e nome="Maria").
"""

def saudacao(nome, mensagem='Bom dia!'):
  print(f'Olá {nome}! {mensagem}')

saudacao('Gustavo', 'Como você está?')

saudacao(mensagem='Suave?', nome='Jão')

"""## Atividade 5

Implemente a função que recebe uma lista de números e retorna a
soma dos números positivos e a soma dos números negativos.
"""

def soma_pn(valores):
  soma_p,soma_n = 0,0
  for n in valores:
    if n >= 0:
      soma_p += n
    else:
      soma_n += n

  return soma_p, soma_n

valores = [2,-1,-4, 3]

soma_p,soma_n = soma_pn(valores)

print(f'soma dos positivos: {soma_p}\nsoma dos negativos: {soma_n}')

"""# Atividade 6

Implemente a função somas(lista) que recebe uma lista de números e
retorna a soma dos números e a soma dos números ao quadrado.
"""

def somas(lista):
  soma = sum(lista)
  soma2 = sum([n**2 for n in lista])

  return soma, soma2

valores = [2,-1,-4, 3]
soma, soma2 = somas(valores)

print(f'soma: {soma}\nsoma2: {soma2}')

"""# Atividade 7


"""

def soma(a,b):
  return a+b

def subtracao(a,b):
  return a-b

def multiplicacao(a,b):
  return a*b

def divisao(a,b):
  return a/b if b != 0 else 'Calculo indefinido'

def potenciacao(a,b):
  return a**b

def radiciacao(a,b):
  return a**(1/b)

def fatorial(a):
  fatorial = 1 if a > 0 else 0
  while a > 0:
    fatorial *= a
    a -= 1

  return fatorial

def exibir_menu():
  print('Escolha uma operação:')
  print('1. Soma')
  print('2. Subtração')
  print('3. Multiplicação')
  print('2. Divisão')
  print('5. Potenciação')
  print('6. Radiciacao')
  print('7. Fatorial')
  print()

def calculadora():
  exibir_menu()
  while True:
    opcao = input('Digite o número da operação desejada: ')
    if opcao in ('1','2','3','4','5','6','7'):
      if opcao == '7':
        n1 = float(input('Digite o número para o fatorial: '))
        resultado = fatorial(n1)
        print(f'Resultado: {resultado}')
        continue
      n1 = float(input('Digite o primeiro número: '))
      n2 = float(input('Digite o segundo número: '))
      if opcao == '1': resultado = soma(n1,n2)
      if opcao == '2': resultado = subtracao(n1,n2)
      if opcao == '3': resultado = multiplicacao(n1,n2)
      if opcao == '4': resultado = divisao(n1,n2)
      if opcao == '5': resultado = potenciacao(n1,n2)
      if opcao == '6': resultado = radiciacao(n1,n2)

      print(f'Resultado: {resultado: .2f}')
    else:
      print('Opção inválida! Programa encerrado.')
      break

calculadora()

def caracteres_iguais(texto: str) -> bool:
  caracter1 = texto[0]

  for caractere in texto:
    if caractere != caracter1:
      return False

  return True

def validar_cpf(cpf: str) -> bool:
  # Verificar se o cpf possui 11 caracteres, todos os digitos são números e que todos os digitos não sejam iguais, caso contrário retorna False
  if len(cpf) != 11 or not cpf.isnumeric(): return False
  if caracteres_iguais(cpf): return False

  # Somadores e multiplicadores para cada digito verificador
  soma_dg = 0
  mult = 10

  # Calculo digito 1
  for digito in cpf[0:9]:
    soma_dg += int(digito)*mult
    mult -= 1

  dg1 = ((soma_dg*10)%11)%10

  # Calculo digito 2
  soma_dg = 0
  mult = 11
  for digito in cpf[0:10]:
    soma_dg += int(digito)*mult
    mult -= 1

  dg2 = ((soma_dg*10)%11)%10

  verificadores = f'{dg1}{dg2}'

  # Verificar se ambos digitos calculos são iguais aos digitos do cpf informado
  return verificadores == cpf[9:]

cpf = input('Informe um CPF: ').strip()

if validar_cpf(cpf):
  print('O CPF é válido!')
else:
  print('O CPF é inválido!')

def caracteres_iguais(texto: str) -> bool:
  caracter1 = texto[0]

  for caractere in texto:
    if caractere != caracter1:
      return False

  return True

def completar_cpf(cpf: str) -> str:
  # Verificar se o cpf possui 9 caracteres, todos os digitos são números e que todos os digitos não sejam iguais, caso contrário retorna False
  if len(cpf) != 9 or not cpf.isnumeric(): return 'Indefinido'
  if caracteres_iguais(cpf): return 'Indefinido'

  cpfn = cpf
  # Somadores e multiplicadores para cada digito verificador
  soma_dg = 0
  mult = 10

  # Calculo digito 1
  for digito in cpfn:
    soma_dg += int(digito)*mult
    mult -= 1

  dg1 = str(((soma_dg*10)%11)%10)
  # Adicionando dg1 á string que compoe o CPF
  cpfn += dg1

  # Calculo digito 2
  soma_dg = 0
  mult = 11
  for digito in cpfn:
    soma_dg += int(digito)*mult
    mult -= 1

  dg2 = str(((soma_dg*10)%11)%10)
  # Adicionando dg2 á string que compoe o CPF
  cpfn += dg2
  return cpfn

cpf_inc = input('Informe 9 de um CPF: ').strip()

print(f'CPF completo: {completar_cpf(cpf_inc)}')
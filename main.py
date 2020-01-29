nome = input ('Coloque seu nome: ')
idade = int(input ('informe sua idade: '))
salario = float (input ('informe seu salário: '))
sexo = input ('informe seu sexo f-feminino ou m-masculino: ')

civil = input ("""informe seu estado civil
               s-solteiro
               c-casado
               v-viúvo
               d-divorciado: """)

estados = ['s', 'c', 'v', 'd']
a = 0
for letra in nome:
  a += 1
  if a > 3:
    print('O nome é valido')
    break

else:
  print('O nome é invalido')

if salario > 0:
  print('O salário é valido')

else:
  print('O salário é inválido')

if idade > 0 and idade <= 150:
  print('A idade é valida')

else:
  print ('A idade é inválida')

if sexo.lower() == 'f' or sexo.lower() == 'm':
  print ('O sexo é valido')

else:
  print ('O sexo é invalido')

for x in estados:
  if civil.lower() == x:
    print ('Estado civil valido')
    break

else:
  print ('Estado civil invalido')



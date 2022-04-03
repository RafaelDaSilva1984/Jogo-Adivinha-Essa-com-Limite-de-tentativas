fim = 5
cont = 0


while cont < fim:
  print('Interação número:',cont)
  cont += 1


vl=int(input('Digite um valor: '))
inicio = 1
contdiv = 0
while inicio <= vl: #começa a testar com o número 1
  if (vl % inicio) == 0: # testa para saber se o resto é zero
    contdiv += 1 # conta qtas div deu com resto zero na formula (vl % inicio)==0
  inicio += 1 # qdo maior ou igual que o inicio para o while
if contdiv == 2: # se o cont for maior q 2 False e se ígual a 2 divisão True
  print('Primo')
else:
  print('Não é Primo')
print(inicio)


print('Qual número estou pensando entre 0 a 10!!!!')
comp = 8
max = 3
tentativas = 1
while tentativas <= max:
  jogador = int(input('Tente adivinhar: ')) # o input tem que ser depois do while para não ficar se repetindo   
  if jogador == comp:
    print('Parabéns você adivinhou... eu escondi o número:',comp)
    break # para o programa após acertar o número do computador
  elif jogador > comp:
    print('Número escondido é Menor...')
  elif jogador < comp:
    print('Número escondido é Maior...')
  if tentativas == max:
    print('Você perdeu meu número escondido é: ',comp)
  tentativas += 1 # somas o número de tentativas até o max indicado
  
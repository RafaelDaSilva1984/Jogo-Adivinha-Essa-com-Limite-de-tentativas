print('Jogo do Adivinha de 0 até 10 com 3 Tentativas Máximas')
print('Qual número estou pensando entre 0 a 10!!!!')
comp = 8
max = 3
tentativas = 1
cont = 1
while tentativas <= max:
    
  jogador = int(input('Tente adivinhar: ')) # o input tem que ser depois do while para não ficar se repetindo   
  if jogador == comp:
    print('Parabéns você adivinhou... eu escondi o número:',comp)
    print(f'Acertou na tentativa {cont }')
    break # para o programa após acertar o número do computador
  elif jogador > comp:
    print('Número escondido é Menor...')
    cont += 1
    print(f'Testativa restante {3 - cont }')
  elif jogador < comp:
    print('Número escondido é Maior...')    
    print(f'Testativa restante {3 - cont}')
  if tentativas == max:
    print('Você perdeu meu número escondido é: ',comp)
    
  tentativas += 1 # somas o número de tentativas até o max indicado
  cont += 1
    
  

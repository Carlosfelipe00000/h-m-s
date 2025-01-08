import time
while True:
    try:
        h = int(input('Digite quantas horas você quer:'))
        print()
        print('continuando')
        print()
        break
    except ValueError: 
        print('Digite um número!')
while True:
    try:
        m = int(input('Digite quantos minutos você quer:'))
        if m > 59:
            print('Digite um número entre 1 e 59!')
        else:
            print()
            print('continuando')
            print()
            break
    except ValueError: 
        print('Digite um número!')
while True:
    try:
        s = int(input('Digite quantos segundos você quer:'))
        if s > 59:
            print('Digite um número entre 1 e 59!')
        else:
            print()
            c = input('digite qualquer tecla para continuar...')
            print()
            break
    except ValueError: 
        print('Digite um número!')
        
print(f'Você digitou: [{h:02}h:{m:02}m:{s:02}s]')
print()   
input('digite uma tecla para continuar...')
print()
print('transformando em segundos...')
time.sleep(3)

ss = h*3600 + m*60 + s

print(f'São ao todo {ss} segundos')

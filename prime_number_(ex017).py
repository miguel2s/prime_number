#exercício 52 numeros primos
n = int(input('Digite um número inteiro: '))
l = []
for c in range(1, n+1):
    if n % c == 0:
        l.append(c)
print('O número {} é divisível por {}.'.format(n, l))
if l == [1, n]:
    print('Portanto o número {} é PRIMO'.format(n))
else:
    print('Portanto o número {} NÃO É PRIMO!'.format(n))


#exercício 52 números primos feito pelo Guanabara
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m', end='')
        t += 1
    else:
       print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, t))
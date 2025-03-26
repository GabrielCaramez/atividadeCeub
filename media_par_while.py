ct = 0
soma = 0
print('Digite -1 para sair do programa: ')
while True:
    n = int(input('Digite sua nota: '))
    if n == 0:
        break
    elif n % 2 == 0:
        soma = soma + n
        ct = ct + 1
print(f'A soma dos números pares é: {soma}')
print(f'A média dos números pares é: {soma/ct:.2f}')
print('Fim do programa')

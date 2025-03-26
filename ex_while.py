ct = 0
print('Digite[-1 para sair]')
while True:
    n = int(input('Digite um número: '))
    if n == -1:
        break
    ct = ct + 1
print(f'Quantidade de números digitados: {ct}')
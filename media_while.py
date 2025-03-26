soma = 0
ctl = 0
print('Digite[-1 para sair]')
dis = input('Digite qual a sua disiplina: ')
while True:
    n = float(input('Digite uma nota: '))
    if n == -1:
        break
    soma = soma + n
    ctl = ctl + 1
print(f'esta e a sua disiplina: {dis}')
print(f'esta e a soma das notas dos alunos {soma:.2f}')
print(f'Média das notas: {soma/ctl:.2f}')
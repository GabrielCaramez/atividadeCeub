valor = 1
menor_valor = float('inf')
contador = 0
soma = 0
maior_valor = float('-inf')
print("Digite 0 para sair ")
while valor != 0:
    valor = float(input("Valor= "))
    if valor < menor_valor and valor != 0:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    contador = contador + 1
    soma = soma + valor
print(f"menor valor = {menor_valor} a quantidade de numeros digitadas foi {contador} e a soma de todos os valores foi {soma} o maior valor e = {maior_valor} ")

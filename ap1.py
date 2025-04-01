valores = []

while True:
    try:
        entrada = input("Digite um valor real (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        valor = float(entrada)
        valores.append(valor)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número real ou 'sair'.")

quantidade = len(valores)
soma = sum(valores)
media = soma / quantidade if quantidade > 0 else 0
maiores_que_20 = len([v for v in valores if v > 20])

print(f"Quantidade de valores digitados: {quantidade}")
print(f"Soma dos valores digitados: {soma}")
print(f"Média aritmética dos valores digitados: {media}")
print(f"Quantidade de valores maiores que 20: {maiores_que_20}")

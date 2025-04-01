def calcular_medias():
    soma_pares = 0
    soma_impares = 0
    cont_pares = 0
    cont_impares = 0

    while True:
        try:
            numero = int(input("Digite um número (0 para sair): "))
            if numero == 0:
                break
            if numero % 2 == 0:
                soma_pares += numero
                cont_pares += 1
            else:
                soma_impares += numero
                cont_impares += 1
        except ValueError:
            print("Por favor, insira um número válido.")

    media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
    media_impares = soma_impares / cont_impares if cont_impares > 0 else 0

    print(f"Média dos números pares: {media_pares:.2f}")
    print(f"Média dos números ímpares: {media_impares:.2f}")

if __name__ == "__main__":
    calcular_medias()
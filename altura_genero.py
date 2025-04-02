m = 0
f = 0
genero = ("")
maior = float('inf')
menor = float('-inf')
print("para parar o progrma aperte o b ")
while genero != b:
    genero = str(input("coloque o genero f(feminino) m(mascolino)")).lower()
    if genero == "m":
        m = m + 1
    elif genero == "f":
        f = f + 1
    else:
        print("letra não bate com o Banco de Dados ")
    altura = float(input("Digite sua altura em metros "))
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
print(f"A contidade de homens foi {m} e a de mulheres foi {f} a maior altura foi {maior} e sua menor altura foi {menor} ")



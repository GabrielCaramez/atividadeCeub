not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))

media = (not1 + not2) / 2

print(f"A média do aluno é: {media:.1f}")
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
 
def resolver_equacao_primeiro_grau(a, b):
    if a == 0:
        if b == 0:
            return "Infinitas soluções"
        else:
            return "Sem solução"
    else:
        x = -b / a
        return x

a = float(input("Digite o coeficiente 'a' :"))
b = float(input("Digite o coeficiente 'b' :"))

solucao = resolver_equacao_primeiro_grau(a, b)
print(f"A solução da equação {a:.1f} x + {b:.1f} = 0 é x = {solucao}")
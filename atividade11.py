vl_compra = float(input("Preço de compra: "))
vl_vendas = float(input("Preço de venda: "))
vl_lucro = vl_vendas - vl_compra
vl_prejuizo = vl_compra - vl_vendas
vl_igual = vl_compra == vl_vendas

if vl_compra < vl_vendas:
    print(f"Lucro {vl_lucro}")
elif vl_compra > vl_vendas:
    print(f"Prejuízo {vl_prejuizo}")
else:
    print(f"Os valores são iguais {vl_igual}")
ano = int(input('digite seu ano de nascimento'))
voto = 2025 - ano

if voto < 16 :
    print('infelizmente vc não pode votar ainda')
elif voto == 16:
    print('parabens vc pode votar seu otario')
elif voto >= 18 :
    print('parabens vc pode tirar sua CNH e tbm pode votar bem vindo a vida adulta')
else:
    print('azar ainda nao pode votar e nem dirigir criança')
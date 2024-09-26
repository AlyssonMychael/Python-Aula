idade=int(input("Idade: "))

if idade<12:
    classificacao="Criança"
elif idade<=17:
    classificacao="Adolescente"
elif idade<=59:
    classificacao="Adulto"
else:
    classificacao="Idoso"

print(f"De acordo com sua idade de {idade} anos, você é {classificacao}")

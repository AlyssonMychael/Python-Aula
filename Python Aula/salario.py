nome=input("Digite seu nome: ")
salario=float(input("Digite o salário do funcionário: "))
tempo=int(input("Digite o tempo que está na empresa: "))

if tempo<=5:
    novo_sal = salario + (salario * 0.06)
elif tempo<=10:
    novo_sal = salario + (salario * 0.10)
elif tempo<=15:
    novo_sal = salario + (salario * 0.15)
else:
    novo_sal = salario + (salario * 0.20)

print(f"O funcionário {nome} possui um novo salário de {novo_sal} reais.")

nome=input("Digite seu nome:\n")
teste=float(input("Digite sua nota do teste:\n"))
prova=float(input("Digite sua nota da prova:\n"))
media=(teste + prova) / 2

if media<4:
    clas="E"
elif media<=6:
    clas="D"
elif media<=7.5:
    clas="C"
elif media<9:
    clas="B"
else:
    clas="A"

print(f"O aluno {nome}, possui uma media de {media:.2f} ficando com o conceito de {clas}")

           

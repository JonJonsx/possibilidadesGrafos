import possibilities_relationship as pr
import possibilities_whitout_relationships as pwr

# |||
fim = True
while fim:
    print("-----------------------------------------")
    print("|1. Criar grafo sem repetição de valor  |")
    print("|2. Criar grafo repetição de valor      |")
    print("-----------------------------------------")
    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        vertices = input("Digite os vertices: ")
        velores = int(input("Digite a quantidade de valore: "))
        pwr.possibilities_whitout_relationships(vertices, velores)
    elif opcao == 2:
        vertices = input("Digite os vertices: ")
        velores = int(input("Digite a quantidade de valore: "))
        pr.possibilities_relationship(vertices, velores)
    else:
        fim = False

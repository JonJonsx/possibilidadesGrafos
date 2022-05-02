import possibilities_no_values as pnv
import possibilities_relationship as pr
import possibilities_whitout_relationships as pwr

# |||
fim = True
while fim:
    print("---------------------------------------------------------------")
    print("|1. Criar gera possibilidades com arestas e repetição         |")
    print("|2. Criar gerar possibilidades com arestas e sem repetição:   |")
    print("|3. Gerar possibilidadades sem arestas                        |")
    print("|4. sair                                                      |")
    print("---------------------------------------------------------------")
    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        vertices = input("Digite os vertices: ")
        velores = int(input("Digite a quantidade de valores: "))
        pwr.possibilities_whitout_relationships(vertices, velores)
    elif opcao == 2:
        vertices = input("Digite os vertices: ")
        velores = int(input("Digite a quantidade de valores: "))
        pr.possibilities_relationship(vertices, velores)
    elif opcao == 3:
        vertices = input("Digite os vertices: ")
        velores = int(input("Digite a quantidade de valores: "))
        pnv.possibilities_no_values(vertices, velores)
    else:
        fim = False

# 5 - Uma escola precisa de ajuda para organizar as notas dos alunos. Crie um programa que leia o nome de um aluno e suas 4 notas. O programa deve continuar lendo os nomes e notas até que o usuário não deseje mais adicionar alunos. Em seguida, o programa deve exibir o nome e a média de cada um dos alunos.
# Extra:
# - Permita que o usuário possa escolher quantas notas cada aluno terá.
# - Mostre uma média geral da turma.

listaAlunos = []
listaNotas = []

continuar = "s"

while continuar == "s":
    qtde_notas_aluno = 0
    nome_aluno = input("Digite o nome do aluno: ")
    listaAlunos.append(nome_aluno)

    qtde_nota_aluno = int(input("Quantas notas esse aluno terá? "))   

    while qtde_notas_aluno < qtde_nota_aluno:
        nota = float(input("Digite a nota: "))
        listaNotas.append(nota)
        qtde_notas_aluno += 1
        
    continuar = input("Deseja continuar? (s/n): \n")

    # for i in range(len(listaAlunos)):
    #     media = listaNotas[i] / len(listaNotas) 
    #     print(f"O aluno {listaAlunos[i]} obteve a média: {media}:.2f")
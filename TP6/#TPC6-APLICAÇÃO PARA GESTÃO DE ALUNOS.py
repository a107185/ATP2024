#TPC6-APLICAÇÃO PARA GESTÃO DE ALUNOS


escola = []
def menu():
    print("""MENU:
          1 Criar uma turma
          2 Inserir um aluno na turma
          3 Listar a turma
          4 Consultar um aluno por ID
          5 Guardar a turma em ficheiro
          6 Carregar uma turma dum ficheiro
          0 Sair da aplicação""")
    op = int(input("Introduza o número da operação que pretende realizar: "))
    if op == 1:
        criarTurma()
    elif op == 2:
        inserirAluno()
    elif op == 3:
        listarTurma()
    elif op == 4:
        consultarAluno()
    elif op == 5:
        guardarTurma(escola)
    elif op == 6:
        carregarTurma(escola)
    elif op == 0:
        print("Saiu da aplicação!")
    else :
        print("Número inválido, selecione outro.")
        menu()
    return

def criarTurma():
    letra = str(input("Introduza a letra da turma: "))
    turma_existe = False
    for turma in escola:
        if turma[0] == letra:
            turma_existe = True
    if turma_existe == False:
        turma = []
        turma.append(letra)
        escola.append(turma)
        print("Turma criada!")
        print(escola)
        menu()
    else:
        print("Essa turma já existe!")
        menu()
    return

def inserirAluno():
    letra = str(input("Introduza a letra da turma a que pretende inserir o aluno: "))
    turma_existe = False
    i = -1
    for turma in escola:
        i = i + 1
        if turma[0] == letra:
            turma_existe = True
            pos = i
    if turma_existe == False:
        print("Essa turma ainda não existe!")
        menu()
    else:
        n = int(input("Quantos alunos pretende inserir nesta turma? "))
        i = 0
        while n > i:
            i = i + 1
            id = input("Introduza o ID do aluno: ")
            id_existe = False
            for turma in escola:
                turmaTeste = turma[1:]
                for aluno in turmaTeste:
                    if id == aluno[1]:
                        id_existe = True
            if id_existe == True:
                print("Este ID já existe!")
                i = i - 1
            else:
                turma = escola[pos]
                notas = []
                nome = str(input("Introduza o nome do aluno: "))
                notaTPC = float(input("Introduza a nota do TPC do aluno: "))
                notaProj = float(input("Introduza a nota do projeto do aluno: "))
                notaTeste = float(input("Introduza a nota do teste do aluno: "))
                notas = [notaTPC, notaProj, notaTeste]
                aluno = (nome, id, notas)
                turma.append(aluno)
                print("Aluno inserido na turma!")
        print(f"A turma criada é {turma}.")
        print(f"A escola com que está a trabalhar é {escola}.")
        menu()
    return
    
def listarTurma():
    letra = str(input("Introduza a letra da turma que pretende listar: "))
    turma_existe = False
    i = -1
    for turma in escola:
        i = i + 1
        if turma[0] == letra:
            turma_existe = True
            pos = i
    if turma_existe == False:
        print("Essa turma ainda não existe!")
        menu()
    else:
        turma = escola[pos]
        print(f"TURMA {turma[0]}: (ALUNO, ID, NOTA TPC, NOTA PROJETO, NOTA TESTE)")
        i = 1
        while len(turma) > i:
            print(f"{turma[i][0]}     {turma[i][1]}     {turma[i][2][0]}  {turma[i][2][1]}  {turma[i][2][2]}")
            i = i + 1
        menu()
    return

def consultarAluno():
    id = input("Introduza o ID do aluno: ")
    id_existe = False
    for turma in escola:
        turmaTeste = turma[1:]
        for aluno in turmaTeste:
            if id == aluno[1]:
                id_existe = True
                alunoID = aluno
    if id_existe == True:
        print(f"Este ID existe e o aluno correspondente apresenta estas informações: {alunoID}")
    else:
        print("Não existe nenhum aluno com este ID!")
    menu()
    
def guardarTurma(escola):
    letra = str(input("Introduza a letra da turma que pretende guardar: "))
    turma_existe = False
    i = -1
    for turma in escola:
        i = i + 1
        if turma[0] == letra:
            turma_existe = True
            pos = i
    if turma_existe == False:
        print("Essa turma ainda não existe!")
        menu()
    else:
        turma = escola[pos]
        f = open(f"turma{turma[0]}.txt", 'w')
        linha = f"TURMA {turma[0]} \n"
        f.write(linha)
        turma = turma[1:]
        for aluno in turma:
            linha = f"{aluno[0]}::{aluno[1]}::{aluno[2][0]}::{aluno[2][1]}::{aluno[2][2]} \n"
            f.write(linha)
        print("Turma Guardada!")
        f.close()
        menu()
    return

def carregarTurma(escola):
    letra = str(input("Introduza a letra da turma que pretende carregar: "))
    turma = [letra]
    f = open(f"turma{letra}.txt", 'r')
    f.readline()
    for linha in f:
        campos = linha.split("::")
        notas = [float(campos[2]), float(campos[3]), float(campos[4])]
        aluno = (str(campos[0]), campos[1], notas)
        turma.append(aluno)
    f.close()
    turma_existe = False
    id_existe = False
    for x in escola:
        if x[0] == letra:
            turma_existe = True
        for al in x[1:]:
            for aluno in turma[1:]:
                if al[1] == aluno[1]:
                    id_existe = True
    if turma_existe == False and id_existe == False:
        escola.append(turma)
        print("Nenhum destes alunos existe noutra turma desta escola, pelo que a turma foi adicionada à escola.")
    print(f"A turma carregada foi {turma}.")
    print(f"A escola com que está a trabalhar é {escola}.")
    menu()
    return

menu()

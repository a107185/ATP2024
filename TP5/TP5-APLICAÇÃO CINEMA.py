#TP5-APLICAÇÃO CINEMA

cinema = [] #sala
sala = [] #nlugares, vendidos, filme, n
nlugares = [int]
filme = [str]
vendidos = [int]
lugar = [int]
n = [int]

#MENU
def menu() :
    print("MENU:\n--------------------------\n(1) Listar Salas\n(2) Disponibilidade Lugar\n(3) Criar Lugar\n(4) Disponibilidade Salas\n(5) Criar Sala\n(6) Remover Sala\n(0) Sair\n-------------------------\n")
    op = int(input("Introduza o número da opção que pretende: "))
    if op == 1 :
        listar()
    elif op == 2:
        disponivel()
    elif op == 3:
        vendebilhete()
    elif op == 4:
        listardisponibilidades()
    elif op == 5:
        inserirSala()
    elif op == 6:
        removerSala()
    elif op == 0:
        print("Terminou o programa!")
    else :
        print("Essa opção é inválida.")
        menu()

def listar() :
    print("SALA                              FILME")
    print("---------------------------------------")
    for sala in cinema:
        print(f" {sala[3]}                                {sala[2]}")
    menu()
    
def vendebilhete() :
    if cinema == []:
        print("Ainda não existem salas!")
    else :
        filme = input("Introduza o nome do filme: ")
        filme_existe = False
        for sala in cinema:
            if filme == sala[2]:
                vendidos = sala[1]
                nlugares = sala[0]
                lugar = 0
                if nlugares == len(vendidos) :
                    print("Sala cheia!")
                    filme_existe = True
                else :
                    while lugar == 0 :
                        lugar = int(input(f"Introduza o número do lugar, entre 1 e {nlugares}, exceto {vendidos}: "))
                        if lugar < 1 or lugar > nlugares :
                            print("Esse lugar não existe nesta sala.")
                            lugar = 0
                        elif lugar in vendidos:
                            print("Esse lugar está ocupado!")
                            lugar = 0
                        else :
                            vendidos.append(lugar)
                            sala[1] = vendidos
                            filme_existe = True
                            print("Lugar vendido!")
                            print(f"Salas: {cinema}")

        if filme_existe == False:
            print("Esse filme não existe!")  
    menu()

def inserirSala() :
    n = int(input("Introduza o número da sala: "))
    sala_existe = False
    for sala in cinema :
        if n == sala[3]:
            print("Essa sala já está ocupada.")
            sala_existe = True
    if sala_existe == False:
        filme = str(input("Introduza o nome do filme: "))
        filme_existe = False
        for sala in cinema :
            if filme == sala[2]:
                print("Esse filme já está a ser exibido noutra sala!")
                filme_existe = True
        if filme_existe == False :
            sala = []
            vendidos = []
            nlugares = int(input("Introduza o número de lugares: "))
            sala.append(nlugares)
            sala.append(vendidos)
            sala.append(filme)
            sala.append(n)
            cinema.append(sala)
            print(f"Salas: {cinema}")
    menu()

def removerSala() :
    n = int(input("Introduza o número da sala que pretende remover: "))
    sala_existe = False
    i = -1
    if cinema == [] :
        print("Não existem salas para remover!")
    else:
        for sala in cinema:
            i = i + 1
            if n in sala:
                del cinema[i]
                sala_existe = True
                print(f"Salas: {cinema}")
        if sala_existe == False:
            print("Essa sala não existe!")
    menu()

def disponivel() :
    filme = input("Introduza o nome do filme: ")
    filme_existe = False
    for sala in cinema:
        vendidos = sala[1]
        nlugares = sala[0]
        if filme in sala:
            filme_existe = True
            lugar = int(input(f"Introduza o número do lugar, entre 1 e {nlugares}: "))
            if lugar < 1 or lugar > nlugares :
                print("Esse lugar não existe nesta sala.")
            elif lugar in vendidos:
                print("Esse lugar está ocupado!")
            else :
                print("Lugar disponível!")
    if filme_existe == False :
        print("Esse filme não existe no cinema!")
    menu()
            
def listardisponibilidades():
    print("SALA         LUGARES DISPONÍEVIS                 FILME")
    print("----------------------------------------------------------------")
    for sala in cinema:
        lugdisp = sala[0] - len(sala[1])
        print(f" {sala[3]}                   {lugdisp}                            {sala[2]}")
    menu()

menu()
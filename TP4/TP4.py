#TP4-Aplicação para monitoração de listas de inteiros

op = (-1)
lista = []
import random 

while op != 0 :
    print("""MENU:        
(1) Criar lista
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")
        
    op = int(input("Introduza o número correspondente à operação que pretende efetuar: "))

    if op == 1 :
        tamanho = int(input("Quantos elementos pretende que a sua lista tenha: "))
        lista = [random.randrange(1,101) for x in range(tamanho)]
        print(lista)

    elif op == 2 :
        tamanho = int(input("Quantos elementos pretende que a sua lista tenha: "))
        i = 0
        lista = []
        while tamanho > 0 :
            i = i + 1
            num = int(input(f"Introduza o {i}º número da sua lista: "))
            lista.append(num)
            tamanho = tamanho - 1
        print(lista)

    elif op == 3 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho :
                num = lista[i]
                i = i + 1
                soma = soma + num
            print(f"A soma é {soma}.")

    elif op == 4 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho :
                num = lista[i]
                i = i + 1
                soma = soma + num
            media = soma / tamanho
            print(f"A média é {média}.")
    
    elif op == 5 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista)
            i = 0
            maior = 0
            while i < tamanho :
                num = lista[i]
                i = i + 1
                if num > maior :
                    maior = num
            print(f"O maior número é {maior}.")

    elif op == 6 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista)
            i = 0
            menor = 0
            while i < tamanho :
                num = lista[i]
                i = i + 1
                if num < menor :
                    menor = num
            print(f"O menor número é {menor}.")

    elif op == 7 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho :
                if lista[i] < lista[i + 1] :
                    i = i + 1
                    if i == tamanho :
                        print("Sim!")
                else :
                    print("Não!")
                    i = tamanho
    
    elif op == 8 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho :
                if lista[i] > lista[i + 1] :
                    i = i + 1
                    if i == tamanho :
                        print("Sim!")
                else :
                    print("Não!")
                    i = tamanho
    
    elif op == 9 :
        if lista == [] :
            print("É necessária a criação de uma lista, para a execução desta função. No menu, selecione 1 ou 2.")
        else :
            print(lista)
            tamanho = len(lista)
            i = 0
            elem = int(input("Introduza o elemento que pretende procurar na lista: "))
            if elem in lista :
                while i < tamanho :
                    if lista[i] == elem :
                        print(f"A sua posição é {i + 1}.")
                        i = tamanho
                    else :
                        i = i + 1
            else :
                print("A sua posição é -1.")

print("Terminou o programa!")




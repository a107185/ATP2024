#TPC7-APLICAÇÃO METEOROLOGIA
tabMeteo = []
fnome = 'metereologia.txt'

def dados():
    dias = int(input("Introduza o número de dias que pretende adicionar à tabela meteorológica: "))
    i = 1
    while i <= dias:
        dia = int(input(f"Introduza o dia ({i}/{dias}): "))
        mês = int(input(f"Introduza o mês ({i}/{dias}): "))
        ano = int(input(f"Introduza o ano ({i}/{dias}): "))
        data = (ano,mês,dia)
        dia_existe = False
        for dados in tabMeteo:
            if dados[0] == data:
                dia_existe = True
        if dia_existe == False:
            tmin = float(input(f"Introduza a temperatura mínina correspondente a esse dia ({i}/{dias}): "))
            tmax = float(input(f"Introduza a temperatura máxima correspondente a esse dia ({i}/{dias}): "))
            prec = float(input(f"Introduza a precipitação correspondente a esse dia ({i}/{dias}): "))
            dados = (data,tmin,tmax,prec)
            tabMeteo.append(dados)
            i = i + 1
        else:
            print("Este dia já se encontra registado na tabela.")
    print(tabMeteo)
    return menu()

def medias(tabMeteo): #DADOS TÊM QUE SER FEITOS PRIMEITO, PÔR ISSO NO MENU
    res = []
    for x in tabMeteo:
        media = (x[2] + x[1])/2
        res.append((x[0], media))
    print(res)
    return menu()

def guardaTabMeteo(tabMeteo, fnome):
    f = open(fnome, 'w')
    for data, tmax, tmin, precip in tabMeteo:
        linha = f'{data[0]}::{data[1]}::{data[2]}::{tmax}::{tmin}::{precip}\n'
        f.write(linha)
    f.close()
    print("Tabela guardada no ficheiro 'metereologia.txt'.")
    return menu()

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome, 'r')
    for linha in f:
        campos = linha.split("::")
        data = (int(campos[0]), int(campos[1]), int(campos[2]))
        res.append((data, float(campos[3]), float(campos[4]), float(campos[5])))
    f.close()
    print(res)
    if tabMeteo == []:
        n = int(input("Pretende trabalhar com esta tabela (1-Sim, 2-Não)? "))
    else:
        n = int(input("Já existe uma outra tabela criada, pretende substituí-la (1-Sim, 2-Não)? "))
    if n == 1:
        tabMeteo = res
    elif n == 2:
        print("A tabela não será adicionada à área de trabalho.")
    else:
        print("Essa operação é inexistente.")
    return menu()

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for _, tmin, _, _ in tabMeteo:
        if tmin < minima :
            minima = tmin
    print(minima)
    return menu()

def amplTerm(tabMeteo):
    res = []
    for x in tabMeteo:
        amp = (x[2] - x[1])
        res.append((x[0], amp))
    print(res)
    return menu()

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    for data, _, _, precip in tabMeteo:
        if precip > max_prec :
            max_prec = precip
            max_data = data
    print((max_data, max_prec))
    return menu()

def diasChuvosos(tabMeteo):
    p = float(input("Introduza o limite máximo de precipitação: "))
    res = []
    for data, _, _, precip in tabMeteo :
        if precip > p :
            res.append((data, precip))
    print(res)
    return menu()

def maxPeriodoCalor(tabMeteo):
    res = 0
    consecutivo = 0
    p = float(input("Introduza o limite máximo de precipitação: "))
    for _, _, _, precip in tabMeteo :
        if precip < p:
            res = res + 1
        else :
            if res > consecutivo:
                consecutivo = res
            res = 0
    if res > consecutivo:
                consecutivo = res
    print(consecutivo)
    return menu()

import matplotlib.pyplot as plt
def grafTabMeteo(tabMeteo):
    dia = []
    tmin = []
    tmax = []
    prec = []
    for dias in tabMeteo:
        dia.append(str(dias[0]))
        tmin.append(dias[1])
        tmax.append(dias[2])
        prec.append(dias[3])
   
    plt.plot(dia, tmin, linewidth = 0,
         marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel("Dias")
    plt.ylabel("Temperatua Mínima")
    plt.title("TEMPERATURAS MÍNIMAS")
    plt.show()

    plt.plot(dia, tmax, linewidth = 0,
         marker='o', markerfacecolor='orange', markersize=12)
    plt.xlabel("Dias")
    plt.ylabel("Temperatua Máxima")
    plt.title("TEMPERATURAS MÁXIMAS")
    plt.show()

    plt.plot(dia, prec, linewidth = 0,
         marker='o', markerfacecolor='cyan', markersize=12)
    plt.xlabel("Dias")
    plt.ylabel("Precipitação")
    plt.title("PRECIPITAÇÃO")
    plt.show()
    return menu()


def menu():
    print("""MENU:
    1. Inserir tabela de dados
    2. Temperaturas Médias
    3. Guardar tabela meteorológica
    4. Carregar tabela meteorológica
    5. Temperatura mínima geral
    6. Amplitudes Térmicas
    7. Dia mais chuvoso
    8. Dias chuvosos
    9. Maior número de dias consecutivos de calor
    10. Gráficos temperaturas mínima, máxima e pluviosidade
    0. Sair da Aplicação """)

    op = int(input("Introduza a operação que pretende efetuar: "))

    if op == 1:
        if tabMeteo == []:
            print("Será criada uma nova tabela.")
        else:
            print("Já existe uma tabela que será substituída.")
        dados()
    elif op == 0:
        print("Programa terminado!")
    elif op == 4:
        carregaTabMeteo(fnome)
    elif tabMeteo == []:
        print("Para esta operação, terá que criar uma tabela primeiramente.")
        dados()
    elif op == 2:
        medias(tabMeteo)
    elif op == 3:
        guardaTabMeteo(tabMeteo, fnome)
    elif op == 5:
        minMin(tabMeteo)
    elif op == 6:
        amplTerm(tabMeteo)
    elif op == 7:
        maxChuva(tabMeteo)
    elif op == 8:
        diasChuvosos(tabMeteo)
    elif op == 9:
        maxPeriodoCalor(tabMeteo)
    elif op == 10:
        grafTabMeteo(tabMeteo)
    else:
        op = input(int("Essa opção não existe, escolha outra: "))

    return

menu()
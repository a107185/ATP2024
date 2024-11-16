#TPC8 - TESTE DE AFERIÇÃO

#tpc1
#a)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [n for n in lista1 if n not in lista2] + [n for n in lista2 if n not in lista1]
print(ncomuns)

#b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
palavras = texto.split(" ")
lista = [palavra for palavra in palavras if len(palavra)>3]
print(lista)

#c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(ind + 1, valor) for ind, valor in enumerate(lista)]
print(listaRes)

#tpc2
#a)
def strCount(s, subs):
    vezes = 0
    while len(s) >= len(subs):
        if s[:len(subs)] == subs:
            vezes = vezes + 1
            s = s[len(subs):]
        else:
            s = s[1:]
    return vezes

print(strCount("catcowcat", "cat"), strCount("catcowcat", "cow"), strCount("catcowcat", "dog"))

#b)
def produtoM3(lista):
    novaLista = []
    while len(novaLista) < 3:
        menor = lista[0]
        for num in lista:
            if num < menor:
                menor = num
        novaLista.append(menor)
        lista.remove(menor)
    produto = novaLista[0] * novaLista[1] * novaLista[2]
    return produto 

print(produtoM3([12,3,7,10,12,8,9]))

#OUTRA FORMA MAIS SIMPLIFICADA
def produtoM3Simplificado(lista):
    lista = sorted(lista)
    return lista[0] * lista[1] * lista[2]

print(produtoM3Simplificado([12,3,7,10,12,8,9]))

#c)
def reduxInt(n):
    while n >= 10:
        soma = 0
        n = str(n)
        for car in n:
            soma = soma + int(car)
        n = soma
    return n

print(reduxInt(777))

#d)
def myIndexOf(s1, s2):
    i = 0
    res = -1
    while i < len(s1) - len(s2):
        if s1[i:(len(s2) + i)] == s2:
            res = i
            i = i + 1
        else: 
            i = i + 1
    return res

print(myIndexOf("Hoje está um belo dia de sol!", "belo"))
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))
      


#tpc3
#a)
def quantosPost(redeSocial):
    return len(redeSocial)

#b)
def postsAutor(redeSocial, autor):
    posts = []
    for post in redeSocial:
        if post["autor"] == autor:
            posts.append(post)
    return posts

#c)
def autores(redeSocial):
    autores = []
    for post in redeSocial:
        if post["autor"] not in autores:
            autores.append(post["autor"])
    autores.sort()
    return autores

#d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    listaID = []
    for post in redeSocial:
        listaID.append(int(post["id"][1:]))
    listaID.sort()
    print(listaID)
    i = 1
    while i in listaID:
        i = i + 1
    id = f"p{i}"
    dici = {"id" : id, "conteudo" : conteudo, "autor" : autor, "dataCriação" : dataCriacao, "comentarios" : comentarios}
    redeSocial.append(dici)
    return redeSocial

#e)
def remPost(redeSocial, id):
    for post in redeSocial:
        if post["id"] == id:
            redeSocial.remove(post)   
    return redeSocial

#f)
#número de posts
def postsPorAutorNum(redeSocial):
    distrib = {}
    for post in redeSocial:
        if post["autor"] in distrib:
            distrib[post["autor"]] = distrib[post["autor"]] + 1
        else:
            distrib[post["autor"]] = 1
    return distrib

#posts
def postsPorAutor(redeSocial):
    distrib = {}
    for post in redeSocial:
        if post["autor"] in distrib:
            list = distrib[post["autor"]]
            list.append(post)
        else:
            distrib[post["autor"]] = [post]
    return distrib

#g)
def comentadoPor(redeSocial, autor):
    lista = []
    for post in redeSocial:
        if "comentarios" in post:
            for comentario in post["comentarios"]:
                if comentario["autor"] == autor:
                    lista.append(post)
    return lista

#TESTE DO TPC3
rede =[{'id': 'p1', 'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas', 'autor': 'jcr', 'dataCriacao': '2023-07-20', 'comentarios': [{'comentario': 'Completamente de acordo...','autor': 'ala'},{'comentario': 'Mas há quem goste...','autor': 'jj'}]},
        {'id': 'p2', 'conteudo': 'Bom dia!', 'autor': 'joana', 'dataCriacao': '2024-07-21', 'comentarios': [{'comentario': 'Olá','autor': 'Ana'},{'comentario': 'Oi','autor': 'jj'}]},
        {'id': 'p5', 'conteudo': 'Boa noite!', 'autor': 'ana', 'dataCriacao': '2025-07-21', 'comentarios': [{'comentario': 'BUENAS','autor': 'prh'},{'comentario': 'EW','autor': 'jj'}]},
        {'id': 'p4', 'conteudo': 'Boa tarde!', 'autor': 'joana', 'dataCriacao': '2026-07-21', 'comentarios': [{'comentario': 'SIM','autor': 'prh'},{'comentario': 'NÃO','autor': 'LORAINE'}]}]

print(quantosPost(rede))
print(postsAutor(rede, "joana"))
print(autores(rede))
print(insPost(rede,"Boa ceia!","maria","2028-07-21",[{"comentario" : "sim", "autor": "paula"}]))
print(remPost(rede, "p3"))
print(postsPorAutorNum(rede))
print(postsPorAutor(rede))
print(comentadoPor(rede, "jj"))

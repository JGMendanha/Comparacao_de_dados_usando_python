import matplotlib.pyplot as mp
import networkx as nx
import numpy as np

def mostrar_selecionados(checkbox_vars, partidos, ano,treshold):
    partidos_selecionados = []
    for i, var in enumerate(checkbox_vars):
        selecionado = var.get()
        if selecionado:
            partidos_selecionados.append(partidos[i])
    normalizacao(partidos_selecionados, ano,treshold)

def normalizacao(partidos_selecionados, ano,treshold):

    grafo_analise_treshold = nx.Graph()
    grafo_analise = nx.Graph()
    deputados = []
    arquivo_politician = "dataset/politicians" + ano + ".txt"
    arquivo_grafo = "dataset/graph" + ano + ".txt"
    partido_deputado = {}
    
    with open(arquivo_politician, 'r', encoding='utf-8') as file:
        candidatos = []
        grafo_qnt_votos = {}
        for linha  in file:
            elementos = linha.strip().split(';')
            if elementos[1] in partidos_selecionados:
                candidatos.append(elementos[0])
                partido_deputado[elementos[0]] = elementos[1]
                grafo_qnt_votos[elementos[0]] = int(elementos[2])
                
    with open(arquivo_grafo, 'r', encoding='utf-8') as file:
        for linha  in file:
            elementos = linha.strip().split(';')
            if elementos[0] in candidatos  and elementos[1] in candidatos:
                peso = int(elementos[2])/min(grafo_qnt_votos[elementos[0]], grafo_qnt_votos[elementos[1]])
                grafo_analise.add_edge(elementos[0], elementos[1], weight = peso)
                grafo_analise_treshold.add_edge(elementos[0], elementos[1], weight = 1 - peso)
                if peso < float(treshold):
                    grafo_analise_treshold.remove_edge(elementos[0],elementos[1])
                    deputados.append(elementos[0])

    betweenness = nx.betweenness_centrality(grafo_analise_treshold)
    #plotagem(grafo_analise_treshold, partidos_selecionados, partido_deputado)
    #grafico(betweenness, deputados)
    heatmap(grafo_analise, partido_deputado, partidos_selecionados)

def grafico(betweenness, lista_deputados):
    fig, ax = mp.subplots(figsize = (10, 6))

    medidas_centralidade = []

    for deputado in lista_deputados:
        medidas_centralidade.append(betweenness[deputado])

    bar_labels = 'black'
    bar_colors = 'tab:blue'

    ax.bar(lista_deputados, medidas_centralidade, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Betweenness')
    ax.set_xlabel('Deputados')
    ax.set_title('Medida de centralidade')

    mp.xticks(rotation=45, ha="right", fontsize=6)
    mp.tight_layout()

    mp.savefig("grafico.png", dpi=140, bbox_inches='tight')

def plotagem(grafo, partidos, partido_deputado):
    cores = [
        (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
        (1.0, 0.4980392156862745, 0.054901960784313725),
        (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
        (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
        (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
        (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
        (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
        (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
        (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
        (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)
    ]
    cores_partido = {}
    cor_no = []

    for i in range(len(partidos)):
       cores_partido[partidos[i]] = cores[i]
    
    for deputado in grafo.nodes():
        cor_no.append(cores_partido[partido_deputado[deputado]])
    
    layout = nx.spring_layout(grafo)
    fig, ax = mp.subplots()
    mp.figure(num=None, figsize=(10, 6), dpi=140)
    nx.draw(grafo, pos=layout, with_labels=True, node_size=10, node_color=cor_no, font_size=6, width=0.1)
    mp.savefig("plotagem.png", bbox_inches='tight')
    mp.show()

def heatmap(grafo, partido_deputado, partidos_selecionados):
    labels = []
    nos = sorted(grafo.nodes(), key=str.lower)
    adj_matrix = nx.adjacency_matrix(grafo, nodelist=grafo.nodes()).todense()

    for i in range(len(partidos_selecionados)):
        for deputado in partido_deputado:
            if partido_deputado[deputado] == partidos_selecionados[i]:
                label = deputado + "(" + partidos_selecionados[i] + ")"
                labels.append(label)

    labels = sorted(labels, key=str.lower)
 
    fig, ax = mp.subplots(figsize=(10, 6), dpi=160)
    mp.xticks(rotation=45, ha='right', fontsize=4)
    mp.yticks(range(len(labels)), labels, fontsize=4)
    mp.plot(labels, labels)

    heatmap = ax.imshow(adj_matrix, cmap='hot', interpolation='nearest')
    fig.colorbar(heatmap, ax=ax)
    
    mp.subplots_adjust(bottom=0.2)
    
    mp.title('Heatmap')
    mp.savefig("heatmap.png", bbox_inches='tight')
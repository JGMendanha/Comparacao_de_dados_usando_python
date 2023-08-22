import matplotlib.pyplot as mp
import networkx as nx

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
    chave_remove = []

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
                if peso >= float(treshold):
                    grafo_analise_treshold.add_edge(elementos[0],elementos[1], weight = (1 - peso))
                    deputados.append(elementos[0])
                else:
                    chave_remove.append(elementos[0])

    betweenness = nx.betweenness_centrality(grafo_analise_treshold)
    #grafico(betweenness, deputados)
    plotagem(grafo_analise_treshold, partidos_selecionados, partido_deputado, chave_remove)

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

def plotagem(grafo, partidos, partido_deputado, chave_remove):
    #print(partido_deputado)
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
    
    for deputado in partido_deputado:
       if deputado not in chave_remove:
        cor_no.append(cores_partido[partido_deputado[deputado]])
    
    layout = nx.spring_layout(grafo)
    nx.draw(grafo, pos=layout, with_labels=True, node_size=300, node_color=cor_no, font_size=10)
    mp.show()
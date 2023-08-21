import matplotlib.pyplot as mp

def mostrar_selecionados(checkbox_vars, partidos, ano,treshold):
    partidos_selecionados = []
    for i, var in enumerate(checkbox_vars):
        selecionado = var.get()
        if selecionado:
            partidos_selecionados.append(partidos[i])
    normalizacao(partidos_selecionados, ano,treshold)

def normalizacao(partidos_selecionados, ano,treshold):

    grafo_analise = {}
    arquivo_politician = "dataset/politicians" + ano + ".txt"
    arquivo_grafo = "dataset/graph" + ano + ".txt"

    with open(arquivo_politician, 'r', encoding='utf-8') as file:
        candidatos = []
        grafo_qnt_votos = {}
        for linha  in file:
            elementos = linha.strip().split(';')
            if elementos[1] in partidos_selecionados:
                candidatos.append(elementos[0])
                grafo_qnt_votos[elementos[0]] = int(elementos[2])

    with open(arquivo_grafo, 'r', encoding='utf-8') as file:
        for linha  in file:
            elementos = linha.strip().split(';')
            if elementos[0] in candidatos  and elementos[1] in candidatos:
                peso = int(elementos[2])/min(grafo_qnt_votos[elementos[0]], grafo_qnt_votos[elementos[1]])
                if peso >= float(treshold):
                    grafo_analise[elementos[0]] = {}
                    grafo_analise[elementos[0]][elementos[1]] = 1 - peso
    print(grafo_analise)

def grafico():
    fig, ax = mp.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    mp.show()
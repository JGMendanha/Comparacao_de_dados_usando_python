import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import funcoes as f

def tela_resultado(checkbox_vars, partidos,s,treshold): 
    tela_resultado = tk.Toplevel(root)
    tela_resultado.title("Nova Tela")
    
    valor_digitado = treshold.get()
    mensagem = f"Resultados considerando um Treshold de {valor_digitado}"
    mensagem_inicial = tk.Label(tela_resultado, text=mensagem)
    mensagem_inicial.pack(padx=20, pady=20)
    mensagem_inicial.configure(font=("Helvetica", 14))

    mensagem2 = f"As imagens foram baixadas na pasta do arquivo e poderão ser vistas em abas que serão abertas "
    orientacao_basica = tk.Label(tela_resultado, text=mensagem2)
    orientacao_basica.pack(padx=20, pady=20)
    orientacao_basica.configure(font=("Helvetica", 14))

    tela_resultado.geometry(f"900x500")
    tela_resultado.geometry(f"+150-57")

    def fechar_nova_tela():
        tela_resultado.destroy() 
        root.deiconify()  

    voltar_botao = tk.Button(tela_resultado, text="Voltar", command=fechar_nova_tela)
    voltar_botao.place(x = 400, y = 450)
    voltar_botao.configure(font=("Helvetica", 14))

    f.mostrar_selecionados(checkbox_vars, partidos,s,valor_digitado)

def selecionar_partidos():
    root.withdraw()  
    tela_selecao_partido = tk.Toplevel(root)
    tela_selecao_partido.title("Nova Tela")
    tela_selecao_partido.geometry(f"900x500")
    tela_selecao_partido.geometry(f"+500-300")

    mensagem = '''Selecione os partidos que deseja fazer as comparações'''

    mensagem_inicial = tk.Label(tela_selecao_partido, text=mensagem)
    mensagem_inicial.place(x=220, y=20)
    mensagem_inicial.configure(font=("Helvetica", 14))

    selecionado = tree_anos.selection()
    s = tree_anos.item(selecionado, "text")

    arquivo_ano = "dataset/politicians" + str(s) + ".txt"

    with open(arquivo_ano, 'r', encoding='utf-8') as file:
        partidos =[]
        for linha in file:
            elementos = linha.strip().split(';')
            if elementos[1] not in partidos:
                partidos.append(elementos[1])

    checkbox_vars = []

    lista_partido = tk.Frame(tela_selecao_partido) 
    lista_partido.place(x=440, y= 200, anchor="center") 

    for i, partido in enumerate(partidos):
        linha = i // 3
        coluna = i % 3
        var = tk.BooleanVar(value=False)
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(lista_partido, text=partido, variable=var)
        checkbox.configure(font=("Helvetica", 14))
        checkbox.grid(row=linha, column=coluna, sticky="w")
    
    digite_treshold = tk.Label(tela_selecao_partido,text="Digite o Threshold (0.0 - 1.0):")
    digite_treshold.pack()
    digite_treshold.configure(font=("Helvetica", 14))
    digite_treshold.place(x = 250, y = 350)
    captura_treshold = tk.Entry(tela_selecao_partido,width=5, )  
    captura_treshold.pack()
    captura_treshold.place(x = 500, y = 350)
    captura_treshold.configure(font=("Helvetica", 14))

    resultados = tk.Button(tela_selecao_partido, text="Mostrar resultados", command=lambda:  tela_resultado(checkbox_vars, partidos,s,captura_treshold))
    resultados.pack()
    resultados.place(x=350, y=400)
    resultados.configure(font=("Helvetica", 14))

    def fechar_nova_tela():
        tela_selecao_partido.destroy() 
        root.deiconify() 

    voltar_botao = tk.Button(tela_selecao_partido, text="Voltar", command=fechar_nova_tela)
    voltar_botao.place(x = 400, y = 450)
    voltar_botao.configure(font=("Helvetica", 14))

root = tk.Tk()
root.title("Comparação de dados de deputados e suas votações - BEM-VINDO !")
root.geometry(f"900x500")
root.geometry(f"+500-300")

mensagem = '''Bem-vindo a comparação de dados de Deputados Federais e suas votações

      Selecione o ano que deseja fazer as comparações'''

mensagem_inicial = tk.Label(root, text=mensagem)
mensagem_inicial.place(x=120, y=20)
mensagem_inicial.configure(font=("Helvetica", 14))

itens = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
    "2021", "2022", "2023"]

lista_anos = tk.Frame(root)
lista_anos.place(x=330, y=140)

tree_anos = ttk.Treeview(lista_anos, selectmode="extended", height=8)
scrollbar = ttk.Scrollbar(lista_anos, orient="vertical", command=tree_anos.yview)

tree_anos["columns"] = ("item",)
tree_anos.column("#0", width=0, stretch=tk.NO) 
tree_anos.column("item", anchor="w", width=200)
tree_anos.heading("item", text="Opções")
tree_anos.configure(yscrollcommand=scrollbar.set)
tree_anos.tag_configure("custom_font", font=("Helvetica", 14))

scrollbar.pack(side=tk.RIGHT, fill="y")
tree_anos.pack(fill="both", expand=False)

for item in itens:
    tree_anos.insert("", tk.END, text=item, values=(item,))

botao_selecionar_ano = tk.Button(root, text="Selecionar", command=selecionar_partidos)
botao_selecionar_ano.pack()
botao_selecionar_ano.place(x=375, y=400)
botao_selecionar_ano.configure(font=("Helvetica", 14))

root.mainloop()

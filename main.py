import tkinter as tk
from tkinter import ttk
import funcoes as f

def abrir_nova_tela(checkbox_vars, partidos,s,treshold):
    root.withdraw()  # Esconde a janela principal
    nova_tela = tk.Toplevel(root)
    nova_tela.title("Nova Tela")
    
    valor_digitado = treshold.get()
    mensagem = f"Resultados considerando um Treshold de {valor_digitado}"
    label = tk.Label(nova_tela, text=mensagem)
    label.pack(padx=20, pady=20)
    label.configure(font=("Helvetica", 14))

    nova_tela.geometry(f"1200x700")
    nova_tela.geometry(f"+400-200")

    f.mostrar_selecionados(checkbox_vars, partidos,s,valor_digitado)
    
    # Definindo uma função para fechar a nova tela e mostrar a janela principal novamente
    def fechar_nova_tela():
        nova_tela.destroy()  # Destroi a nova tela
        root.deiconify()  # Mostra a janela principal novamente

    voltar_botao = tk.Button(nova_tela, text="Voltar", command=fechar_nova_tela)
    voltar_botao.place(x = 550, y = 600)
    voltar_botao.configure(font=("Helvetica", 14))

def selecionar_partidos():
    root.withdraw()  # Esconde a janela principal
    nova_tela = tk.Toplevel(root)
    nova_tela.title("Nova Tela")
    nova_tela.geometry(f"900x500")
    nova_tela.geometry(f"+500-300")

    mensagem = '''Selecione os partidos que deseja fazer as comparações'''

    label = tk.Label(nova_tela, text=mensagem)
    label.place(x=220, y=20)
    label.configure(font=("Helvetica", 14))

    selecionado = tree.selection()
    s = tree.item(selecionado, "text")

    arquivo_ano = "dataset/politicians" + str(s) + ".txt"

    with open(arquivo_ano, 'r', encoding='utf-8') as file:
        partidos =[]
        for linha in file:
            elementos = linha.strip().split(';')
            if elementos[1] not in partidos:
                partidos.append(elementos[1])

    checkbox_vars = []

    frame = tk.Frame(nova_tela) 
    frame.place(x=440, y= 200, anchor="center") 

    for i, partido in enumerate(partidos):
        linha = i // 3
        coluna = i % 3
        var = tk.BooleanVar(value=False)
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(frame, text=partido, variable=var)
        checkbox.configure(font=("Helvetica", 14))
        checkbox.grid(row=linha, column=coluna, sticky="w")
    
    digite = tk.Label(nova_tela,text="Digite o Threshold (0.0 - 1.0):")
    digite.pack()
    digite.configure(font=("Helvetica", 14))
    digite.place(x = 250, y = 350)
    entrada = tk.Entry(nova_tela,width=5, )  # Defina o tamanho da entrada usando o parâmetro 'width'
    entrada.pack()
    entrada.place(x = 500, y = 350)
    entrada.configure(font=("Helvetica", 14))

    btn_mostrar = tk.Button(nova_tela, text="Mostrar resultados", command=lambda:  abrir_nova_tela(checkbox_vars, partidos,s,entrada))
    btn_mostrar.pack()
    btn_mostrar.place(x=350, y=400)
    btn_mostrar.configure(font=("Helvetica", 14))

    def fechar_nova_tela():
        nova_tela.destroy()  # Destroi a nova tela
        root.deiconify()  # Mostra a janela principal novamente

    voltar_botao = tk.Button(nova_tela, text="Voltar", command=fechar_nova_tela)
    voltar_botao.place(x = 400, y = 450)
    voltar_botao.configure(font=("Helvetica", 14))

root = tk.Tk()
root.title("Comparação de dados de deputados e suas votações - BEM-VINDO !")
root.geometry(f"900x500")
root.geometry(f"+500-300")

mensagem = '''Bem-vindo a comparação de dados de Deputados Federais e suas votações

      Selecione o ano que deseja fazer as comparações'''

label = tk.Label(root, text=mensagem)
label.place(x=120, y=20)
label.configure(font=("Helvetica", 14))

itens = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
    "2021", "2022", "2023"]

frame = tk.Frame(root)
frame.place(x=330, y=140)

tree = ttk.Treeview(frame, selectmode="extended", height=8)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)

tree["columns"] = ("item",)
tree.column("#0", width=0, stretch=tk.NO) 
tree.column("item", anchor="w", width=200)
tree.heading("item", text="Opções")
tree.configure(yscrollcommand=scrollbar.set)
tree.tag_configure("custom_font", font=("Helvetica", 14))

scrollbar.pack(side=tk.RIGHT, fill="y")
tree.pack(fill="both", expand=False)

for item in itens:
    tree.insert("", tk.END, text=item, values=(item,))

btn_mostrar = tk.Button(root, text="Selecionar", command=selecionar_partidos)
btn_mostrar.pack()
btn_mostrar.place(x=375, y=400)
btn_mostrar.configure(font=("Helvetica", 14))

root.mainloop()

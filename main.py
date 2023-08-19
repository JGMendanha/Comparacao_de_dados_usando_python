import tkinter as tk
from tkinter import ttk
import funcoes as f

def abrir_nova_tela():
    root.withdraw()  # Esconde a janela principal
    nova_tela = tk.Toplevel(root)
    nova_tela.title("Nova Tela")
    
    mensagem = "Bem-vindo à nova tela!"
    label = tk.Label(nova_tela, text=mensagem)
    label.pack(padx=20, pady=20)

    nova_tela.geometry(f"1200x700")
    nova_tela.geometry(f"+400-200")
    
    # Definindo uma função para fechar a nova tela e mostrar a janela principal novamente
    def fechar_nova_tela():
        nova_tela.destroy()  # Destroi a nova tela
        root.deiconify()  # Mostra a janela principal novamente

    # Criando um botão na nova tela para fechar a nova tela e voltar à janela principal
    voltar_botao = tk.Button(nova_tela, text="Voltar", command=fechar_nova_tela)
    voltar_botao.place(x = 550, y = 600)

def selecionar_partidos():
    mensagem = '''Bem-vindo a comparação de dados de Deputados Federais e suas votações

    Selecione os partidos que deseja fazer as comparações'''

    label = tk.Label(root, text=mensagem)
    label.place(x=120, y=20)
    label.configure(font=("Helvetica", 14))
    itens = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011",
        "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
        "2021", "2022", "2023"]
    
    checkbox_vars = []

    frame = tk.Frame(root) 
    frame.place(x=440, y= 240, anchor="center") 

    for i, item in enumerate(itens):
        linha = i // 3
        coluna = i % 3
        var = tk.BooleanVar(value=False)
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(frame, text=item, variable=var)
        checkbox.configure(font=("Helvetica", 14))
        checkbox.grid(row=linha, column=coluna, sticky="w")

    btn_mostrar = tk.Button(root, text="Mostrar resultados", command=lambda:  f.mostrar_selecionados(checkbox_vars))
    btn_mostrar.pack()
    btn_mostrar.place(x=350, y=400)
    btn_mostrar.configure(font=("Helvetica", 14))


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
frame.place(x=330, y=130)

tree = ttk.Treeview(frame, selectmode="extended", height=9)
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

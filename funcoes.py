def mostrar_selecionados(checkbox_vars):
    for i, var in enumerate(checkbox_vars):
        selecionado = var.get()  # Obtém o estado da checkbox usando get()
        print(f"Ano {i+2003}: {'Selecionado' if selecionado else 'Não selecionado'}")
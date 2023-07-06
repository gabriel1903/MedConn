import pandas as pd
import tkinter as tk
from tkinter import ttk

# Criar dados fictícios para o exemplo
dados = {
    'Paciente': ['Dado 1', 'Dado 2', 'Dado 3', 'Dado 4', 'Dado 5'],
    'Medicamento': ['Dado A', 'Dado B', 'Dado C', 'Dado D', 'Dado E'],
    'Última receita': [10, 20, 30, 40, 50],
    'Próxima Receita': [True, False, True, False, True],
    'Situação': ['Texto 1', 'Texto 2', 'Texto 3', 'Texto 4', 'Texto 5']
}

# Criação do DataFrame
df = pd.DataFrame(dados)
pd.set_option('display.width', 100)

# Criação da janela
janela = tk.Tk()
janela.title('Tabela_teste')
largura = janela.winfo_screenwidth() * 0.8
altura = janela.winfo_screenheight() * 0.8
janela.geometry("%dx%d" % (largura, altura))
janela.state('zoomed')

# Criação da Treeview (tabela)
tree = ttk.Treeview(janela, show="headings")
tree.pack(side='right', fill='both', expand=True, padx=(250, 50), pady=(30,20))

# Definir as colunas
colunas = tuple(df.columns)
tree["columns"] = colunas

# Formatação das colunas
for coluna in colunas:
    tree.column(coluna, minwidth=100, width=100)
    tree.heading(coluna, text=coluna)

# Adicionar as linhas
for linha in df.to_numpy():
    tree.insert("", "end", values=tuple(linha))

# Criar o filtro para todos os conteúdos
filtro_frame = ttk.Frame(janela)
filtro_frame.pack(padx=10, pady=10)

ttk.Label(filtro_frame, text="Filtrar").pack(side='left')
filtro_entry = ttk.Entry(filtro_frame)
filtro_entry.pack(side='left', padx=(5, 0))

# Função para aplicar os filtros
def aplicar_filtros(event=None):
    filtro_texto = filtro_entry.get()
    filtro_resultados = df.copy()

    if filtro_texto:
        filtro_resultados = filtro_resultados.apply(lambda x: x.astype(str).str.contains(filtro_texto, case=False))

    filtro_resultados = filtro_resultados.any(axis=1)
    filtro_resultados = df[filtro_resultados]

    tree.delete(*tree.get_children())
    for linha in filtro_resultados.to_numpy():
        tree.insert("", "end", values=tuple(linha))

# Vincular o evento KeyRelease ao filtro_entry
filtro_entry.bind("<KeyRelease>", aplicar_filtros)

# Configurar scrollbars
scrollbar_x = ttk.Scrollbar(janela, orient="horizontal", command=tree.xview)
scrollbar_y = ttk.Scrollbar(janela, orient="vertical", command=tree.yview)
tree.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
scrollbar_y.place(relx=0.980, rely=0.02, relheight=0.9555, anchor='ne')

# Exibir a tabela
tree.pack(expand=True, fill="both")

# Definindo o estilo do LabelFrame
label_frame = ttk.LabelFrame(janela, text='Informações do Medicamento')
label_frame.pack(side='left', anchor='nw', padx=10, pady=10)

# Criando as caixas de entrada de texto dentro do LabelFrame
fornecedor_label = ttk.Label(label_frame, text='Fornecedor')
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
fornecedor_entry = ttk.Entry(label_frame, width=30)
fornecedor_entry.grid(row=0, column=1, padx=3, pady=5)

medicamento_label = ttk.Label(label_frame, text='Medicamento')
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
medicamento_label.grid(row=1, column=0, padx=5, pady=5)
medicamento_entry = ttk.Entry(label_frame, width=30)
medicamento_entry.grid(row=1, column=1, padx=5, pady=5)

marca_label = ttk.Label(label_frame, text='Marca')
marca_label.grid(row=2, column=0, padx=5, pady=5)
marca_entry = ttk.Entry(label_frame, width=30)
marca_entry.grid(row=2, column=1, padx=5, pady=5)

quantidade_label = ttk.Label(label_frame, text='Quantidade')
quantidade_label.grid(row=3, column=0, padx=5, pady=5)
quantidade_entry = ttk.Entry(label_frame, width=30)
quantidade_entry.grid(row=3, column=1, padx=5, pady=5)

num_ordem_label = ttk.Label(label_frame, text='Número de Ordem')
num_ordem_label.grid(row=4, column=0, padx=5, pady=5)
num_ordem_entry = ttk.Entry(label_frame, width=30)
num_ordem_entry.grid(row=4, column=1, padx=5, pady=5)








# Iniciar a janela principal
janela.mainloop()

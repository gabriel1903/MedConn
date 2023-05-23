import tkinter as tk
from tkinter import ttk
import os
import sqlite3
import textwrap
from tkinter import *
import time
from tkinter import Tk
from tkinter.ttk import Style
import tkinter.font as TkFont
from ttkbootstrap.constants import *
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview

# new approach
root = ttk.Window(themename="litera")

# Crie uma conexão com o banco de dados
conn = sqlite3.connect('database.db')

# Crie um cursor para a conexão
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS database (id INTEGER PRIMARY KEY AUTOINCREMENT, fornecedor TEXT, medicamento TEXT, marca TEXT, quantidade INTEGER, num_ordem INTEGER, solicitacao TEXT,requisicao TEXT, ordem_de_compra TEXT, empenho TEXT, observacao TEXT)')

# define a largura e altura da janela
largura = root.winfo_screenwidth() * 0.8
altura = root.winfo_screenheight() * 0.8
root.geometry("%dx%d" % (largura, altura))
root.state('zoomed')

style=ttk.Style()

# Definindo o estilo do LabelFrame
label_frame = ttk.LabelFrame(root, text='Informações do Medicamento')
label_frame.pack(side='left', anchor='nw', padx=10, pady=10)

# Fazer a consulta no banco de dados
c.execute('SELECT fornecedor, medicamento, marca, quantidade, num_ordem, solicitacao, requisicao, ordem_de_compra, empenho, observacao FROM database')
rows = c.fetchall()

# Criando as caixas de entrada de texto dentro do LabelFrame
fornecedor_label = ttk.Label(label_frame, text='Fornecedor', font=('Bierstadt', 12))
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
fornecedor_entry = ttk.Entry(label_frame, width=30)
fornecedor_entry.grid(row=0, column=1, padx=3, pady=5)

medicamento_label = ttk.Label(label_frame, text='Medicamento', font=('Bierstadt', 12))
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
medicamento_label.grid(row=1, column=0, padx=5, pady=5)
medicamento_entry = ttk.Entry(label_frame, width=30)
medicamento_entry.grid(row=1, column=1, padx=5, pady=5)

marca_label = ttk.Label(label_frame, text='Marca', font=('Bierstadt', 12))
marca_label.grid(row=2, column=0, padx=5, pady=5)
marca_entry = ttk.Entry(label_frame, width=30)
marca_entry.grid(row=2, column=1, padx=5, pady=5)

quantidade_label = ttk.Label(label_frame, text='Quantidade', font=('Bierstadt', 12))
quantidade_label.grid(row=3, column=0, padx=5, pady=5)
quantidade_entry = ttk.Entry(label_frame, width=30)
quantidade_entry.grid(row=3, column=1, padx=5, pady=5)

num_ordem_label = ttk.Label(label_frame, text='Número de Ordem', font=('Bierstadt', 12))
num_ordem_label.grid(row=4, column=0, padx=5, pady=5)
num_ordem_entry = ttk.Entry(label_frame, width=30)
num_ordem_entry.grid(row=4, column=1, padx=5, pady=5)

# define as colunas
columns = ('fornecedor', 'medicamento', 'marca', 'quantidade', 'numero_ordem',
           'Solicitação', 'requisicao', 'ordem_de_compra', 'empenho', 'observacao')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.pack(side='right', fill='both', expand=True, padx=(10, 80), pady=19)

scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview, bootstyle="default-round")
scrollbar.place(x=1128, y=1, height=795)
tree.configure(yscrollcommand=scrollbar.set)

# define estilo para cabeçalho das colunas
style.configure('Treeview', rowheight=65)

# define textos do cabeçalho das colunas
tree.heading('fornecedor', text='Fornecedor')
tree.column('fornecedor', width=100, minwidth=120, anchor="center")

tree.heading('medicamento', text='Medicamento')
tree.column('medicamento', width=125, minwidth=145, anchor="center")

tree.heading('marca', text='Marca')
tree.column('marca', width=70, minwidth=70, anchor="center")

tree.heading('quantidade', text='Quantidade')
tree.column('quantidade', width=110, minwidth=120, anchor="center")

tree.heading('numero_ordem', text='Nº de Ordem')
tree.column('numero_ordem', width=110, minwidth=130, anchor="center")

tree.heading('Solicitação', text='Solicitação')
tree.column('Solicitação', width=90, minwidth=115, anchor="center")

tree.heading('requisicao', text='Requisição')
tree.column('requisicao', width=90, minwidth=110, anchor="center")

tree.heading('ordem_de_compra', text='Ordem')
tree.column('ordem_de_compra', width=70, minwidth=90, anchor="center")

tree.heading('empenho', text='Empenho')
tree.column('empenho', width=80, minwidth=95, anchor="center")

tree.heading('observacao', text='Observação')
tree.column('observacao', width=140, minwidth=140, anchor="center")

contacts = []

# configura as tags com as cores desejadas
tree.tag_configure('linha_par', background='#ffffff')
tree.tag_configure('linha_impar', background='#cedbf5')

for contact in contacts:
    tree.insert('', tk.END, values=contact)
    tree.pack(full='x', padx=5, pady=5)
    tree.pack(side='left', fill='both', expand=True)

for row in rows:
    contacts.append(row)
    if None in row:
        # Se houver, substitui por uma string vazia
        row = ["" if val is None else val for val in row]
    tree.insert('', 'end', values=row, tags=('linha_par' if len(
        tree.get_children()) % 2 == 0 else 'linha_impar'))

# função a ser chamada quando o botão "Inserir" for pressionado
def inserir():
    # obter as informações do medicamento a partir das caixas de entrada de texto
    marca = marca_entry.get()
    quantidade = quantidade_entry.get()
    num_ordem = num_ordem_entry.get()
    fornecedor = fornecedor_entry.get()
    medicamento = medicamento_entry.get()

    if fornecedor and medicamento:
        # insere os dados na tabela
        tree.insert('', tk.END, values=(fornecedor, medicamento, marca, quantidade, num_ordem),
                    tags=('linha_par' if len(tree.get_children()) % 2 == 0 else 'linha_impar',))
        
        radio_buttons()
        
        c.execute("INSERT INTO database (fornecedor, medicamento, marca, quantidade, num_ordem) VALUES (?, ?, ?, ?, ?)",
                  (fornecedor, medicamento, marca, quantidade, num_ordem))
        conn.commit()
        
        # limpar as caixas de entrada de texto
        fornecedor_entry.delete(0, tk.END)
        medicamento_entry.delete(0, tk.END)
        marca_entry.delete(0, tk.END)
        quantidade_entry.delete(0, tk.END)
        num_ordem_entry.delete(0, tk.END)
        habilitar_botao_salvar() 
        
        inserir_button.config(bootstyle=(SUCCESS, OUTLINE))
        fornecedor_entry.config(bootstyle=(DEFAULT))
        medicamento_entry.config(bootstyle=(DEFAULT))              
    else:
        inserir_button.config(bootstyle=(DANGER, OUTLINE))
        if not fornecedor:
            fornecedor_entry.config(bootstyle=(DANGER))
        if not medicamento:
            medicamento_entry.config(bootstyle=(DANGER))

        
# Associar a tecla "Enter" do teclado à função "inserir"
fornecedor_entry.bind('<Return>', lambda event: inserir())
medicamento_entry.bind('<Return>', lambda event: inserir())
marca_entry.bind('<Return>', lambda event: inserir())
quantidade_entry.bind('<Return>', lambda event: inserir())
num_ordem_entry.bind('<Return>', lambda event: inserir())

def excluir_cliente():
    # Verifica se uma linha foi selecionada na tree view
    fornecedor_selecionado = tree.item(tree.selection())['values'][0]

    # Exclui a linha no banco de dados
    c.execute("DELETE FROM database WHERE fornecedor=?",
              (fornecedor_selecionado,))
    conn.commit()

    # Remove a linha da tree view
    tree.delete(tree.selection())

tree.bind('<Delete>', lambda event: excluir_cliente())

def editar():
    selected_item = tree.selection()
    for item in selected_item:
        # Obtenha as informações da linha selecionada
        fornecedor = tree.item(item, 'values')[0]
        medicamento = tree.item(item, 'values')[1]
        marca = tree.item(item, 'values')[2]
        quantidade = tree.item(item, 'values')[3]
        num_ordem = tree.item(item, 'values')[4]

        # Atualize as informações nos campos de entrada correspondentes
        fornecedor_entry.delete(0, tk.END)
        fornecedor_entry.insert(0, fornecedor)
        medicamento_entry.delete(0, tk.END)
        medicamento_entry.insert(0, medicamento)
        marca_entry.delete(0, tk.END)
        marca_entry.insert(0, marca)
        quantidade_entry.delete(0, tk.END)
        quantidade_entry.insert(0, quantidade)
        num_ordem_entry.delete(0, tk.END)
        num_ordem_entry.insert(0, num_ordem)
        habilitar_botao_salvar()
        desabilitar_botao_inserir()

def salvar():
    # Obtém a linha selecionada
    linha_selecionada = tree.selection()[0]

    # Obtém os valores antigos da linha selecionada
    valores = tree.item(linha_selecionada)['values']
    id = valores[0]

    # Obtém os novos valores dos campos de entrada
    fornecedor = fornecedor_entry.get()
    medicamento = medicamento_entry.get()
    marca = marca_entry.get()
    num_ordem = num_ordem_entry.get()
    quantidade = quantidade_entry.get()

    # Atualiza os valores na linha do Treeview
    tree.set(linha_selecionada, column=0, value=fornecedor)
    tree.set(linha_selecionada, column=1, value=medicamento)
    tree.set(linha_selecionada, column=2, value=marca)
    tree.set(linha_selecionada, column=3, value=quantidade)
    tree.set(linha_selecionada, column=4, value=num_ordem)

    c.execute("UPDATE database SET fornecedor=?, medicamento=?, marca=?, quantidade=?, num_ordem=? WHERE id=?",
              (fornecedor, medicamento, marca, quantidade, num_ordem, id))
    conn.commit()

    fornecedor_entry.delete(0, tk.END)
    medicamento_entry.delete(0, tk.END)
    marca_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    num_ordem_entry.delete(0, tk.END)
    habilitar_botao_inserir()
    inserir_sobre_salvar()

# Criar o botão "Inserir"
inserir_button = ttk.Button(label_frame, text='Inserir', command=lambda: [inserir()], bootstyle=(SUCCESS, OUTLINE))
inserir_button.place(relx=0.21, rely=0.80, width=250, height=35)

editar_button = ttk.Button(label_frame, text='Editar', command=lambda: [editar(), salvar_sobre_inserir()], bootstyle=(SUCCESS, OUTLINE))
editar_button.place(relx=0.21, rely=0.90, width=250, height=35)

salvar_button = ttk.Button(label_frame, text='Salvar', command=lambda: [salvar(), habilitar_botao_inserir(), inserir_sobre_salvar()], bootstyle=(SUCCESS, OUTLINE))
salvar_button.config(command=salvar)

def salvar_sobre_inserir():
    salvar_button.place(relx=0.21, rely=0.80, width=250, height=35)

def inserir_sobre_salvar():
    salvar_button.place_forget()

# cria um checkbutton fantasma, para manter o tamanho do label_frame
fantasma_label = ttk.Label(label_frame, text='')
fantasma_label.grid(row=50, column=0, padx=7, pady=85)

def habilitar_botao_salvar():
    salvar_button.config(state="normal")

def desabilitar_botao_salvar():
    salvar_button.config(state="disabled")

def habilitar_botao_inserir():
    inserir_button.config(state="normal")

def desabilitar_botao_inserir():
    inserir_button.config(state="disabled")

def radio_buttons():
    # Obtém o valor do radio button selecionado
    selecionado = radio_var.get()

    # Obtém os itens/linhas existentes na Treeview
    items = tree.get_children()

    for item in items:
        # Atualiza as colunas na Treeview com base na seleção
        if selecionado == "Solicitação":
            tree.set(item, 'Solicitação', 'OK')
            tree.set(item, 'Requisição', 'OUT')
            tree.set(item, 'Ordem', 'OUT')
            tree.set(item, 'Empenho', 'OUT')
        elif selecionado == "Requisição":
            tree.set(item, 'Solicitação', 'OK')
            tree.set(item, 'Requisição', 'OK')
            tree.set(item, 'Ordem', 'OUT')
            tree.set(item, 'Empenho', 'OUT')
        elif selecionado == "Ordem":
            tree.set(item, 'Solicitação', 'OK')
            tree.set(item, 'Requisição', 'OK')
            tree.set(item, 'Ordem', 'OK')
            tree.set(item, 'Empenho', 'OUT')
        elif selecionado == "Empenho":
            tree.set(item, 'Solicitação', 'OK')
            tree.set(item, 'Requisição', 'OK')
            tree.set(item, 'Ordem', 'OK')
            tree.set(item, 'Empenho', 'OK')

    # Limpar seleção dos radiobuttons
    radio_var.set(None)

lf_radio = ttk.LabelFrame(label_frame, text='Informações do Medicamento')
lf_radio.place(relx=0.02, rely=0.55, width=333, height=70)

# Cria os radio buttons
radio_var = tk.StringVar()

solicitacao_radio = ttk.Radiobutton(lf_radio, text="Solicitação", variable=radio_var, value="Solicitação", command=radio_buttons)
solicitacao_radio.place(relx=0.01, rely=0.06, width=80, height=35)

requisicao_radio = ttk.Radiobutton(lf_radio, text="Requisição", variable=radio_var, value="Requisição", command=radio_buttons)
requisicao_radio.place(relx=0.26, rely=0.06, width=80, height=35)

ordem_radio = ttk.Radiobutton(lf_radio, text="Ordem", variable=radio_var, value="Ordem", command=radio_buttons)
ordem_radio.place(relx=0.52, rely=0.06, width=80, height=35)

empenho_radio = ttk.Radiobutton(lf_radio, text="Empenho", variable=radio_var, value="Empenho", command=radio_buttons)
empenho_radio.place(relx=0.73, rely=0.085, width=80, height=30)


root.mainloop()

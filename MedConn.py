import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
import csv
import pickle
import os
from PIL import Image
from PIL import Image, ImageTk
import glob
import os
import sqlite3
import textwrap
from tkinter import *

root = tk.Tk()
root.title("Cadastro de Medicamentos")

# Crie uma conexão com o banco de dados
conn = sqlite3.connect('database.db')

# Crie um cursor para a conexão
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS database (fornecedor TEXT, medicamento TEXT, marca TEXT, quantidade INTEGER, num_ordem INTEGER, solicitacao TEXT,requisicao TEXT, ordem_de_compra TEXT, empenho TEXT, observacao TEXT)''')

# define a largura e altura da janela
largura = 900
altura = 700
root.geometry("%dx%d" % (largura, altura))
fonte_padrao = ("Arial", 11)
root.state('zoomed')

# Configura a fonte para todos os widgets da aplicação
root.option_add("*Font", fonte_padrao)

# Definindo o estilo do LabelFrame
style = ttk.Style()
style.configure('My.TLabelframe', background='Transparent.TLabelframe', foreground='Transparent.TLabelframe',
                borderwidth=90, relief='sunken', font=('Arial', 11), borderstyle='sunken')

label_frame = ttk.LabelFrame(root, text='Informações do Medicamento')
label_frame.grid(row=0, column=0, padx=33, pady=10)

# Fazer a consulta no banco de dados
c.execute('SELECT * FROM database')
rows = c.fetchall()

# Criando as caixas de entrada de texto dentro do LabelFrame
fornecedor_label = ttk.Label(label_frame, text='Fornecedor')
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
fornecedor_entry = ttk.Entry(label_frame, width=30)
fornecedor_entry.grid(row=0, column=1, padx=5, pady=5)

medicamento_label = ttk.Label(label_frame, text='Medicamento')
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

# define as colunas
columns = ('fornecedor', 'medicamento', 'marca', 'quantidade', 'numero_ordem',
           'solicitacao', 'requisicao', 'ordem_de_compra', 'empenho', 'observacao')
tree = ttk.Treeview(root, columns=columns, show='headings')
style.configure('Treeview', rowheight=25, bordercolor='#000000',
                borderwidth=1, separatorcolor='#000000')

# define estilo para cabeçalho das colunas
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11))

# define textos do cabeçalho das colunas
tree.heading('fornecedor', text='Fornecedor')
tree.column('fornecedor', width=100, minwidth=100)

tree.heading('medicamento', text='Medicamento')
tree.column('medicamento', width=150, minwidth=150)

tree.heading('marca', text='Marca')
tree.column('marca', width=87, minwidth=87)

tree.heading('quantidade', text='Quantidade')
tree.column('quantidade', width=80, minwidth=80)

tree.heading('numero_ordem', text='Número de Ordem')
tree.column('numero_ordem', width=85, minwidth=130)

tree.heading('solicitacao', text='Solicitação')
tree.column('solicitacao', width=90, minwidth=90)

tree.heading('requisicao', text='Requisição')
tree.column('requisicao', width=45, minwidth=45)

tree.heading('ordem_de_compra', text='Ordem de Compra')
tree.column('ordem_de_compra', width=90, minwidth=90)

tree.heading('empenho', text='Empenho')
tree.column('empenho', width=40, minwidth=40)

tree.heading('observacao', text='Observação')
tree.column('observacao', width=350, minwidth=350)

contacts = []

# configura as tags com as cores desejadas
tree.tag_configure('linha_par', background='#ffffff')
tree.tag_configure('linha_impar', background='#e6e3e3')

for contact in contacts:
    tree.insert('', tk.END, values=contact)
    tree.place(relx=0.02, rely=0.65, relwidth=0.959)

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.place(relx=0.99, rely=0.64, relheight=0.345, anchor='ne')
tree.place(relx=0.02, rely=0.65, relwidth=0.959)

for row in rows:
    contacts.append(row)
    if None in row:
        # Se houver, substitui por uma string vazia
        row = ["" if val is None else val for val in row]
    tree.insert('', 'end', values=row, tags=('linha_par' if len(tree.get_children()) % 2 == 0 else 'linha_impar'))
  

# communicate back to the scrollbar
tree['yscrollcommand'] = scrollbar.set

# função a ser chamada quando o botão "Inserir" for pressionado


def inserir():
    # obter as informações do medicamento a partir das caixas de entrada de texto
    marca = marca_entry.get()
    quantidade = quantidade_entry.get()
    num_ordem = num_ordem_entry.get()
    fornecedor = fornecedor_entry.get()
    medicamento = medicamento_entry.get()

    # Execute a consulta SQL para inserir os dados na tabela
    c.execute("INSERT INTO database (fornecedor, medicamento, marca, quantidade, num_ordem) VALUES (?, ?, ?, ?, ?)",
              (fornecedor, medicamento, marca, quantidade, num_ordem))

    # Salve as alterações no banco de dados
    conn.commit()

    if fornecedor and medicamento:
        # insere os dados na tabela
        tree.insert('', tk.END, values=(fornecedor, medicamento, marca, quantidade, num_ordem), tags=('linha_par' if len(tree.get_children()) % 2 == 0 else 'linha_impar',))
        error_label.config(text=error_message, fg=root.cget('bg'))
    else:
        error_label.config(text=error_message, fg='red',
                           font=("TkDefaultFont", 11,))

    # limpar as caixas de entrada de texto
    fornecedor_entry.delete(0, tk.END)
    medicamento_entry.delete(0, tk.END)
    marca_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    num_ordem_entry.delete(0, tk.END)


error_message = 'Fornecedor ou Medicamento não informado'
error_label = tk.Label(text=error_message, fg=root.cget('bg'))
error_label.place(relx=0.13, rely=0.289, width=290, height=30)

check = tk.PhotoImage(file='imagens\checkredimensionado.png').subsample(5, 5)

# criar o botão "Inserir"
inserir_button = ttk.Button(
    root, text='Inserir', command=inserir, image=check, compound=RIGHT)
inserir_button.place(relx=0.02, rely=0.31, width=150, height=30)

def save_item(self):
    fornecedor = self.fornecedor_entry.get()
    medicamento = self.medicamento_entry.get()
    marca = self.marca_entry.get()
    quantidade = self.quantidade_entry.get()
    num_ordem = self.num_ordem_entry.get()

    self.insert_item('fornecedor', 'medicamento',
                     'marca', 'quantidade', 'num_ordem')
    self.fornecedor_entry.delete(0, tk.END)
    self.medicamento_entry.delete(0, tk.END)
    self.marca_entry.delete(0, tk.END)
    self.quantidade_entry.delete(0, tk.END)
    self.num_ordem_entry.delete(0, tk.END)


combo_box = tk.StringVar(value="Selecione uma opção")
combo_box_options = ["Solicitação", "Requisição", "Ordem de compra", "Empenho"]
combo_box_menu = tk.OptionMenu(label_frame, combo_box, *combo_box_options)
combo_box_menu.place(relx=0.355, rely=0.78, width=250)

# cria um checkbutton fantasma, para manter o tamanho do label_frame
fantasma_label = ttk.Label(label_frame, text='')
fantasma_label.grid(row=9, column=0, padx=7, pady=14)

def excluir_cliente():
    # Verifica se uma linha foi selecionada na tree view
    if len(tree.selection()) == 0:
        return
    
    # Recupera o ID da linha selecionada
    fornecedor_selecionado = tree.item(tree.selection())['values'][0]
    
    # Exclui a linha no banco de dados
    c.execute("DELETE FROM database WHERE fornecedor=?", (fornecedor_selecionado,))
    conn.commit()
    
    # Remove a linha da tree view
    tree.delete(tree.selection())

# Adiciona o botão de exclusão
excluir = tk.PhotoImage(file='imagens\excluir.png').subsample(3, 3)
botao_excluir = ttk.Button(root, text='', command=inserir, image=excluir, compound=CENTER)
botao_excluir.place(relx=0.954, rely=0.59, width=40, height=40)
botao_excluir.config(command=excluir_cliente)

root.mainloop()
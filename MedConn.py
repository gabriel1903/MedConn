import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import Image, ImageTk
import glob
import os
import sqlite3
import textwrap
from tkinter import *
import time
from PIL import Image
from tkinter import Tk
from tkinter.ttk import Style
from ttkthemes import ThemedTk
import TKinterModernThemes as TKMT
import tkinter.font as TkFont
from tkFont import Font
from ttk import Style, Treeview
from Tkinter import *
    
root = tk.Tk()
# Import the tcl file
root.tk.call('source', 'Forest-ttk-theme-1.0/forest-light.tcl')


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
fornecedor_entry.grid(row=0, column=1, padx=5, pady=5)

medicamento_label = ttk.Label(label_frame, text='Medicamento', font=('Bierstadt', 12))
fornecedor_label.grid(row=0, column=0, padx=5, pady=5)
medicamento_label.grid(row=1, column=0, padx=5, pady=5)
medicamento_entry = ttk.Entry(label_frame, width=30)
medicamento_entry.grid(row=1, column=1, padx=5, pady=5)

marca_label = ttk.Label(label_frame, text='Marca', font=('Bierstadt', 12, 'bold'))
marca_label.grid(row=2, column=0, padx=5, pady=5)
marca_entry = ttk.Entry(label_frame, width=30)
marca_entry.grid(row=2, column=1, padx=5, pady=5)

quantidade_label = ttk.Label(label_frame, text='Quantidade', font=('Bierstadt', 12, 'bold'))
quantidade_label.grid(row=3, column=0, padx=5, pady=5)
quantidade_entry = ttk.Entry(label_frame, width=30)
quantidade_entry.grid(row=3, column=1, padx=5, pady=5)

num_ordem_label = ttk.Label(label_frame, text='Número de Ordem', font=('Bierstadt', 12, 'bold'))
num_ordem_label.grid(row=4, column=0, padx=5, pady=5)
num_ordem_entry = ttk.Entry(label_frame, width=30)
num_ordem_entry.grid(row=4, column=1, padx=5, pady=5)

# define as colunas
columns = ('fornecedor', 'medicamento', 'marca', 'quantidade', 'numero_ordem',
           'Solicitação', 'requisicao', 'ordem_de_compra', 'empenho', 'observacao')
tree = ttk.Treeview(root, columns=columns, show='headings')

# define estilo para cabeçalho das colunas
ttk.Style().theme_use('forest-light')
style = ttk.Style()
style.configure("Treeview.Heading", font=('Bierstadt', 12), rowheight=90)
style = ttk.Style(root) 
style.configure('Treeview', rowheight=40)
                                        
# define textos do cabeçalho das colunas
tree.heading('fornecedor', text='Fornecedor')
tree.column('fornecedor', width=90, minwidth=90)

tree.heading('medicamento', text='Medicamento')
tree.column('medicamento', width=105, minwidth=105)

tree.heading('marca', text='Marca')
tree.column('marca', width=70, minwidth=70)

tree.heading('quantidade', text='Quantidade')
tree.column('quantidade', width=120, minwidth=120)

tree.heading('numero_ordem', text='Número de \n Ordem', anchor='w')
tree.column('numero_ordem', width=100, minwidth=100)

tree.heading('Solicitação', text='Solicitação')
tree.column('Solicitação', width=80, minwidth=80)

tree.heading('requisicao', text='Requisição')
tree.column('requisicao', width=80, minwidth=80)

tree.heading('ordem_de_compra', text='Ordem de \n Compra')
tree.column('ordem_de_compra', width=90, minwidth=90)

tree.heading('empenho', text='Empenho')
tree.column('empenho', width=80, minwidth=80)

tree.heading('observacao', text='Observação')
tree.column('observacao', width=300, minwidth=300)

contacts = []

# configura as tags com as cores desejadas
tree.tag_configure('linha_par', background='#ffffff')
tree.tag_configure('linha_impar', background='#e6e3e3')

for contact in contacts:
    tree.insert('', tk.END, values=contact)
    tree.pack(full='x', padx=5, pady=5)
    tree.pack(side='left', fill='both', expand=True)
# criar um widget de barra de rolagem e definir seu comando para a treeview
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.place(relx=0.953, rely=0.055, relheight=0.80, anchor='ne')
tree.pack(side='right', fill='both', expand=True, padx=(10, 80), pady=19)
tree.configure(yscrollcommand=scrollbar.set)
tree['yscrollcommand'] = scrollbar.set

horizontalscrollbar = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
horizontalscrollbar.place(relx=0.306, rely=0.965, relwidth=0.642)
horizontalscrollbar.config(command=tree.xview)
tree.configure(xscrollcommand=horizontalscrollbar.set)
tree['xscrollcommand'] = horizontalscrollbar.set


for row in rows:
    contacts.append(row)
    if None in row:
        # Se houver, substitui por uma string vazia
        row = ["" if val is None else val for val in row]
    tree.insert('', 'end', values=row, tags=('linha_par' if len(
        tree.get_children()) % 2 == 0 else 'linha_impar'))

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

    if fornecedor and medicamento:
        # insere os dados na tabela
        tree.insert('', tk.END, values=(fornecedor, medicamento, marca, quantidade, num_ordem),
                    tags=('linha_par' if len(tree.get_children()) % 2 == 0 else 'linha_impar',))
        error_label.config(text=error_message, fg=root.cget('bg'))
    else:
        error_label.config(text=error_message, fg='red')

    c.execute("INSERT INTO database (fornecedor, medicamento, marca, quantidade, num_ordem) VALUES (?, ?, ?, ?, ?)",
              (fornecedor, medicamento, marca, quantidade, num_ordem))
    conn.commit()

    # limpar as caixas de entrada de texto
    fornecedor_entry.delete(0, tk.END)
    medicamento_entry.delete(0, tk.END)
    marca_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    num_ordem_entry.delete(0, tk.END)

# Associar a tecla "Enter" do teclado à função "inserir"
fornecedor_entry.bind('<Return>', lambda event: inserir())
medicamento_entry.bind('<Return>', lambda event: inserir())
marca_entry.bind('<Return>', lambda event: inserir())
quantidade_entry.bind('<Return>', lambda event: inserir())
num_ordem_entry.bind('<Return>', lambda event: inserir())

error_message = 'Fornecedor ou Medicamento não informado'
error_label = tk.Label(text=error_message, fg=root.cget('bg'))
error_label.place(relx=0.13, rely=0.35, width=290, height=30)

# Criar o botão "Inserir"
inserir_button = ttk.Button(root, text='Inserir', command=inserir, compound='right')
inserir_button.config = tk.PhotoImage(file='check.png')
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


# cria um checkbutton fantasma, para manter o tamanho do label_frame
fantasma_label = ttk.Label(label_frame, text='')
fantasma_label.grid(row=9, column=0, padx=7, pady=14)

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
        desabilitar_botao_salvar()
    # Salve as alterações no banco de dados

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
    desabilitar_botao_salvar()
    habilitar_botao_inserir()


editar_button = ttk.Button(root, text='Editar', command=lambda: [
                           editar(), habilitar_botao_salvar(), desabilitar_botao_inserir()])
editar_button.place(relx=0.8, rely=0.59, width=40, height=40)

salvar_button = ttk.Button(root, text='Salvar', command=salvar)
salvar_button = ttk.Button(
    root, text='Salvar', command=salvar, state="disable")
salvar_button.place(relx=0.7, rely=0.59, width=40, height=40)
salvar_button.config(command=salvar)

# Adiciona o botão de exclusão
botao_excluir = ttk.Button( root, text='Excluir', compound=CENTER)
botao_excluir.place(relx=0.9455, rely=0.59, width=40, height=40)


def habilitar_botao_salvar():
    salvar_button.config(state="normal")

def desabilitar_botao_salvar():
    salvar_button.config(state="disabled")

def habilitar_botao_inserir():
    inserir_button.config(state="normal")

def desabilitar_botao_inserir():
    inserir_button.config(state="disabled")


# definindo a string da combobox
combo_box = tk.StringVar(value="Selecione uma opção")
combo_box_options = ["Solicitação", "Requisição", "Ordem de compra", "Empenho"]
combo_box_menu = ttk.OptionMenu(label_frame, combo_box, *combo_box_options)
combo_box_menu.place(relx=0.355, rely=0.78, width=250)

salvar_button = ttk.Button(
    root, text='Salvar', command=salvar, state="disable")
salvar_button.place(relx=0.7, rely=0.59, width=40, height=40)
salvar_button.config(command=salvar)

def config_menu():
    options_window = tk.Toplevel(root)
    options_window.title("Configurações")
    options_window.geometry("600x450")
    
    label1 = ttk.LabelFrame(options_window, text="Opção 1")
    check1 = ttk.Checkbutton(label1)
    check1.pack(side=tk.RIGHT)

    label2 = ttk.LabelFrame(options_window, text="Opção 2")
    check2 = ttk.Checkbutton(label2)
    check2.pack(side=tk.RIGHT)

    # Posiciona os labels na janela principal
    label1.pack()
    label2.pack()   

root.mainloop()

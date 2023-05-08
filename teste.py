import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Lista de seleção
        self.options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])
        
        self.option_menu = ttk.OptionMenu(self, self.selected_option, *self.options, command=self.change_option)
        self.option_menu.pack()
        
        # Treeview
        self.treeview = ttk.Treeview(self)
        self.treeview.pack()
        
        self.treeview["columns"] = ("column1", "column2", "column3", "column4")
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("column1", width=100, minwidth=100, stretch=tk.NO)
        self.treeview.column("column2", width=100, minwidth=100, stretch=tk.NO)
        self.treeview.column("column3", width=100, minwidth=100, stretch=tk.NO)
        self.treeview.column("column4", width=100, minwidth=100, stretch=tk.NO)
        
        self.treeview.heading("#0", text="", anchor=tk.W)
        self.treeview.heading("column1", text="Column 1", anchor=tk.W)
        self.treeview.heading("column2", text="Column 2", anchor=tk.W)
        self.treeview.heading("column3", text="Column 3", anchor=tk.W)
        self.treeview.heading("column4", text="Column 4", anchor=tk.W)
        
        self.treeview.bind("<ButtonRelease-1>", self.insert_row)
        
    def change_option(self, selected):
        self.selected_option.set(selected)
        
    def insert_row(self, event):
        option_index = self.options.index(self.selected_option.get())
        column_name = "column" + str(option_index + 1)
        image = tk.PhotoImage(file="imagens\check.png") # Substitua "path/to/image.png" pelo caminho para a imagem que deseja inserir
        
        self.treeview.insert("", "end", text="", values=["Value 1", "Value 2", "Value 3", "Value 4"])
        row_id = self.treeview.get_children()[-1]
        
        self.treeview.set(row_id, column_name, image)
        
app = Application()
app.mainloop()

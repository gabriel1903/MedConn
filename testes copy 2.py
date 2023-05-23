import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from sqlalchemy import create_engine
import sqlite3


app = ttk.Window()
colors = app.style.colors

# Crie uma conexão com o banco de dados
conn = conn = engine.connect('database.db')

# Crie um cursor para a conexão
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS database (id INTEGER PRIMARY KEY AUTOINCREMENT, fornecedor TEXT, medicamento TEXT, marca TEXT, quantidade INTEGER, num_ordem INTEGER, solicitacao TEXT,requisicao TEXT, ordem_de_compra TEXT, empenho TEXT, observacao TEXT)')







coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
    ('A158', 'Farmadding Co.', 36)
]

dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()

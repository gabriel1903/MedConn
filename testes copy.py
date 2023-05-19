import PySimpleGUI as sg

# Dados da planilha
data = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '25', 'São Paulo'],
    ['Maria', '30', 'Rio de Janeiro'],
    ['Carlos', '35', 'Curitiba']
]

# Definir layout
layout = [
    [sg.Table(values=data, headings=data[0], display_row_numbers=True, justification='left', num_rows=6, col_widths=[10, 10, 10])]
]

# Criar janela
window = sg.Window('Planilha', layout)

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Fechar a janela
window.close()

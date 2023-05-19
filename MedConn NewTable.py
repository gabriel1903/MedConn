import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QStyleFactory
# Defina o estilo desejado
style = "Fusion"  # Substitua "Fusion" pelo nome do estilo que você deseja aplicar
app = QApplication([])
# Verifique se o estilo está disponível
if style in QStyleFactory.keys():
    # Aplique o estilo
    app.setStyle(style)
else:
    print("O estilo selecionado não está disponível.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Defina a largura e altura da janela
        largura = int(self.screen().size().width() * 0.8)
        altura = int(self.screen().size().height() * 0.8)
        self.setGeometry(0, 0, largura, altura)

        # Defina um layout principal para a janela
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crie a tabela
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)  # Define o número de colunas
        self.table_widget.setHorizontalHeaderLabels(['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5'])  # Define os rótulos das colunas

        # Adicione itens à tabela
        self.add_table_row(['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'])
        self.add_table_row(['Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10'])

        # Adicione a tabela ao layout
        layout.addWidget(self.table_widget)

    def add_table_row(self, items):
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        for column, item in enumerate(items):
            table_item = QTableWidgetItem(item)
            self.table_widget.setItem(row_count, column, table_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

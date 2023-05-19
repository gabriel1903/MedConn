import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

def __init__(self):
    super().__init__()
    self.setWindowTitle("Tabela")
self.setGeometry(100, 100, 400, 300)

# Criar modelo de dados
self.model = QStandardItemModel()
self.model.setHorizontalHeaderLabels(["Coluna 1", "Coluna 2", "Coluna 3"])

        # Criar a árvore de exibição (tabela)
self.tree_view = QTreeView()
self.tree_view.setModel(self.model)

# Obter o cabeçalho da tabela
header = self.tree_view.header()
        # Definir uma altura fixa para o cabeçalho das colunas
header.setFixedHeight(50)
        # Criar campos de entrada de texto
    self.text1 = QLineEdit()
        elf.text2 = QLineEdit()
        self.text3 = QLineEdit()

        # Criar botão de inserção
        # ...

        self.button = QPushButton("Inserir")
        self.button.clicked.connect(self.inserir_dados)

        # Definir layout
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addWidget(self.text3)
        layout.addWidget(self.button)
        layout.addWidget(self.tree_view)

        # Definir o layout principal da janela
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def inserir_dados(self):
        # Obter o texto dos campos de entrada
        valor1 = self.text1.text()
        valor2 = self.text2.text()
        valor3 = self.text3.text()

        # Inserir os dados na tabela
        row = self.model.rowCount()
        item1 = QStandardItem(valor1)
        self.model.setItem(row, 0, item1)
        item2 = QStandardItem(valor2)
        self.model.setItem(row, 1, item2)
        item3 = QStandardItem(valor3)
        self.model.setItem(row, 2, item3)

        # Limpar os campos de entrada
        self.text1.clear()
        self.text2.clear()
        self.text3.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt as Qt
import client as clnt


class OrderWindow(Qtw.QDialog):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.order_count = 0

        # Add a title
        self.setWindowTitle(f"Orden de {client.name}")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Add Layout
        self.add_order_lyt = Qtw.QHBoxLayout()
        self.add_order_lbl = Qtw.QLabel("Añadir Orden:")
        self.healthy_menu_btn = Qtw.QPushButton("Menú Saludable")
        #self.healthy_menu_btn.clicked.connect()
        self.regular_menu_btn = Qtw.QPushButton("Menú Regular")
        # self.regular_menu_btn.clicked.connect()
        self.add_order_lyt.addWidget(self.add_order_lbl)
        self.add_order_lyt.addWidget(self.healthy_menu_btn)
        self.add_order_lyt.addWidget(self.regular_menu_btn)

        # Set table
        self.col_hdr = ["ID", "Descripción", "Precio ($)", "Calorias (Kcal)"]
        self.data_tbl = Qtw.QTableWidget(0, len(self.col_hdr))
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalHeaderLabels(self.col_hdr)
        self.data_tbl.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Delete btn
        self.delete_order_btn = Qtw.QPushButton("Eliminar")
        #self.delete_client_btn.clicked.connect(self.full_delete)

        self.main_lyt.addLayout(self.add_order_lyt)
        self.main_lyt.addWidget(self.data_tbl)
        self.main_lyt.addWidget(self.delete_order_btn)
        self.setLayout(self.main_lyt)

        self.show()

if __name__ == "__main__":
    # Este código se ejecutará solo cuando gui_table.py se ejecute como script
    cliente = clnt.Client(1,"Luis")
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    ventana = OrderWindow(cliente)
    sys.exit(app.exec_())
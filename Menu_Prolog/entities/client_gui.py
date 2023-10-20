import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
import table as tbl
import client as clnt


class ClientWindow(Qtw.QDialog):
    def __init__(self, rest_table):
        super().__init__()
        self.rest_table = rest_table
        self.client_count = 0

        # Add a title
        self.setWindowTitle(f"Clientes Mesa {rest_table.id_table}")
        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Set client
        self.client_lyt = Qtw.QHBoxLayout()
        self.client_lbl = Qtw.QLabel("Nombre:")
        self.client_tbox = Qtw.QLineEdit()
        self.add_client_btn = Qtw.QPushButton("Agregar")
        self.add_client_btn.clicked.connect(self.add_row)
        self.client_lyt.addWidget(self.client_lbl)
        self.client_lyt.addWidget(self.client_tbox)
        self.client_lyt.addWidget(self.add_client_btn)

        # Set table
        self.col_hdr = ["ID", "Nombre", "Total ($)"]
        self.table = Qtw.QTableWidget(0, len(self.col_hdr))
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(self.col_hdr)
        self.table.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Set btn
        self.btn_lyt = Qtw.QHBoxLayout()
        self.update_client_btn = Qtw.QPushButton("Editar Orden")
        # self.update_table_btn.clicked.connect()
        self.delete_client_btn = Qtw.QPushButton("Eliminar")
        self.delete_client_btn.clicked.connect(self.full_delete)
        self.btn_lyt.addWidget(self.update_client_btn)
        self.btn_lyt.addWidget(self.delete_client_btn)

        self.main_lyt.addLayout(self.client_lyt)
        self.main_lyt.addWidget(self.table)
        self.main_lyt.addLayout(self.btn_lyt)
        self.setLayout(self.main_lyt)

        self.show()

    def get_selected_row(self):
        try:
            selected_row = self.table.currentRow()
            return selected_row
        except Exception as e:
            print(f"Error: {e}")

    def get_client(self):
        try:
            selected_row = self.get_selected_row()
            item = self.table.item(selected_row, 0)
            id_client = item.text()
            for client in self.rest_table.clients:
                if int(client.id_client) == int(id_client):
                    return client
        except Exception as e:
            print(f"Error: {e}")

    def delete_table(self, client):
        try:
            if client in self.rest_table.clients:
                self.rest_table.clients.remove(client)
                print(f"Client with ID {client.id_client} deleted.")
            else:
                print(f"No matching client found for deletion.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_row(self, selected_row):
        try:
            self.table.removeRow(selected_row)
            print(f"Row {selected_row} deleted.")
        except Exception as e:
            print(f"Error: {e}")

    def full_delete(self):
        try:
            selected_row = self.get_selected_row()
            client = self.get_client()
            self.delete_table(client)
            self.delete_row(selected_row)
        except Exception as e:
            print(f"Error: {e}")

    def add_row(self):
        name = self.client_tbox.text()
        if name:
            # Abrir espacio en la tabla
            rows = self.table.rowCount()
            self.table.setRowCount(rows + 1)

            # Crear instancia
            new_client = clnt.Client(self.client_count + 1, name)
            self.rest_table.clients.append(new_client)
            self.client_count += 1

            for col, value in enumerate([new_client.id_client, new_client.name, new_client.bill]):
                item = Qtw.QTableWidgetItem(str(value))
                self.table.setItem(self.table.rowCount() - 1, col, item)



if __name__ == "__main__":
    # Este código se ejecutará solo cuando table_gui.py se ejecute como script
    mesa = tbl.Table(1)
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    ventana = ClientWindow(mesa)
    sys.exit(app.exec_())

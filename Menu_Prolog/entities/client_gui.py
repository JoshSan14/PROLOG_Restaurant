import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
import table as tbl
import client as clnt


class ClientWindow(Qtw.QDialog):
    def __init__(self, rest_table):
        super().__init__()
        self.rest_table = rest_table
        self.client_count = self.get_last_id()

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
        self.data_table = Qtw.QTableWidget(0, len(self.col_hdr))
        self.data_table.verticalHeader().setVisible(False)
        self.data_table.setHorizontalHeaderLabels(self.col_hdr)
        self.data_table.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.data_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        if self.client_count > 0:
            self.update_data_table()

        # Set btn
        self.btn_lyt = Qtw.QHBoxLayout()
        self.update_client_btn = Qtw.QPushButton("Editar Orden")
        # self.update_table_btn.clicked.connect()
        self.delete_client_btn = Qtw.QPushButton("Eliminar")
        self.delete_client_btn.clicked.connect(self.full_delete)
        self.btn_lyt.addWidget(self.update_client_btn)
        self.btn_lyt.addWidget(self.delete_client_btn)

        self.main_lyt.addLayout(self.client_lyt)
        self.main_lyt.addWidget(self.data_table)
        self.main_lyt.addLayout(self.btn_lyt)
        self.setLayout(self.main_lyt)

    def get_selected_row(self):
        try:
            selected_row = self.data_table.currentRow()
            return selected_row
        except Exception as e:
            print(f"Error: {e}")

    def get_client(self):
        try:
            selected_row = self.get_selected_row()
            item = self.data_table.item(selected_row, 0)
            id_client = item.text()
            for client in self.rest_table.clients:
                if int(client.id_client) == int(id_client):
                    return client
        except Exception as e:
            print(f"Error: {e}")

    def delete_client(self, client):
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
            self.data_table.removeRow(selected_row)
            print(f"Row {selected_row} deleted.")
        except Exception as e:
            print(f"Error: {e}")

    def full_delete(self):
        try:
            selected_row = self.get_selected_row()
            client = self.get_client()
            self.delete_client(client)
            self.delete_row(selected_row)
        except Exception as e:
            print(f"Error: {e}")

    def add_row(self):
        name = self.client_tbox.text()
        if name:
            # Abrir espacio en la tabla
            rows = self.data_table.rowCount()
            self.data_table.setRowCount(rows + 1)

            # Crear instancia
            client = clnt.Client(self.client_count + 1, name)
            self.rest_table.clients.append(client)
            self.client_count += 1

            for col, value in enumerate([client.id_client, client.name, client.bill]):
                item = Qtw.QTableWidgetItem(str(value))
                self.data_table.setItem(self.data_table.rowCount() - 1, col, item)

    def update_data_table(self):
        # Clear the existing data in the table
        self.data_table.setRowCount(0)

        # Populate the table with client data using list comprehensions
        data = [[str(client.id_client), client.name, str(client.bill)] for client in self.rest_table.clients]

        # Update the table with data
        for row_index, row_data in enumerate(data):
            self.data_table.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = Qtw.QTableWidgetItem(col_data)
                self.data_table.setItem(row_index, col_index, item)

    def get_last_id(self):
        try:
            if len(self.rest_table.clients) > 0:
                print(int(self.rest_table.clients[-1].id_client))
                return self.rest_table.clients[-1].id_client
            else:
                return 0
        except Exception as e:
            print(f"Error: {e} 5")


if __name__ == "__main__":
    # Este código se ejecutará solo cuando table_gui.py se ejecute como script
    mesa = tbl.Table(1)
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    ventana = ClientWindow(mesa)
    sys.exit(app.exec_())

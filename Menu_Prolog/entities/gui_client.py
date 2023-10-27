import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
import table as tbl
import client as clnt
import gui_order as ogui


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
        self.data_tbl = Qtw.QTableWidget(0, len(self.col_hdr))
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalHeaderLabels(self.col_hdr)
        self.data_tbl.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        if self.client_count > 0:
            self.load_data_table()

        # Set btn
        self.btn_lyt = Qtw.QHBoxLayout()
        self.update_client_btn = Qtw.QPushButton("Editar Orden")
        self.update_client_btn.clicked.connect(self.edit_order)
        self.delete_client_btn = Qtw.QPushButton("Eliminar")
        self.delete_client_btn.clicked.connect(self.full_delete)
        self.btn_lyt.addWidget(self.update_client_btn)
        self.btn_lyt.addWidget(self.delete_client_btn)

        self.main_lyt.addLayout(self.client_lyt)
        self.main_lyt.addWidget(self.data_tbl)
        self.main_lyt.addLayout(self.btn_lyt)
        self.setLayout(self.main_lyt)

    def get_client(self):
        try:
            selected_row = self.data_tbl.currentRow()
            item = self.data_tbl.item(selected_row, 0)
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
            self.data_tbl.removeRow(selected_row)
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
            rows = self.data_tbl.rowCount()
            self.data_tbl.setRowCount(rows + 1)

            # Crear instancia
            client = self.create_client(name)

            for col, value in enumerate([client.id_client, client.name, client.bill]):
                item = Qtw.QTableWidgetItem(str(value))
                self.data_tbl.setItem(self.data_tbl.rowCount() - 1, col, item)

    def create_client(self, name):
        client = clnt.Client(self.client_count + 1, name)
        self.rest_table.clients.append(client)
        self.client_count += 1
        return client

    def load_data_table(self):
        # Clear the existing data in the table
        self.data_tbl.setRowCount(0)

        # Populate the table with client data using list comprehensions
        data = [[str(client.id_client), client.name, str(client.bill)] for client in self.rest_table.clients]

        # Update the table with data
        for row_index, row_data in enumerate(data):
            self.data_tbl.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = Qtw.QTableWidgetItem(col_data)
                self.data_tbl.setItem(row_index, col_index, item)

    def get_last_id(self):
        try:
            if len(self.rest_table.clients) > 0:
                print(int(self.rest_table.clients[-1].id_client))
                return self.rest_table.clients[-1].id_client
            else:
                return 0
        except Exception as e:
            print(f"Error: {e} 5")

    def get_total_bill(self):
        try:
            total_bill = sum(client.bill for client in self.rest_table.clients)
            self.rest_table.total_bill = total_bill
        except Exception as e:
            print(f"Error: {e} alfa")
            return 0  # Return 0 in case of an error

    def update_data_table(self):
        pass

    def edit_order(self):
        try:
            client = self.get_client()
            order_window = ogui.OrderWindow(client)
            order_window.setModal(True)
            order_window.exec_()
            self.get_total_bill()
            #Actualizar valores
        except Exception as e:
            print(f"Error: {e} 6")

if __name__ == "__main__":
    # Este código se ejecutará solo cuando gui_table.py se ejecute como script
    mesa = tbl.Table(1)
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    ventana = ClientWindow(mesa)
    sys.exit(app.exec_())

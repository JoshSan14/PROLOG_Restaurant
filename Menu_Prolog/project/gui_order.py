import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt as Qt
import client as clnt
from utils import Utils as Utl
import gui_healthy_menu as ghm
import healthy_menu as hm
import db_conn as dbc
from regular_menu import *
from order import Order


class OrderSelectDialog(Qtw.QDialog):
    def __init__(self, db_conn, title, client, menu_object, last_id):
        super().__init__()

        self.db_conn = db_conn
        self.client = client
        self.menu_object = menu_object
        self.last_id = last_id

        self.setWindowTitle(title)
        self.main_lyt = Qtw.QVBoxLayout()

        # Set table
        self.data_tbl = Qtw.QTableWidget(0, len(self.menu_object.col_hdr))
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalHeaderLabels(self.menu_object.col_hdr)
        self.data_tbl.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()

        self.show_data()

        # Set button:
        self.select_btn = Qtw.QPushButton("Añadir a la orden")
        self.select_btn.clicked.connect(self.select_option)

        self.main_lyt.addWidget(self.data_tbl)
        self.main_lyt.addWidget(self.select_btn)

        self.setLayout(self.main_lyt)

    def show_data(self):
        records = self.menu_object.get_all_db_menu(self.db_conn)
        Utl.add_data_to_table(self.data_tbl, records)

    def select_option(self):
        selected_row = self.data_tbl.currentRow()
        row = [self.data_tbl.item(selected_row, col).text() for col in range(self.data_tbl.columnCount())]
        if type(self.menu_object) is Plate:
            formatted_combo = Utl.format_string(row, " + ", 1, 4)
            cals = round(float(row[5]), 2)
            price = round(float(row[6]), 2)
        if type(self.menu_object) is Combo:
            formatted_combo = Utl.format_string(row, " + ", 1, 6)
            cals = round(float(row[7]), 2)
            price = round(float(row[8]), 2)
        order = Order(
            id_order=self.last_id() + 1,
            description=formatted_combo,
            cals=cals,
            price=price
        )
        self.client.order.append(order)


class OrderDialog(Qtw.QDialog):
    def __init__(self, db_conn, client):
        super().__init__()
        self.client = client
        self.order_count = self.get_last_id()
        self.db_conn = db_conn
        self.healthy_menu = hm.HealthyMenu(db_conn)
        self.healthy_menu_dialog = ghm.HealthyMenuDialog(self.healthy_menu, self.client)

        # Add a title
        self.setWindowTitle(f"Orden de {client.name}")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Add Layout
        self.add_order_lyt = Qtw.QHBoxLayout()
        self.add_order_lbl = Qtw.QLabel("Añadir Orden:")
        self.healthy_menu_btn = Qtw.QPushButton("Menú Saludable")
        self.healthy_menu_btn.clicked.connect(lambda: self.open_dialog(self.healthy_menu_dialog))
        self.select_plate_btn = Qtw.QPushButton("Menú de Platos")
        self.select_plate_btn.clicked.connect(lambda: self.open_dialog(self.select_plate))
        self.select_combo_btn = Qtw.QPushButton("Menú de Combos")
        self.select_combo_btn.clicked.connect(lambda: self.open_dialog(self.select_combo))
        self.add_order_lyt.addWidget(self.add_order_lbl)
        self.add_order_lyt.addWidget(self.healthy_menu_btn)
        self.add_order_lyt.addWidget(self.select_plate_btn)
        self.add_order_lyt.addWidget(self.select_combo_btn)

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
        self.delete_order_btn.clicked.connect(self.full_delete)

        self.select_plate = OrderSelectDialog(self.db_conn, "Platos", self.client, Plate(), self.get_last_id)
        self.select_combo = OrderSelectDialog(self.db_conn, "Combo", self.client, Combo(), self.get_last_id)

        self.load_data_table()

        self.main_lyt.addLayout(self.add_order_lyt)
        self.main_lyt.addWidget(self.data_tbl)
        self.main_lyt.addWidget(self.delete_order_btn)
        self.setLayout(self.main_lyt)

    def get_order(self):
        try:
            selected_row = self.data_tbl.currentRow()
            item = self.data_tbl.item(selected_row, 0)
            id_order = item.text()
            for order in self.client.order:
                if int(order.id_order) == int(id_order):
                    return order
        except Exception as e:
            print(f"Error: {e}")

    def delete_order(self, order):
        try:
            if order in self.client.order:
                self.client.order.remove(order)
                print(f"Order with ID {order.id_order} deleted.")
            else:
                print("No matching order found for deletion.")
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
            selected_row = self.data_tbl.currentRow()
            order = self.get_order()
            self.delete_order(order)
            self.delete_row(selected_row)
            self.calculate_total_price()
        except Exception as e:
            print(f"Error: {e}")

    def load_data_table(self):
        self.data_tbl.setRowCount(0)

        data = [[str(order.id_order), order.description, str(order.cals), str(order.price)] for order in
                self.client.order]

        for row_index, row_data in enumerate(data):
            self.data_tbl.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = Qtw.QTableWidgetItem(col_data)
                self.data_tbl.setItem(row_index, col_index, item)

        self.data_tbl.resizeColumnsToContents()

    def calculate_total_price(self):
        try:
            self.client.bill = sum(order.price for order in self.client.order)
            print(self.client.bill)
        except Exception as e:
            print(f"Error: {e}")

    def open_dialog(self, dialog):
        Utl.open_dialog(dialog)
        self.calculate_total_price()
        self.load_data_table()

    def get_last_id(self):
        try:
            if len(self.client.order) > 0:
                return self.client.order[-1].id_order
            else:
                return 0
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Este código se ejecutará solo cuando gui_table.py se ejecute como script
    cliente = clnt.Client(1, "Luis")
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    dbconn = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    ventana = OrderDialog(dbconn, cliente)
    ventana.show()
    sys.exit(app.exec_())

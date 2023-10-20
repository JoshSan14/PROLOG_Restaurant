import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
from Menu_Prolog.entities import table as tbl
import client_gui as cgui


class TableWindow(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Set an empty list to add tables
        self.table_count = 0
        self.table_list = []

        # Add a title
        self.setWindowTitle("Mesas")
        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Set table
        self.col_hdr = ["ID Mesa", "Nº Clientes", "Total"]
        self.table = Qtw.QTableWidget(0, len(self.col_hdr))
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(self.col_hdr)
        self.table.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Set btns
        self.btn_lyt = Qtw.QHBoxLayout()
        self.add_table_btn = Qtw.QPushButton("Agregar")
        self.add_table_btn.clicked.connect(self.add_row)
        self.edit_table_btn = Qtw.QPushButton("Administar")
        self.edit_table_btn.clicked.connect(self.edit_clients)
        self.delete_table_btn = Qtw.QPushButton("Eliminar")
        self.delete_table_btn.clicked.connect(self.full_delete)
        self.btn_lyt.addWidget(self.add_table_btn)
        self.btn_lyt.addWidget(self.edit_table_btn)
        self.btn_lyt.addWidget(self.delete_table_btn)

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

    def get_table(self):
        try:
            selected_row = self.get_selected_row()
            item = self.table.item(selected_row, 0)
            id_table = item.text()
            for table in self.table_list:
                if int(table.id_table) == int(id_table):
                    return table
        except Exception as e:
            print(f"Error: {e} 1")

    def delete_table(self, d_table):
        try:
            if d_table in self.table_list:
                self.table_list.remove(d_table)
                print(f"Table with ID {d_table.id_table} deleted.")
            else:
                print(f"No matching table found for deletion.")
        except Exception as e:
            print(f"Error: {e} 2")

    def delete_row(self, selected_row):
        try:
            self.table.removeRow(selected_row)
            print(f"Row {selected_row} deleted.")
        except Exception as e:
            print(f"Error: {e} 3")

    def full_delete(self):
        try:
            selected_row = self.get_selected_row()
            table = self.get_table()
            self.delete_table(table)
            self.delete_row(selected_row)
        except Exception as e:
            print(f"Error: {e} 4")

    def add_row(self):
        # Abrir espacio en la tabla
        rows = self.table.rowCount()
        self.table.setRowCount(rows + 1)

        # Crear instancia
        new_table = tbl.Table(self.table_count + 1)
        self.table_list.append(new_table)
        self.table_count += 1

        for col, value in enumerate([new_table.id_table, len(new_table.clients), new_table.total_bill]):
            item = Qtw.QTableWidgetItem(str(value))
            self.table.setItem(self.table.rowCount() - 1, col, item)

    def update_table(self):
        try:
            for row, table in enumerate(self.table_list):
                for col, value in enumerate([table.id_table, len(table.clients), table.total_bill]):
                    item = Qtw.QTableWidgetItem(str(value))
                    self.table.setItem(row, col, item)
        except Exception as e:
            print(f"Error: {e} 5")

    def edit_clients(self):
        try:
            table = self.get_table()
            client_window = cgui.ClientWindow(table)
            client_window.setModal(True)
            client_window.exec_()
            self.update_table()
        except Exception as e:
            print(f"Error: {e} 6")



if __name__ == "__main__":
    # Este código se ejecutará solo cuando table_gui.py se ejecute como script

    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    ventana = TableWindow()
    sys.exit(app.exec_())

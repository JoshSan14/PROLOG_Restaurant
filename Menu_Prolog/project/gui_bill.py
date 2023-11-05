import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
import table as tbl
import gui_client as cgui
from utils import Utils as Utl
from db_conn import *
import client as cl


class PaymentWindow(Qtw.QDialog):
    def __init__(self, db_conn, rest_table):
        super().__init__()
        self.db_conn = db_conn
        self.rest_table = rest_table

        # Add a title
        self.setWindowTitle(f"Factura Mesa: {rest_table.id_table}")
        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Set table
        self.col_hdr = ["Cliente", "Orden", "Total + IVA($)"]
        self.data_tbl = Qtw.QTableWidget(0, len(self.col_hdr))
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalHeaderLabels(self.col_hdr)
        self.data_tbl.setEditTriggers(Qtw.QAbstractItemView.NoEditTriggers)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.total_lyt = Qtw.QHBoxLayout()
        self.total_lbl = Qtw.QLabel(f"Total de Factura: {self.rest_table.total_bill}")
        self.total_lyt.addWidget(self.total_lbl)

        self.payment_lyt = Qtw.QHBoxLayout()
        self.payment_lbl = Qtw.QLabel("Tipo de Pago:")
        self.payment_btn_group = Qtw.QButtonGroup()
        self.payment_btn_cash = Qtw.QRadioButton("Efectivo")
        self.payment_btn_group.addButton(self.payment_btn_cash)
        self.payment_btn_cash.setChecked(True)
        self.payment_btn_card = Qtw.QRadioButton("Tarjeta")
        self.payment_btn_group.addButton(self.payment_btn_card)
        self.payment_lyt.addWidget(self.payment_lbl)
        self.payment_lyt.addWidget(self.payment_btn_cash)
        self.payment_lyt.addWidget(self.payment_btn_card)

        self.btn_lyt = Qtw.QHBoxLayout()
        self.btn_pay_sep = Qtw.QPushButton("Pagar por separado")
        self.btn_lyt.addWidget(self.btn_pay_sep)
        self.btn_pay_total = Qtw.QPushButton("Pagar total")
        self.btn_lyt.addWidget(self.btn_pay_total)

        self.main_lyt.addWidget(self.data_tbl)
        self.main_lyt.addLayout(self.total_lyt)
        self.main_lyt.addLayout(self.payment_lyt)
        self.main_lyt.addLayout(self.btn_lyt)
        self.setLayout(self.main_lyt)

        Utl.add_data_to_table(self.data_tbl, self.rest_table.generate_client_records())


        self.show()


if __name__ == "__main__":
    dbconn = DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    table = tbl.Table(1)
    table.clients = [
        cl.Client(1, "Alice"),
        cl.Client(2, "Bob"),
    ]
    table.clients[1].order = ["papas + refresco", "pan"]
    print(table.clients[1].get_formatted_orders())
    table.clients[1].bill = 300
    app = Qtw.QApplication(sys.argv)  # Crear una aplicación de PyQt
    pw = PaymentWindow(dbconn, table)
    sys.exit(app.exec_())

import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from crud_utils import Utils as Utl
from factory_ingredient import DrinkFactory as Drf
from ingredient import Drink as Dr
from gui_crud_ingredient import IngredientCRUD


class DrinkCRUD(IngredientCRUD):
    def __init__(self, db_conn):
        super().__init__(db_conn, drink)

        self.drink = Dr()

        # Add a title
        self.setWindowTitle("Bebidas")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Category
        self.cat_lyt = Qtw.QVBoxLayout()
        self.cat_lbl = Qtw.QLabel("Categoría")
        self.cat_lyt.addWidget(self.cat_lbl)
        self.cat_lbl.setAlignment(Qt.AlignCenter)
        self.cat_cbox = Qtw.QComboBox()
        self.cat_cbox.addItems(self.drink.cat_opts)
        self.cat_lyt.addWidget(self.cat_cbox)

        # Temp
        self.temp_lyt = Qtw.QVBoxLayout()
        self.temp_lbl = Qtw.QLabel("Temperatura")
        self.temp_lyt.addWidget(self.temp_lbl)
        self.temp_lbl.setAlignment(Qt.AlignCenter)
        self.temp_cbox = Qtw.QComboBox()
        self.temp_cbox.addItems(self.drink.temp_opts)
        self.temp_lyt.addWidget(self.temp_cbox)

        # Base
        self.base_lyt = Qtw.QVBoxLayout()
        self.base_lbl = Qtw.QLabel("Base")
        self.base_lyt.addWidget(self.base_lbl)
        self.base_lbl.setAlignment(Qt.AlignCenter)
        self.base_cbox = Qtw.QComboBox()
        self.base_cbox.addItems(self.drink.base_opts)
        self.base_lyt.addWidget(self.base_cbox)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(self.drink.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(self.drink.col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()
        self.data_tbl.cellClicked.connect(self.upload_object)

        self.line1_lyt = Qtw.QHBoxLayout()
        self.line1_lyt.addLayout(self.diet_nat_lyt)
        self.line1_lyt.addLayout(self.time_lyt)

        self.line2_lyt = Qtw.QHBoxLayout()
        self.line2_lyt.addLayout(self.fla_lyt)
        self.line2_lyt.addLayout(self.cat_lyt)
        self.line2_lyt.addLayout(self.temp_lyt)
        self.line2_lyt.addLayout(self.base_lyt)

        self.line3_lyt = Qtw.QHBoxLayout()
        self.line3_lyt.addLayout(self.cal_lyt)
        self.line3_lyt.addLayout(self.pri_lyt)

        self.main_lyt.addLayout(self.name_lyt)
        self.main_lyt.addLayout(self.line1_lyt)
        self.main_lyt.addLayout(self.line2_lyt)
        self.main_lyt.addLayout(self.line3_lyt)
        self.main_lyt.addLayout(self.btn_lyt)
        self.main_lyt.addWidget(self.data_tbl)
        self.setLayout(self.main_lyt)

        self.load_recs()

        self.show()

    def locate_rec(self, record):
        try:
            self.name_tbox.setText(record[1])
            Utl.set_combobox_value(self.diet_nat_cbox, record[2])
            Utl.set_checkbox_state(self.br_chbox, record[3])
            Utl.set_checkbox_state(self.lu_chbox, record[4])
            Utl.set_checkbox_state(self.di_chbox, record[5])
            Utl.set_combobox_value(self.fla_cbox, record[6])
            Utl.set_combobox_value(self.cat_cbox, record[7])
            Utl.set_combobox_value(self.temp_cbox, record[8])
            Utl.set_combobox_value(self.base_cbox, record[9])
            self.cal_tbox.setText(str(record[10]))
            self.pri_tbox.setText(str(record[11]))
        except Exception as e:
            print(f"Error reading record: {e}")

    def upload_object(self):
        try:
            record = Utl.get_single_record(self.db_conn, self.drink.table_name, self.data_tbl, self.drink.col_ord)
            self.drink = Drf.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[10],
                                               diet_nat=record[2],
                                               flavor=record[6], price=record[11], breakfast=record[3], lunch=record[4],
                                               dinner=record[5], category=record[7], temperature=record[8],
                                               base=record[9])
            self.locate_rec(record)
        except Exception as e:
            print(f"Error in input: {e}")

    def download_object(self):
        try:
            self.drink.name = self.name_tbox.text().capitalize()
            self.drink.cals = float(self.cal_tbox.text())
            self.drink.diet_nat = self.diet_nat_cbox.currentText()
            self.drink.flavor = self.fla_cbox.currentText()
            self.drink.price = float(self.pri_tbox.text())
            self.drink.breakfast = Utl.word_to_boolean(str(self.br_chbox.isChecked()))
            self.drink.lunch = Utl.word_to_boolean(str(self.lu_chbox.isChecked()))
            self.drink.dinner = Utl.word_to_boolean(str(self.di_chbox.isChecked()))
            self.drink.category = self.cat_cbox.currentText()
            self.drink.temperature = self.temp_cbox.currentText()
            self.drink.base = self.base_cbox.currentText()
        except Exception as e:
            print(f"Error in input: {e}")

    def clean_inputs(self):
        self.name_tbox.clear()
        self.cal_tbox.clear()
        self.pri_tbox.clear()

        self.diet_nat_cbox.setCurrentIndex(0)
        self.fla_cbox.setCurrentIndex(0)
        self.cat_cbox.setCurrentIndex(0)
        self.temp_cbox.setCurrentIndex(0)
        self.base_cbox.setCurrentIndex(0)

        self.br_chbox.setChecked(False)
        self.lu_chbox.setChecked(False)
        self.di_chbox.setChecked(False)

        self.drink = Dr()

    def insert_rec(self):
        try:
            self.download_object()
            Utl.insert_values(self.db_conn, self.drink.table_name, self.drink.to_dict())
            self.load_recs()
            self.clean_inputs()
        except Exception as e:
            print(f"Error inserting record: {e}")

    def load_recs(self):
        Utl.load_values(self.db_conn, self.drink.table_name, self.drink.col_ord, self.data_tbl)

    def update_rec(self):
        try:
            if self.drink.id_object > 0:
                self.download_object()
                Utl.update_values(self.db_conn, self.drink.table_name, self.drink.id_column,
                                  self.drink.id_object, self.drink.to_dict())
                self.load_recs()
        except Exception as e:
            print(f"Error in update: {e}")

    def delete_rec(self):
        try:
            Utl.delete_values(self.db_conn, self.drink.table_name, self.data_tbl)
            self.load_recs()
        except Exception as e:
            print(f"Error deleting record: {e}")


if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    drink = Dr()
    mw = DrinkCRUD(db)

    # Run the application
    sys.exit(app.exec_())

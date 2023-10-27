import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from crud_utils import Utils as Utl
from factory_ingredient import ProteinFactory as Prf
from ingredient import Protein as Pr
from gui_crud_ingredient import IngredientCRUD


class ProteinCRUD(IngredientCRUD):
    def __init__(self, db_conn):
        super().__init__(db_conn, protein)

        self.protein = Pr()

        # Add a title
        self.setWindowTitle("Proteína")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Origin
        self.ori_lyt = Qtw.QVBoxLayout()
        self.ori_lbl = Qtw.QLabel("Origen")
        self.ori_lyt.addWidget(self.ori_lbl)
        self.ori_lbl.setAlignment(Qt.AlignCenter)
        self.ori_cbox = Qtw.QComboBox()
        self.ori_cbox.addItems(self.protein.ori_opts)
        self.ori_lyt.addWidget(self.ori_cbox)

        # Temp
        self.tex_lyt = Qtw.QVBoxLayout()
        self.tex_lbl = Qtw.QLabel("Textura")
        self.tex_lyt.addWidget(self.tex_lbl)
        self.tex_lbl.setAlignment(Qt.AlignCenter)
        self.tex_cbox = Qtw.QComboBox()
        self.tex_cbox.addItems(self.protein.tex_opts)
        self.tex_lyt.addWidget(self.tex_cbox)

        # Base
        self.cook_met_lyt = Qtw.QVBoxLayout()
        self.cook_met_lbl = Qtw.QLabel("Método de Cocción")
        self.cook_met_lyt.addWidget(self.cook_met_lbl)
        self.cook_met_lbl.setAlignment(Qt.AlignCenter)
        self.cook_met_cbox = Qtw.QComboBox()
        self.cook_met_cbox.addItems(self.protein.cook_met_opts)
        self.cook_met_lyt.addWidget(self.cook_met_cbox)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(self.protein.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(self.protein.col_hdr)
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
        self.line2_lyt.addLayout(self.ori_lyt)
        self.line2_lyt.addLayout(self.tex_lyt)
        self.line2_lyt.addLayout(self.cook_met_lyt)

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
            Utl.set_combobox_value(self.ori_cbox, record[7])
            Utl.set_combobox_value(self.tex_cbox, record[8])
            Utl.set_combobox_value(self.cook_met_cbox, record[9])
            self.cal_tbox.setText(str(record[10]))
            self.pri_tbox.setText(str(record[11]))
        except Exception as e:
            print(f"Error reading record: {e}")

    def upload_object(self):
        try:
            record = Utl.get_single_record(self.db_conn, self.protein.table_name, self.data_tbl, self.protein.col_ord)
            self.protein = Prf.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[10],
                                                 diet_nat=record[2], flavor=record[6], price=record[11],
                                                 breakfast=record[3], lunch=record[4], dinner=record[5],
                                                 origin=record[7], texture=record[8], cook_met=record[9])
            self.locate_rec(record)
        except Exception as e:
            print(f"Error in input: {e}")

    def download_object(self):
        try:
            self.protein.name = self.name_tbox.text().capitalize()
            self.protein.cals = float(self.cal_tbox.text())
            self.protein.diet_nat = self.diet_nat_cbox.currentText()
            self.protein.flavor = self.fla_cbox.currentText()
            self.protein.price = float(self.pri_tbox.text())
            self.protein.breakfast = Utl.word_to_boolean(str(self.br_chbox.isChecked()))
            self.protein.lunch = Utl.word_to_boolean(str(self.lu_chbox.isChecked()))
            self.protein.dinner = Utl.word_to_boolean(str(self.di_chbox.isChecked()))
            self.protein.origin = self.ori_cbox.currentText()
            self.protein.texture = self.tex_cbox.currentText()
            self.protein.cook_met = self.cook_met_cbox.currentText()
        except Exception as e:
            print(f"Error in input: {e}")

    def clean_inputs(self):
        self.name_tbox.clear()
        self.cal_tbox.clear()
        self.pri_tbox.clear()

        self.diet_nat_cbox.setCurrentIndex(0)
        self.fla_cbox.setCurrentIndex(0)
        self.ori_cbox.setCurrentIndex(0)
        self.tex_cbox.setCurrentIndex(0)
        self.cook_met_cbox.setCurrentIndex(0)

        self.br_chbox.setChecked(False)
        self.lu_chbox.setChecked(False)
        self.di_chbox.setChecked(False)

        self.protein = Pr()

    def insert_rec(self):
        try:
            self.download_object()
            Utl.insert_values(self.db_conn, self.protein.table_name, self.protein.to_dict())
            self.load_recs()
            self.clean_inputs()
        except Exception as e:
            print(f"Error inserting record: {e}")

    def load_recs(self):
        Utl.load_values(self.db_conn, self.protein.table_name, self.protein.col_ord, self.data_tbl)

    def update_rec(self):
        try:
            if self.protein.id_object > 0:
                self.download_object()
                Utl.update_values(self.db_conn, self.protein.table_name, self.protein.id_column,
                                  self.protein.id_object, self.protein.to_dict())
                self.load_recs()
        except Exception as e:
            print(f"Error in update: {e}")

    def delete_rec(self):
        try:
            Utl.delete_values(self.db_conn, self.protein.table_name, self.data_tbl)
            self.load_recs()
        except Exception as e:
            print(f"Error deleting record: {e}")


if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    protein = Pr()
    mw = ProteinCRUD(db)

    # Run the application
    sys.exit(app.exec_())

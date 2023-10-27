import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from crud_utils import Utils as Utl
from ingredient_factory import ProteinFactory as Prf
from plate import Plate as Plt


class IngredientSelectLayout(Qtw.QVBoxLayout):
    def __init__(self, name):
        super().__init__()
        self.lbl = Qtw.QLabel(name)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.addWidget(self.lbl)
        self.tbox = Qtw.QLineEdit()
        self.tbox.setEnabled(False)
        self.addWidget(self.tbox)
        self.btn = Qtw.QPushButton(f"Seleccionar {name}")
        # self.btn.clicked.connect()
        self.addWidget(self.btn)


class IngredientSelectDialog(Qtw.QDialog):
    def __init__(self, title, ingredient, col_hdr):
        super().__init__()

        # Add a title
        self.setWindowTitle(f"Seleccionar {title}")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        self.setFixedWidth(750)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()

        self.main_lyt.addWidget(self.data_tbl)

        self.setLayout(self.main_lyt)

        self.show()


class PlateCRUD(Qtw.QDialog):
    def __init__(self, db_conn):
        super().__init__()

        self.col_hdr = []

        self.plate = Plt()

        # Add a title
        self.setWindowTitle("Platos")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Name Layout
        self.name_lyt = Qtw.QHBoxLayout()
        self.name_lbl = Qtw.QLabel("Nombre:")
        self.name_lbl.setAlignment(Qt.AlignCenter)
        self.name_lyt.addWidget(self.name_lbl)
        self.name_tbox = Qtw.QLineEdit()
        self.name_lyt.addWidget(self.name_tbox)

        # Protein Layout
        self.pro_lyt = IngredientSelectLayout("Proteína")

        # Garrison 1 Layout
        self.gar1_lyt = IngredientSelectLayout("Guarnición 1")

        # Garrison 2 Layout
        self.gar2_lyt = IngredientSelectLayout("Guarnición 2")

        # Garrison 3 Layout
        self.gar3_lyt = IngredientSelectLayout("Guarnición 3")

        # Buttons
        self.btn_lyt = Qtw.QHBoxLayout()
        self.clean_btn = Qtw.QPushButton("Limpiar")
        # self.clean_btn.clicked.connect(self.clean_inputs)
        self.btn_lyt.addWidget(self.clean_btn)
        self.add_btn = Qtw.QPushButton("Añadir")
        # self.add_btn.clicked.connect(self.insert_rec)
        self.btn_lyt.addWidget(self.add_btn)
        self.update_btn = Qtw.QPushButton("Actualizar")
        # self.update_btn.clicked.connect(self.update_rec)
        self.btn_lyt.addWidget(self.update_btn)
        self.delete_btn = Qtw.QPushButton("Borrar")
        # self.delete_btn.clicked.connect(self.delete_rec)
        self.btn_lyt.addWidget(self.delete_btn)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(self.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(self.col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()
        # self.data_tbl.cellClicked.connect(self.upload_object)

        self.ingredient_lyt = Qtw.QHBoxLayout()
        self.ingredient_lyt.addLayout(self.pro_lyt)
        self.ingredient_lyt.addLayout(self.gar1_lyt)
        self.ingredient_lyt.addLayout(self.gar2_lyt)
        self.ingredient_lyt.addLayout(self.gar3_lyt)

        self.main_lyt.addLayout(self.name_lyt)
        self.main_lyt.addLayout(self.ingredient_lyt)
        self.main_lyt.addLayout(self.btn_lyt)
        self.main_lyt.addWidget(self.data_tbl)

        self.setLayout(self.main_lyt)

        self.show()


if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    mw = PlateCRUD(db)
    mm = IngredientSelectDialog("Title", "ingredient", [])

    # Run the application
    sys.exit(app.exec_())

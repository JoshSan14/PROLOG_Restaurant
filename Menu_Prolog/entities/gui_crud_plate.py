import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from crud_utils import Utils as Utl
from factory_ingredient import ProteinFactory as Prf
from regular_menu import Plate as Plt
from ingredient import *
from factory_ingredient import *


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
        self.addWidget(self.btn)


class IngredientSelectDialog(Qtw.QDialog):
    def __init__(self, title, db_conn, ingredient, callback_function):
        super().__init__()

        self.title = title
        self.db_conn = db_conn
        self.ingredient = ingredient
        self.callback_function = callback_function

        # Add a title
        self.setWindowTitle(f"Seleccionar {title}")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        self.setFixedWidth(550)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(ingredient.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(ingredient.col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()
        self.data_tbl.itemClicked.connect(self.select_value)

        self.main_lyt.addWidget(self.data_tbl)

        self.setLayout(self.main_lyt)

        Utl.load_values(self.db_conn, self.ingredient.table_name, self.ingredient.col_ord, self.data_tbl)

    def select_value(self):
        record = Utl.get_single_record(self.db_conn, self.ingredient.table_name, self.data_tbl, self.ingredient.col_ord)
        if isinstance(self.ingredient, Drink):
            self.ingredient = DrinkFactory.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[10],
                                                             diet_nat=record[2], flavor=record[6], price=record[11],
                                                             breakfast=record[3], lunch=record[4], dinner=record[5],
                                                             category=record[7], temperature=record[8], base=record[9])
        if isinstance(self.ingredient, Protein):
            self.ingredient = ProteinFactory.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[10],
                                                               diet_nat=record[2], flavor=record[6], price=record[11],
                                                               breakfast=record[3], lunch=record[4], dinner=record[5],
                                                               origin=record[7], texture=record[8], cook_met=record[9])
        if isinstance(self.ingredient, Garrison):
            self.ingredient = GarrisonFactory.create_ingredient(id_ingredient=record[0], name=record[1],
                                                                cals=record[10], diet_nat=record[2], flavor=record[6],
                                                                price=record[11], breakfast=record[3], lunch=record[4],
                                                                dinner=record[5], category=record[7], size=record[8],
                                                                cook_met=record[9])
        if isinstance(self.ingredient, Dessert):
            self.ingredient = DessertFactory.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[9],
                                                               diet_nat=record[2], flavor=record[6], price=record[10],
                                                               breakfast=record[3], lunch=record[4], dinner=record[5],
                                                               texture=record[7], temperature=record[8])
        self.callback_function(self.ingredient)


class PlateCRUD(Qtw.QDialog):
    def __init__(self, db_conn):
        super().__init__()

        # Database Connection:
        self.db_conn = db_conn

        # Ingredients:
        self.protein = Protein()
        self.garrison1 = Garrison()
        self.garrison2 = Garrison()
        self.garrison3 = Garrison()

        # Select Dialogs
        self.pro_dial = IngredientSelectDialog("Proteína", self.db_conn, self.protein, self.update_ingredient)
        self.gar1_dial = IngredientSelectDialog("Guarnición 1", self.db_conn, self.garrison1, self.update_ingredient)
        self.gar2_dial = IngredientSelectDialog("Guarnición 2", self.db_conn, self.garrison2, self.update_ingredient)
        self.gar3_dial = IngredientSelectDialog("Guarnición 3", self.db_conn, self.garrison3, self.update_ingredient)

        # Plate
        self.plate = Plt()

        self.col_hdr = []

        # Add a title
        self.setWindowTitle("Platos")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Protein Layout
        self.pro_lyt = IngredientSelectLayout("Proteína")
        self.pro_lyt.btn.clicked.connect(lambda: self.open_select_dialog(self.pro_dial))

        # Garrison 1 Layout
        self.gar1_lyt = IngredientSelectLayout("Guarnición 1")
        self.gar1_lyt.btn.clicked.connect(lambda: self.open_select_dialog(self.gar1_dial))

        # Garrison 2 Layout
        self.gar2_lyt = IngredientSelectLayout("Guarnición 2")
        self.gar2_lyt.btn.clicked.connect(lambda: self.open_select_dialog(self.gar2_dial))

        # Garrison 3 Layout
        self.gar3_lyt = IngredientSelectLayout("Guarnición 3")
        self.gar3_lyt.btn.clicked.connect(lambda: self.open_select_dialog(self.gar3_dial))

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

        self.main_lyt.addLayout(self.ingredient_lyt)
        self.main_lyt.addLayout(self.btn_lyt)
        self.main_lyt.addWidget(self.data_tbl)

        self.setLayout(self.main_lyt)

        self.show()

    def update_ingredient(self, ingredient):
        if isinstance(ingredient, Protein):
            self.protein = ingredient
        elif isinstance(ingredient, Garrison):
            self.garrison1 = ingredient
        elif isinstance(ingredient, Garrison):
            self.garrison2 = ingredient
        elif isinstance(ingredient, Garrison):
            self.garrison3 = ingredient
        self.update_plate_values()

    def update_plate_values(self):
        self.plate.id_protein = self.protein.id_object
        self.plate.id_garrison1 = self.garrison1.id_object
        self.plate.id_garrison2 = self.garrison2.id_object
        self.plate.id_garrison3 = self.garrison3.id_object
        self.plate.cals = self.protein.cals + self.garrison1.cals + self.garrison2.cals + self.garrison3.cals
        self.plate.price = self.protein.price + self.garrison1.price + self.garrison2.price + self.garrison3.price

    def open_select_dialog(self, dialog):
        Utl.open_dialog(dialog)
        print(self.plate.id_protein)



if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    mw = PlateCRUD(db)
    dr = Drink()

    # Run the application
    sys.exit(app.exec_())

import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from utils import Utils as Utl
from factory_ingredient import ProteinFactory as Prf
from factory_ingredient import GarrisonFactory as Gaf
from regular_menu import Plate as Plt
from ingredient import *
from factory_menu import MenuFactory as Mf
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


class NumLayout(Qtw.QVBoxLayout):
    def __init__(self, name):
        super().__init__()

        self.lbl = Qtw.QLabel(name)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.addWidget(self.lbl)
        self.tbox = Qtw.QLineEdit()
        self.tbox.setText("0")
        self.tbox.setEnabled(False)
        self.addWidget(self.tbox)


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
        self.pro_dial = IngredientSelectDialog("Proteína", self.db_conn, self.protein, self.update_selected_protein)
        self.gar1_dial = IngredientSelectDialog("Guarnición 1", self.db_conn, self.garrison1,
                                                self.update_selected_garrison1)
        self.gar2_dial = IngredientSelectDialog("Guarnición 2", self.db_conn, self.garrison2,
                                                self.update_selected_garrison2)
        self.gar3_dial = IngredientSelectDialog("Guarnición 3", self.db_conn, self.garrison3,
                                                self.update_selected_garrison3)

        # Menu Item
        self.menu_item = Plt()

        # Add a title
        self.setWindowTitle("Platos")

        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Protein Layout
        self.pro_lyt = IngredientSelectLayout("Proteína")
        self.pro_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.pro_dial))

        # Garrison 1 Layout
        self.gar1_lyt = IngredientSelectLayout("Guarnición 1")
        self.gar1_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.gar1_dial))

        # Garrison 2 Layout
        self.gar2_lyt = IngredientSelectLayout("Guarnición 2")
        self.gar2_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.gar2_dial))

        # Garrison 3 Layout
        self.gar3_lyt = IngredientSelectLayout("Guarnición 3")
        self.gar3_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.gar3_dial))

        # Calorie Layout
        self.cals_lyt = NumLayout("Calorias (Kcal)")
        self.price_lyt = NumLayout("Price ($)")

        # Buttons
        self.btn_lyt = Qtw.QHBoxLayout()
        self.clean_btn = Qtw.QPushButton("Limpiar")
        self.clean_btn.clicked.connect(self.clean_values)
        self.btn_lyt.addWidget(self.clean_btn)
        self.add_btn = Qtw.QPushButton("Añadir")
        self.add_btn.clicked.connect(self.post_menu_item)
        self.btn_lyt.addWidget(self.add_btn)
        self.update_btn = Qtw.QPushButton("Actualizar")
        self.update_btn.clicked.connect(self.update_menu_item_db)
        self.btn_lyt.addWidget(self.update_btn)
        self.delete_btn = Qtw.QPushButton("Borrar")
        self.delete_btn.clicked.connect(self.delete_menu_item_db)
        self.btn_lyt.addWidget(self.delete_btn)

        # Data Table
        self.data_tbl = Qtw.QTableWidget(0, len(self.menu_item.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(self.menu_item.col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()
        self.data_tbl.cellClicked.connect(self.upload_plate)

        self.ingredient_lyt = Qtw.QHBoxLayout()
        self.ingredient_lyt.addLayout(self.pro_lyt)
        self.ingredient_lyt.addLayout(self.gar1_lyt)
        self.ingredient_lyt.addLayout(self.gar2_lyt)
        self.ingredient_lyt.addLayout(self.gar3_lyt)

        self.num_lyt = Qtw.QHBoxLayout()
        self.num_lyt.addLayout(self.cals_lyt)
        self.num_lyt.addLayout(self.price_lyt)

        self.main_lyt.addLayout(self.ingredient_lyt)
        self.main_lyt.addLayout(self.num_lyt)
        self.main_lyt.addLayout(self.btn_lyt)
        self.main_lyt.addWidget(self.data_tbl)

        self.setLayout(self.main_lyt)

        self.load_values_in_data_table()

    def update_selected_protein(self, protein):
        if isinstance(protein, Protein):
            self.protein = protein
            self.update_menu_values()
            self.pro_lyt.tbox.setText(self.protein.name)

    def update_selected_garrison1(self, garrison):
        if isinstance(garrison, Garrison):
            self.garrison1 = garrison
            self.update_menu_values()
            self.gar1_lyt.tbox.setText(self.garrison1.name)

    def update_selected_garrison2(self, garrison):
        if isinstance(garrison, Garrison):
            self.garrison2 = garrison
            self.update_menu_values()
            self.gar2_lyt.tbox.setText(self.garrison2.name)

    def update_selected_garrison3(self, garrison):
        if isinstance(garrison, Garrison):
            self.garrison3 = garrison
            self.update_menu_values()
            self.gar3_lyt.tbox.setText(self.garrison3.name)

    def update_menu_values(self):
        self.menu_item.id_protein = self.protein.id_object
        self.menu_item.id_garrison1 = self.garrison1.id_object
        self.menu_item.id_garrison2 = self.garrison2.id_object
        self.menu_item.id_garrison3 = self.garrison3.id_object
        self.menu_item.cals = round((self.protein.cals + self.garrison1.cals + self.garrison2.cals + self.garrison3.cals),
                                    2)
        self.menu_item.price = round(
            (self.protein.price + self.garrison1.price + self.garrison2.price + self.garrison3.price), 2)
        self.cals_lyt.tbox.setText(str(self.menu_item.cals))
        self.price_lyt.tbox.setText(str(self.menu_item.price))

    def load_values_in_data_table(self):
        try:
            records = self.menu_item.get_all_db_menu(self.db_conn)
            Utl.add_data_to_table(self.data_tbl, records)
        except Exception as e:
            print(f"Error getting records: {e}")

    def locate_rec(self, record):
        try:
            self.pro_lyt.tbox.setText(record[1])
            self.gar1_lyt.tbox.setText(record[2])
            self.gar2_lyt.tbox.setText(record[3])
            self.gar3_lyt.tbox.setText(record[4])
            self.cals_lyt.tbox.setText(str(record[5]))
            self.price_lyt.tbox.setText(str(record[6]))
        except Exception as e:
            print(f"Error reading record: {e}")

    def protein_query(self, id_menu, id_protein):
        column_order = ", ".join([f"P.{col}" for col in Protein().col_ord])
        sql_query = f"""
            SELECT {column_order}
            FROM ingrediente.proteina AS P
            JOIN menu.plato AS MP ON MP.proteina = P.id
            WHERE MP.id = {id_menu};
        """
        try:
            record = self.db_conn.execute_custom_query(sql_query, (id_protein,))[0]
            if record:
                protein = Prf.create_ingredient(
                    id_ingredient=record[0], name=record[1], cals=record[10], diet_nat=record[2],
                    flavor=record[6], price=record[11], breakfast=record[3], lunch=record[4],
                    dinner=record[5], origin=record[7], texture=record[8], cook_met=record[9]
                )
                return protein
        except Exception as e:
            print(f"Error executing protein query: {e}")
            return None

    def garrison_query(self, id_menu, id_garrison, num_garrison):
        column_order = ", ".join([f"G.{col}" for col in Garrison().col_ord])
        sql_query = f"""
            SELECT {column_order}
            FROM ingrediente.guarnicion AS G
            JOIN menu.plato AS MP ON MP.guarnicion_{num_garrison} = G.id
            WHERE MP.id = {id_menu};
        """
        try:
            record = self.db_conn.execute_custom_query(sql_query, (id_garrison,))[0]
            if record:
                garrison = Gaf.create_ingredient(
                    id_ingredient=record[0], name=record[1], cals=record[10], diet_nat=record[2], flavor=record[6],
                    price=record[11], breakfast=record[3], lunch=record[4], dinner=record[5], category=record[7],
                    size=record[8], cook_met=record[9]
                )
                return garrison
        except Exception as e:
            print(f"Error executing garrison query: {e}")
            return None

    def upload_plate(self):
        try:
            record = Utl.get_single_record(self.db_conn, self.menu_item.table_name, self.data_tbl, self.menu_item.col_ord)
            self.menu_item.id_menu = record[0]
            self.protein = self.protein_query(self.menu_item.id_menu, record[1])
            self.garrison1 = self.garrison_query(self.menu_item.id_menu, record[2], "1")
            self.garrison2 = self.garrison_query(self.menu_item.id_menu, record[3], "2")
            self.garrison3 = self.garrison_query(self.menu_item.id_menu, record[4], "3")
            self.update_menu_values()
            plate_rec = [self.menu_item.id_menu, self.protein.name, self.garrison1.name, self.garrison2.name,
                         self.garrison3.name, self.menu_item.cals, self.menu_item.price]
            self.locate_rec(plate_rec)
            print(self.menu_item.to_dict())
        except Exception as e:
            print(f"Error in input: {e}")

    def clean_values(self):
        self.protein = Protein()
        self.garrison1 = Garrison()
        self.garrison2 = Garrison()
        self.garrison3 = Garrison()
        self.menu_item.id_menu = 0
        self.update_menu_values()
        record = [self.menu_item.id_menu, self.protein.name, self.garrison1.name, self.garrison2.name, self.garrison3.name,
                  self.menu_item.cals, self.menu_item.price]
        self.locate_rec(record)

    def delete_menu_item_db(self):
        Utl.delete_values(self.db_conn, self.menu_item.table_name, self.data_tbl)
        self.clean_values()
        self.load_values_in_data_table()

    def update_menu_item_db(self):
        Utl.update_values(self.db_conn, self.menu_item.table_name, self.menu_item.id_column, self.menu_item.id_menu,
                          self.menu_item.to_dict())
        self.load_values_in_data_table()

    def post_menu_item(self):
        Utl.insert_values(self.db_conn, self.menu_item.table_name, self.menu_item.to_dict())
        self.load_values_in_data_table()


if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    mw = PlateCRUD(db)
    dr = Drink()
    mw.show()
    # Run the application
    sys.exit(app.exec_())

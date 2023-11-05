import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
import db_conn as dbc
from utils import Utils as Utl
from factory_ingredient import ProteinFactory as Prf
from factory_ingredient import GarrisonFactory as Gaf
from factory_ingredient import DrinkFactory as Drf
from factory_ingredient import DessertFactory as Def
from regular_menu import Combo as Cbo
from ingredient import *
from factory_menu import MenuFactory as Mf
from factory_ingredient import *
from gui_crud_plate import *


class ComboCRUD(PlateCRUD):
    def __init__(self, db_conn):
        super().__init__(db_conn)

        self.main_lyt.removeWidget(self.data_tbl)

        # Ingredients:
        self.drink = Drink()
        self.dessert = Dessert()

        # Select Dialogs
        self.dri_dial = IngredientSelectDialog("Bebida", self.db_conn, self.drink, self.update_selected_drink)
        self.des_dial = IngredientSelectDialog("Postre", self.db_conn, self.dessert,
                                               self.update_selected_dessert)

        # Menu Item
        self.menu_item = Cbo()

        # Add a title
        self.setWindowTitle("Combos")

        # Drink Layout
        self.dri_lyt = IngredientSelectLayout("Bebida")
        self.dri_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.dri_dial))

        # Dessert Layout
        self.des_lyt = IngredientSelectLayout("Postre")
        self.des_lyt.btn.clicked.connect(lambda: Utl.open_dialog(self.des_dial))

        self.ingredient_lyt.addLayout(self.dri_lyt)
        self.ingredient_lyt.addLayout(self.des_lyt)

        print(self.menu_item.col_hdr)

        # Data Table

        self.data_tbl = Qtw.QTableWidget(0, len(self.menu_item.col_hdr))
        self.data_tbl.setHorizontalHeaderLabels(self.menu_item.col_hdr)
        self.data_tbl.verticalHeader().setVisible(False)
        self.data_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.data_tbl.resizeColumnsToContents()
        self.data_tbl.cellClicked.connect(self.upload_plate)

        self.main_lyt.addWidget(self.data_tbl)

        self.load_values_in_data_table()

    def update_selected_drink(self, drink):
        if isinstance(drink, Drink):
            self.drink = drink
            self.update_menu_values()
            self.dri_lyt.tbox.setText(self.drink.name)

    def update_selected_dessert(self, dessert):
        if isinstance(dessert, Dessert):
            self.dessert = dessert
            self.update_menu_values()
            self.des_lyt.tbox.setText(self.dessert.name)

    def update_menu_values(self):
        self.menu_item.id_protein = self.protein.id_object
        self.menu_item.id_garrison1 = self.garrison1.id_object
        self.menu_item.id_garrison2 = self.garrison2.id_object
        self.menu_item.id_garrison3 = self.garrison3.id_object
        self.menu_item.id_drink = self.drink.id_object
        self.menu_item.id_dessert = self.dessert.id_object
        self.menu_item.cals = round((self.protein.cals + self.garrison1.cals + self.garrison2.cals +
                                     self.garrison3.cals + self.drink.cals + self.dessert.cals), 2)
        self.menu_item.price = round((self.protein.price + self.garrison1.price + self.garrison2.price +
                                      self.garrison3.price + self.drink.price + self.dessert.price), 2)
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
            self.dri_lyt.tbox.setText(record[5])
            self.des_lyt.tbox.setText(record[6])
            self.cals_lyt.tbox.setText(str(record[7]))
            self.price_lyt.tbox.setText(str(record[8]))
        except Exception as e:
            print(f"Error reading record: {e}")

    def dessert_query(self, id_menu, id_dessert):
        column_order = ", ".join([f"Po.{col}" for col in Dessert().col_ord])
        sql_query = f"""
            SELECT {column_order}
            FROM ingrediente.postre AS Po
            JOIN menu.combo AS MC ON MC.postre = Po.id
            WHERE MC.id = {id_menu};
        """
        try:
            record = self.db_conn.execute_custom_query(sql_query, (id_dessert,))[0]
            if record:
                dessert = Def.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[9],
                                                diet_nat=record[2], flavor=record[6], price=record[10],
                                                breakfast=record[3], lunch=record[4], dinner=record[5],
                                                texture=record[7], temperature=record[8])
                return dessert
        except Exception as e:
            print(f"Error executing protein query: {e}")
            return None

    def drink_query(self, id_menu, id_drink):
        column_order = ", ".join([f"B.{col}" for col in Drink().col_ord])
        sql_query = f"""
            SELECT {column_order}
            FROM ingrediente.bebida AS B
            JOIN menu.combo AS MC ON MC.bebida = B.id
            WHERE MC.id = {id_menu};
        """
        try:
            record = self.db_conn.execute_custom_query(sql_query, (id_drink,))[0]
            if record:
                drink = Drf.create_ingredient(id_ingredient=record[0], name=record[1], cals=record[10],
                                              diet_nat=record[2], flavor=record[6], price=record[11],
                                              breakfast=record[3], lunch=record[4], dinner=record[5],
                                              category=record[7], temperature=record[8], base=record[9])
                return drink
        except Exception as e:
            print(f"Error executing protein query: {e}")
            return None

    def upload_plate(self):
        try:
            record = Utl.get_single_record(self.db_conn, self.menu_item.table_name, self.data_tbl,
                                           self.menu_item.col_ord)
            self.menu_item.id_menu = record[0]
            self.protein = self.protein_query(self.menu_item.id_menu, record[1])
            self.garrison1 = self.garrison_query(self.menu_item.id_menu, record[2], "1")
            self.garrison2 = self.garrison_query(self.menu_item.id_menu, record[3], "2")
            self.garrison3 = self.garrison_query(self.menu_item.id_menu, record[4], "3")
            self.drink = self.drink_query(self.menu_item.id_menu, record[5])
            self.dessert = self.dessert_query(self.menu_item.id_menu, record[6])
            self.update_menu_values()
            plate_rec = [self.menu_item.id_menu, self.protein.name, self.garrison1.name, self.garrison2.name,
                         self.garrison3.name, self.drink.name, self.dessert.name, self.menu_item.cals,
                         self.menu_item.price]
            self.locate_rec(plate_rec)
            print(self.menu_item.to_dict())
        except Exception as e:
            print(f"Error in input: {e}")

    def clean_values(self):
        self.protein = Protein()
        self.garrison1 = Garrison()
        self.garrison2 = Garrison()
        self.garrison3 = Garrison()
        self.drink = Drink()
        self.dessert = Dessert()
        self.menu_item.id_menu = 0
        self.update_menu_values()
        record = [self.menu_item.id_menu, self.protein.name, self.garrison1.name, self.garrison2.name,
                  self.garrison3.name, self.drink.name, self.dessert.name, self.menu_item.cals, self.menu_item.price]
        self.locate_rec(record)


if __name__ == "__main__":
    db = dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432")
    app = Qtw.QApplication(sys.argv)
    mw = ComboCRUD(db)
    dr = Drink()
    mw.show()
    # Run the application
    sys.exit(app.exec_())

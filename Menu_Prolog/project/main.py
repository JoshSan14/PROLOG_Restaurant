import sys
import PyQt5.QtWidgets as Qtw
from PyQt5.QtCore import Qt
import table as tbl
import gui_client as cgui
from utils import Utils as Utl
from db_conn import DBConn
import gui_crud_combo
import gui_crud_plate
import gui_crud_drink
import gui_crud_dessert
import gui_crud_garrison
import gui_crud_protein
import gui_table


class Main(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.db_conn = DBConn("restaurante", "postgres", "1234", "localhost", "5432")

        # Add a title
        self.setWindowTitle("Restaurante")
        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        self.crud_combo = gui_crud_combo.ComboCRUD(self.db_conn)
        self.crud_plate = gui_crud_plate.PlateCRUD(self.db_conn)
        self.crud_dessert = gui_crud_dessert.DessertCRUD(self.db_conn)
        self.crud_drink = gui_crud_drink.DrinkCRUD(self.db_conn)
        self.crud_garrison = gui_crud_garrison.GarrisonCRUD(self.db_conn)
        self.crud_protein = gui_crud_protein.ProteinCRUD(self.db_conn)
        self.table_adm = gui_table.TableDialog(self.db_conn)

        # Crud
        self.crud_ing_lyt = Qtw.QHBoxLayout()
        self.crud_ing_lbl = Qtw.QLabel("Ver, Agregar, Editar y Eliminar Ingredientes ")
        self.crud_ing_lyt.addWidget(self.crud_ing_lbl)
        self.crud_des_btn = Qtw.QPushButton("Postre")
        self.crud_des_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_dessert))
        self.crud_ing_lyt.addWidget(self.crud_des_btn)
        self.crud_pro_btn = Qtw.QPushButton("Proteína")
        self.crud_pro_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_protein))
        self.crud_ing_lyt.addWidget(self.crud_pro_btn)
        self.crud_dri_btn = Qtw.QPushButton("Bebida")
        self.crud_dri_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_drink))
        self.crud_ing_lyt.addWidget(self.crud_dri_btn)
        self.crud_gar_btn = Qtw.QPushButton("Guarnición")
        self.crud_gar_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_garrison))
        self.crud_ing_lyt.addWidget(self.crud_gar_btn)

        self.crud_menu_lyt = Qtw.QHBoxLayout()
        self.crud_menu_lbl = Qtw.QLabel("Ver, Agregar, Editar y Eliminar Menú ")
        self.crud_menu_lyt.addWidget(self.crud_menu_lbl)
        self.crud_plate_btn = Qtw.QPushButton("Platos")
        self.crud_plate_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_plate))
        self.crud_menu_lyt.addWidget(self.crud_plate_btn)
        self.crud_combo_btn = Qtw.QPushButton("Combos")
        self.crud_combo_btn.clicked.connect(lambda: Utl.open_dialog(self.crud_combo))
        self.crud_menu_lyt.addWidget(self.crud_combo_btn)

        self.admin_lyt = Qtw.QHBoxLayout()
        self.admin_lbl = Qtw.QLabel("Sistema Administrador")
        self.admin_lyt.addWidget(self.admin_lbl)
        self.table_adm_btn = Qtw.QPushButton("Administrar Mesas")
        self.table_adm_btn.clicked.connect(lambda: Utl.open_dialog(gui_table.TableDialog(self.db_conn)))
        self.admin_lyt.addWidget(self.table_adm_btn)

        self.main_lyt.addLayout(self.crud_ing_lyt)
        self.main_lyt.addLayout(self.crud_menu_lyt)
        self.main_lyt.addLayout(self.admin_lyt)
        self.setLayout(self.main_lyt)

        self.show()




if __name__ == "__main__":
    app = Qtw.QApplication(sys.argv)
    mw = Main()
    sys.exit(app.exec_())

import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt
import healthy_menu as hm
import client as clnt
import order as ordr


class HealthyMenuWindow(Qtw.QWidget):
    def __init__(self, healthy_menu, client):
        super().__init__()

        # plMenu instance
        self.pl_menu = healthy_menu

        # Client
        self.client = client

        # Add a title
        self.setWindowTitle(f"Menú saludable de {self.client.name}")
        # Set layout
        self.main_lyt = Qtw.QVBoxLayout()

        # Options
        self.nat_opts = ["cualquiera", "vegana", "carnica"]
        self.des_opts = ["cualquiera", "dulce", "salado", "amargo", "acido", "umami"]
        self.pro_ori_opts = ["cualquiera", "pollo", "pescado", "cerdo", "res", "marisco"]
        self.tex_opts = ["cualquiera", "suave", "dura"]
        self.dri_cat_opts = ["cualquiera", "soda", "natural", "batido"]
        self.temp_opts = ["cualquiera", "caliente", "frio", "tibio"]
        self.dri_base_opts = ["cualquiera", "agua", "leche", "gas"]
        self.gar_cat_opts = ["cualquiera", "grano", "tuberculo", "verdura", "pan"]
        self.size_opts = ["cualquiera", "pequeño", "mediano", "grande"]
        self.g_coc_opts = ["cualquiera", "cocido", "fritura", "fresco", "al vapor", "asado", "tostado", "horneado",
                           "salteado", "puré"]
        self.pro_coc_opts = ["asado", "al vapor", "fritura", "horneado", "asado", "sofrito"]
        self.col_hdr = ["Bebida", "Proteína", "Guarnición 1", "Guarnición 2", "Guarnición 3", "Postre", "Precio ($)",
                        "Calorías (Kcal)"]

        # Naturaleza Dietetica
        self.nat_lyt = Qtw.QVBoxLayout()
        self.nat_lbl = Qtw.QLabel("Naturaleza Dietética")
        self.nat_lbl.setAlignment(Qt.AlignCenter)
        self.nat_lyt.addWidget(self.nat_lbl)
        self.nat_cbox = Qtw.QComboBox()
        self.nat_cbox.addItems(self.nat_opts)
        self.nat_lyt.addWidget(self.nat_cbox)

        # Desayuno, Almuerzo y Cena
        self.check_lyt = Qtw.QHBoxLayout()
        self.check_lyt.setAlignment(Qt.AlignCenter)
        self.br_chbox = Qtw.QCheckBox("Desayuno")
        self.lu_chbox = Qtw.QCheckBox("Almuezo")
        self.di_chbox = Qtw.QCheckBox("Cena")
        self.check_lyt.addWidget(self.br_chbox)
        self.check_lyt.addWidget(self.lu_chbox)
        self.check_lyt.addWidget(self.di_chbox)

        # Tiempos Alimenticios
        self.time_lyt = Qtw.QVBoxLayout()
        self.time_lbl = Qtw.QLabel("Tiempos Alimenticios")
        self.time_lbl.setAlignment(Qt.AlignCenter)
        self.time_lyt.addWidget(self.time_lbl)
        self.time_lyt.addLayout(self.check_lyt)

        self.validator = Qtg.QDoubleValidator(0.0, 10000.0, 2)

        self.pri_lyt = Qtw.QVBoxLayout()
        self.pri_lbl = Qtw.QLabel("Precio Max ($)")
        self.pri_lbl.setAlignment(Qt.AlignCenter)
        self.pri_lyt.addWidget(self.pri_lbl)
        self.pri_tbox = Qtw.QLineEdit()
        self.pri_tbox.setText("10000")
        self.pri_tbox.setValidator(self.validator)
        self.pri_lyt.addWidget(self.pri_tbox)

        self.cal_lyt = Qtw.QVBoxLayout()
        self.cal_lbl = Qtw.QLabel("Calorias Max (Kcal)")
        self.cal_lbl.setAlignment(Qt.AlignCenter)
        self.cal_lyt.addWidget(self.cal_lbl)
        self.cal_tbox = Qtw.QLineEdit()
        self.cal_tbox.setText("5000")
        self.cal_tbox.setValidator(self.validator)
        self.cal_lyt.addWidget(self.cal_tbox)

        # General Layout
        self.gen_lyt = Qtw.QHBoxLayout()
        self.gen_lbl = Qtw.QLabel("General:")
        self.gen_lyt.addWidget(self.gen_lbl)
        self.gen_lyt.addLayout(self.nat_lyt)
        self.gen_lyt.addLayout(self.time_lyt)
        self.gen_lyt.addLayout(self.pri_lyt)
        self.gen_lyt.addLayout(self.cal_lyt)

        ###################################

        # Flavor
        self.pro_fla_lyt = Qtw.QVBoxLayout()
        self.pro_fla_lbl = Qtw.QLabel("Sabor")
        self.pro_fla_lyt.addWidget(self.pro_fla_lbl)
        self.pro_fla_lbl.setAlignment(Qt.AlignCenter)
        self.pro_fla_cbox = Qtw.QComboBox()
        self.pro_fla_cbox.addItems(self.des_opts)
        self.pro_fla_lyt.addWidget(self.pro_fla_cbox)

        # Origin
        self.pro_ori_lyt = Qtw.QVBoxLayout()
        self.pro_ori_lbl = Qtw.QLabel("Origen")
        self.pro_ori_lyt.addWidget(self.pro_ori_lbl)
        self.pro_ori_lbl.setAlignment(Qt.AlignCenter)
        self.pro_ori_cbox = Qtw.QComboBox()
        self.pro_ori_cbox.addItems(self.pro_ori_opts)
        self.pro_ori_lyt.addWidget(self.pro_ori_cbox)

        # Texture
        self.pro_tex_lyt = Qtw.QVBoxLayout()
        self.pro_tex_lbl = Qtw.QLabel("Textura")
        self.pro_tex_lyt.addWidget(self.pro_tex_lbl)
        self.pro_tex_lbl.setAlignment(Qt.AlignCenter)
        self.pro_tex_cbox = Qtw.QComboBox()
        self.pro_tex_cbox.addItems(self.tex_opts)
        self.pro_tex_lyt.addWidget(self.pro_tex_cbox)

        # Cooking Method
        self.pro_coc_lyt = Qtw.QVBoxLayout()
        self.pro_coc_lbl = Qtw.QLabel("Método de Cocción")
        self.pro_coc_lyt.addWidget(self.pro_coc_lbl)
        self.pro_coc_lbl.setAlignment(Qt.AlignCenter)
        self.pro_coc_cbox = Qtw.QComboBox()
        self.pro_coc_cbox.addItems(self.pro_coc_opts)
        self.pro_coc_lyt.addWidget(self.pro_coc_cbox)

        # Protein Layout
        self.pro_lyt = Qtw.QHBoxLayout()
        self.pro_lbl = Qtw.QLabel("Proteina:")
        self.pro_lyt.addWidget(self.pro_lbl)
        self.pro_lyt.addLayout(self.pro_fla_lyt)
        self.pro_lyt.addLayout(self.pro_ori_lyt)
        self.pro_lyt.addLayout(self.pro_tex_lyt)
        self.pro_lyt.addLayout(self.pro_coc_lyt)

        ###################################

        # Drink Layout

        # Flavor
        self.dri_fla_lyt = Qtw.QVBoxLayout()
        self.dri_fla_lbl = Qtw.QLabel("Sabor")
        self.dri_fla_lyt.addWidget(self.dri_fla_lbl)
        self.dri_fla_lbl.setAlignment(Qt.AlignCenter)
        self.dri_fla_cbox = Qtw.QComboBox()
        self.dri_fla_cbox.addItems(self.des_opts)
        self.dri_fla_lyt.addWidget(self.dri_fla_cbox)

        self.dri_cat_lyt = Qtw.QVBoxLayout()
        self.dri_cat_lbl = Qtw.QLabel("Categoria")
        self.dri_cat_lyt.addWidget(self.dri_cat_lbl)
        self.dri_cat_lbl.setAlignment(Qt.AlignCenter)
        self.dri_cat_cbox = Qtw.QComboBox()
        self.dri_cat_cbox.addItems(self.dri_cat_opts)
        self.dri_cat_lyt.addWidget(self.dri_cat_cbox)

        self.dri_temp_lyt = Qtw.QVBoxLayout()
        self.dri_temp_lbl = Qtw.QLabel("Temperatura")
        self.dri_temp_lyt.addWidget(self.dri_temp_lbl)
        self.dri_temp_lbl.setAlignment(Qt.AlignCenter)
        self.dri_temp_cbox = Qtw.QComboBox()
        self.dri_temp_cbox.addItems(self.temp_opts)
        self.dri_temp_lyt.addWidget(self.dri_temp_cbox)

        self.dri_base_lyt = Qtw.QVBoxLayout()
        self.dri_base_lbl = Qtw.QLabel("Base")
        self.dri_base_lyt.addWidget(self.dri_base_lbl)
        self.dri_base_lbl.setAlignment(Qt.AlignCenter)
        self.dri_base_cbox = Qtw.QComboBox()
        self.dri_base_cbox.addItems(self.dri_base_opts)
        self.dri_base_lyt.addWidget(self.dri_base_cbox)

        self.dri_lyt = Qtw.QHBoxLayout()
        self.dri_lbl = Qtw.QLabel("Bebida:")
        self.dri_lyt.addWidget(self.dri_lbl)
        self.dri_lyt.addLayout(self.dri_fla_lyt)
        self.dri_lyt.addLayout(self.dri_cat_lyt)
        self.dri_lyt.addLayout(self.dri_temp_lyt)
        self.dri_lyt.addLayout(self.dri_base_lyt)

        ###################################

        # Flavor
        self.gar1_fla_lyt = Qtw.QVBoxLayout()
        self.gar1_fla_lbl = Qtw.QLabel("Sabor")
        self.gar1_fla_lyt.addWidget(self.gar1_fla_lbl)
        self.gar1_fla_lbl.setAlignment(Qt.AlignCenter)
        self.gar1_fla_cbox = Qtw.QComboBox()
        self.gar1_fla_cbox.addItems(self.des_opts)
        self.gar1_fla_lyt.addWidget(self.gar1_fla_cbox)

        self.gar1_cat_lyt = Qtw.QVBoxLayout()
        self.gar1_cat_lbl = Qtw.QLabel("Categoria")
        self.gar1_cat_lyt.addWidget(self.gar1_cat_lbl)
        self.gar1_cat_lbl.setAlignment(Qt.AlignCenter)
        self.gar1_cat_cbox = Qtw.QComboBox()
        self.gar1_cat_cbox.addItems(self.gar_cat_opts)
        self.gar1_cat_lyt.addWidget(self.gar1_cat_cbox)

        self.gar1_size_lyt = Qtw.QVBoxLayout()
        self.gar1_size_lbl = Qtw.QLabel("Tamaño")
        self.gar1_size_lyt.addWidget(self.gar1_size_lbl)
        self.gar1_size_lbl.setAlignment(Qt.AlignCenter)
        self.gar1_size_cbox = Qtw.QComboBox()
        self.gar1_size_cbox.addItems(self.size_opts)
        self.gar1_size_lyt.addWidget(self.gar1_size_cbox)

        self.gar1_coc_lyt = Qtw.QVBoxLayout()
        self.gar1_coc_lbl = Qtw.QLabel("Método de Cocción")
        self.gar1_coc_lyt.addWidget(self.gar1_coc_lbl)
        self.gar1_coc_lbl.setAlignment(Qt.AlignCenter)
        self.gar1_coc_cbox = Qtw.QComboBox()
        self.gar1_coc_cbox.addItems(self.g_coc_opts)
        self.gar1_coc_lyt.addWidget(self.gar1_coc_cbox)

        self.gar1_lyt = Qtw.QHBoxLayout()
        self.gar1_lbl = Qtw.QLabel("Guarnicion 1:")
        self.gar1_lyt.addWidget(self.gar1_lbl)
        self.gar1_lyt.addLayout(self.gar1_fla_lyt)
        self.gar1_lyt.addLayout(self.gar1_cat_lyt)
        self.gar1_lyt.addLayout(self.gar1_size_lyt)
        self.gar1_lyt.addLayout(self.gar1_coc_lyt)

        self.gar2_fla_lyt = Qtw.QVBoxLayout()
        self.gar2_fla_lbl = Qtw.QLabel("Sabor")
        self.gar2_fla_lyt.addWidget(self.gar2_fla_lbl)
        self.gar2_fla_lbl.setAlignment(Qt.AlignCenter)
        self.gar2_fla_cbox = Qtw.QComboBox()
        self.gar2_fla_cbox.addItems(self.des_opts)
        self.gar2_fla_lyt.addWidget(self.gar2_fla_cbox)

        self.g2_cat_lyt = Qtw.QVBoxLayout()
        self.gar2_cat_lbl = Qtw.QLabel("Categoria")
        self.g2_cat_lyt.addWidget(self.gar2_cat_lbl)
        self.gar2_cat_lbl.setAlignment(Qt.AlignCenter)
        self.gar2_cat_cbox = Qtw.QComboBox()
        self.gar2_cat_cbox.addItems(self.gar_cat_opts)
        self.g2_cat_lyt.addWidget(self.gar2_cat_cbox)

        self.gar2_size_lyt = Qtw.QVBoxLayout()
        self.gar2_size_lbl = Qtw.QLabel("Tamaño")
        self.gar2_size_lyt.addWidget(self.gar2_size_lbl)
        self.gar2_size_lbl.setAlignment(Qt.AlignCenter)
        self.gar2_size_cbox = Qtw.QComboBox()
        self.gar2_size_cbox.addItems(self.size_opts)
        self.gar2_size_lyt.addWidget(self.gar2_size_cbox)

        self.gar2_coc_lyt = Qtw.QVBoxLayout()
        self.gar2_coc_lbl = Qtw.QLabel("Método de Cocción")
        self.gar2_coc_lyt.addWidget(self.gar2_coc_lbl)
        self.gar2_coc_lbl.setAlignment(Qt.AlignCenter)
        self.gar2_coc_cbox = Qtw.QComboBox()
        self.gar2_coc_cbox.addItems(self.g_coc_opts)
        self.gar2_coc_lyt.addWidget(self.gar2_coc_cbox)

        self.gar2_lyt = Qtw.QHBoxLayout()
        self.gar2_lbl = Qtw.QLabel("Guarnicion 2:")
        self.gar2_lyt.addWidget(self.gar2_lbl)
        self.gar2_lyt.addLayout(self.gar2_fla_lyt)
        self.gar2_lyt.addLayout(self.g2_cat_lyt)
        self.gar2_lyt.addLayout(self.gar2_size_lyt)
        self.gar2_lyt.addLayout(self.gar2_coc_lyt)

        self.gar3_fla_lyt = Qtw.QVBoxLayout()
        self.gar3_fla_lbl = Qtw.QLabel("Sabor")
        self.gar3_fla_lyt.addWidget(self.gar3_fla_lbl)
        self.gar3_fla_lbl.setAlignment(Qt.AlignCenter)
        self.gar3_fla_cbox = Qtw.QComboBox()
        self.gar3_fla_cbox.addItems(self.des_opts)
        self.gar3_fla_lyt.addWidget(self.gar3_fla_cbox)

        self.gar3_cat_lyt = Qtw.QVBoxLayout()
        self.gar3_cat_lbl = Qtw.QLabel("Categoria")
        self.gar3_cat_lyt.addWidget(self.gar3_cat_lbl)
        self.gar3_cat_lbl.setAlignment(Qt.AlignCenter)
        self.gar3_cat_cbox = Qtw.QComboBox()
        self.gar3_cat_cbox.addItems(self.gar_cat_opts)
        self.gar3_cat_lyt.addWidget(self.gar3_cat_cbox)

        self.gar3_size_lyt = Qtw.QVBoxLayout()
        self.gar3_size_lbl = Qtw.QLabel("Tamaño")
        self.gar3_size_lyt.addWidget(self.gar3_size_lbl)
        self.gar3_size_lbl.setAlignment(Qt.AlignCenter)
        self.gar3_size_cbox = Qtw.QComboBox()
        self.gar3_size_cbox.addItems(self.size_opts)
        self.gar3_size_lyt.addWidget(self.gar3_size_cbox)

        self.gar3_coc_lyt = Qtw.QVBoxLayout()
        self.gar3_coc_lbl = Qtw.QLabel("Método de Cocción")
        self.gar3_coc_lyt.addWidget(self.gar3_coc_lbl)
        self.gar3_coc_lbl.setAlignment(Qt.AlignCenter)
        self.gar3_coc_cbox = Qtw.QComboBox()
        self.gar3_coc_cbox.addItems(self.g_coc_opts)
        self.gar3_coc_lyt.addWidget(self.gar3_coc_cbox)

        self.gar3_lyt = Qtw.QHBoxLayout()
        self.gar3_lbl = Qtw.QLabel("Guarnicion 3:")
        self.gar3_lyt.addWidget(self.gar3_lbl)
        self.gar3_lyt.addLayout(self.gar3_fla_lyt)
        self.gar3_lyt.addLayout(self.gar3_cat_lyt)
        self.gar3_lyt.addLayout(self.gar3_size_lyt)
        self.gar3_lyt.addLayout(self.gar3_coc_lyt)

        self.des_fla_lyt = Qtw.QVBoxLayout()
        self.des_fla_lbl = Qtw.QLabel("Sabor")
        self.des_fla_lyt.addWidget(self.des_fla_lbl)
        self.des_fla_lbl.setAlignment(Qt.AlignCenter)
        self.des_fla_cbox = Qtw.QComboBox()
        self.des_fla_cbox.addItems(self.des_opts)
        self.des_fla_lyt.addWidget(self.des_fla_cbox)

        self.des_tex_lyt = Qtw.QVBoxLayout()
        self.des_tex_lbl = Qtw.QLabel("Textura")
        self.des_tex_lyt.addWidget(self.des_tex_lbl)
        self.des_tex_lbl.setAlignment(Qt.AlignCenter)
        self.des_tex_cbox = Qtw.QComboBox()
        self.des_tex_cbox.addItems(self.tex_opts)
        self.des_tex_lyt.addWidget(self.des_tex_cbox)

        self.des_temp_lyt = Qtw.QVBoxLayout()
        self.des_temp_lbl = Qtw.QLabel("Temperatura")
        self.des_temp_lyt.addWidget(self.des_temp_lbl)
        self.des_temp_lbl.setAlignment(Qt.AlignCenter)
        self.des_temp_cbox = Qtw.QComboBox()
        self.des_temp_cbox.addItems(self.temp_opts)
        self.des_temp_lyt.addWidget(self.des_temp_cbox)

        self.des_lyt = Qtw.QHBoxLayout()
        self.des_lbl = Qtw.QLabel("Postre:")
        self.des_lyt.addWidget(self.des_lbl)
        self.des_lyt.addLayout(self.des_fla_lyt)
        self.des_lyt.addLayout(self.des_tex_lyt)
        self.des_lyt.addLayout(self.des_temp_lyt)

        self.opts_btn = Qtw.QPushButton("Buscar Opciones")
        self.opts_btn.clicked.connect(self.show_menu_items)

        self.table = Qtw.QTableWidget(0, len(self.col_hdr))
        self.table.setHorizontalHeaderLabels(self.col_hdr)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.select_opt_btn = Qtw.QPushButton("Seleccionar Opción")
        self.select_opt_btn.clicked.connect(self.select_option)

        self.main_lyt.addLayout(self.gen_lyt)
        self.main_lyt.addLayout(self.dri_lyt)
        self.main_lyt.addLayout(self.pro_lyt)
        self.main_lyt.addLayout(self.gar1_lyt)
        self.main_lyt.addLayout(self.gar2_lyt)
        self.main_lyt.addLayout(self.gar3_lyt)
        self.main_lyt.addLayout(self.des_lyt)
        self.main_lyt.addWidget(self.opts_btn)
        self.main_lyt.addWidget(self.table)
        self.main_lyt.addWidget(self.select_opt_btn)
        self.main_lyt.setAlignment(Qt.AlignCenter)

        self.setLayout(self.main_lyt)
        self.show()

    def map_values_to_symbol(self, word, symbol, dictionary):
        for key, value in dictionary.items():
            if value == word:
                dictionary[key] = symbol
        return dictionary

    def get_options(self):
        try:
            opts = {
                "max_cals": float(self.cal_tbox.text()),
                "max_pre": float(self.pri_tbox.text()),
                "br": int(self.br_chbox.isChecked()),
                "lu": int(self.lu_chbox.isChecked()),
                "di": int(self.lu_chbox.isChecked()),
                "nat": self.nat_cbox.currentText().lower(),
                "dri_fla": self.dri_fla_cbox.currentText().lower(),
                "dri_cat": self.dri_cat_cbox.currentText().lower(),
                "dri_temp": self.dri_temp_cbox.currentText().lower(),
                "dri_base": self.dri_base_cbox.currentText().lower(),
                "pro_fla": self.pro_fla_cbox.currentText().lower(),
                "pro_ori": self.pro_ori_cbox.currentText().lower(),
                "pro_tex": self.pro_tex_cbox.currentText().lower(),
                "pro_coc": self.pro_coc_cbox.currentText().lower(),
                "gar1_fla": self.gar1_fla_cbox.currentText().lower(),
                "gar1_cat": self.gar1_cat_cbox.currentText().lower(),
                "gar1_size": self.gar1_size_cbox.currentText().lower(),
                "gar1_coc": self.gar1_coc_cbox.currentText().lower(),
                "gar2_fla": self.gar2_fla_cbox.currentText().lower(),
                "gar2_cat": self.gar2_cat_cbox.currentText().lower(),
                "gar2_size": self.gar2_size_cbox.currentText().lower(),
                "gar2_coc": self.gar2_coc_cbox.currentText().lower(),
                "gar3_fla": self.gar3_fla_cbox.currentText().lower(),
                "gar3_cat": self.gar3_cat_cbox.currentText().lower(),
                "gar3_size": self.gar3_size_cbox.currentText().lower(),
                "gar3_coc": self.gar3_coc_cbox.currentText().lower(),
                "des_fla": self.des_fla_cbox.currentText().lower(),
                "des_tex": self.des_tex_cbox.currentText().lower(),
                "des_temp": self.des_temp_cbox.currentText().lower()
            }
            qu_opts = self.map_values_to_symbol('cualquiera', '_', opts)
            return qu_opts

        except (ValueError, AttributeError) as e:
            print(f"An error occurred: {e}")

    def fill_table(self, tuple_list):
        # Ensure that the number of rows and columns is set properly
        num_columns = len(self.col_hdr)
        self.table.setColumnCount(num_columns)

        # Clear the table first, in case it already contains data
        self.table.setRowCount(0)

        # Set the number of rows to match the number of tuples
        self.table.setRowCount(len(tuple_list))

        for row, data in enumerate(tuple_list):
            for col, item in enumerate(data):
                item = Qtw.QTableWidgetItem(str(item))
                self.table.setItem(row, col, item)

        self.table.resizeColumnsToContents()

    def show_menu_items(self, quantity):
        qu_opts = self.get_options()
        print(qu_opts)
        query = self.pl_menu.menu_query(999, qu_opts["max_cals"], qu_opts["max_pre"], qu_opts["br"], qu_opts["lu"],
                                        qu_opts["di"], qu_opts["nat"], qu_opts["dri_fla"], qu_opts["dri_cat"],
                                        qu_opts["dri_temp"], qu_opts["dri_base"], qu_opts["pro_fla"],
                                        qu_opts["pro_ori"], qu_opts["pro_tex"], qu_opts["pro_coc"], qu_opts["gar1_fla"],
                                        qu_opts["gar1_cat"], qu_opts["gar1_size"], qu_opts["gar1_coc"],
                                        qu_opts["gar2_fla"], qu_opts["gar2_cat"], qu_opts["gar2_size"],
                                        qu_opts["gar2_coc"], qu_opts["gar3_fla"], qu_opts["gar3_cat"],
                                        qu_opts["gar3_size"], qu_opts["gar3_coc"], qu_opts["des_fla"],
                                        qu_opts["des_tex"], qu_opts["des_temp"])
        for q in query:
            print(q)
        self.fill_table(query)

    def get_selected_row(self):
        try:
            selected_row = self.table.currentRow()
            return selected_row
        except Exception as e:
            print(f"Error: {e}")

    def select_option(self):
        try:
            combo = []
            selected_row = self.get_selected_row()
            for i in range(len(self.col_hdr)):
                combo.append(self.table.item(selected_row, i).text())
            order = ordr.Order(
                id_order=self.get_last_id() + 1,
                description=f"{combo[0]} + {combo[1]} + {combo[2]} + {combo[3]} + {combo[4]} + {combo[5]}",
                price=combo[6],
                cals=combo[7]
            )
            self.client.order.append(order)
            print("\n")
            for ord in self.client.order:
                print(ord.description)
        except Exception as e:
            print(f"Error: {e} 1")

    def get_last_id(self):
        try:
            if len(self.client.order) > 0:
                return self.client.order[-1].id_order
            else:
                return 0
        except Exception as e:
            print(f"Error: {e} 5")


if __name__ == "__main__":
    app = Qtw.QApplication(sys.argv)
    healthy = hm.HealthyMenu()
    client = clnt.Client(5, "Joshua")
    mw = HealthyMenuWindow(healthy, client)

    # Run the application
    sys.exit(app.exec_())

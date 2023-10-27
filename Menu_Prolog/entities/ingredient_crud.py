import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
from abc import ABC, abstractmethod


class IngredientCRUD(Qtw.QDialog):

    def __init__(self, db_conn, ingredient):
        super().__init__()

        self.db_conn = db_conn

        self.ingredient = ingredient

        self.nat_opts = self.ingredient.nat_opts
        self.flav_opts = self.ingredient.flav_opts

        # Name Layout
        self.name_lyt = Qtw.QHBoxLayout()
        self.name_lbl = Qtw.QLabel("Nombre:")
        self.name_lbl.setAlignment(Qt.AlignCenter)
        self.name_lyt.addWidget(self.name_lbl)
        self.name_tbox = Qtw.QLineEdit()
        self.name_lyt.addWidget(self.name_tbox)

        # Naturaleza Dietetica
        self.diet_nat_lyt = Qtw.QVBoxLayout()
        self.diet_nat_lbl = Qtw.QLabel("Naturaleza Dietética")
        self.diet_nat_lbl.setAlignment(Qt.AlignCenter)
        self.diet_nat_lyt.addWidget(self.diet_nat_lbl)
        self.diet_nat_cbox = Qtw.QComboBox()
        self.diet_nat_cbox.addItems(self.nat_opts)
        self.diet_nat_lyt.addWidget(self.diet_nat_cbox)

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

        # Flavor
        self.fla_lyt = Qtw.QVBoxLayout()
        self.fla_lbl = Qtw.QLabel("Sabor")
        self.fla_lyt.addWidget(self.fla_lbl)
        self.fla_lbl.setAlignment(Qt.AlignCenter)
        self.fla_cbox = Qtw.QComboBox()
        self.fla_cbox.addItems(self.flav_opts)
        self.fla_lyt.addWidget(self.fla_cbox)

        self.validator = Qtg.QDoubleValidator(0.0, 10000.0, 2)

        # Cals
        self.cal_lyt = Qtw.QVBoxLayout()
        self.cal_lbl = Qtw.QLabel("Calorías (Kcal)")
        self.cal_lbl.setAlignment(Qt.AlignCenter)
        self.cal_lyt.addWidget(self.cal_lbl)
        self.cal_tbox = Qtw.QLineEdit()
        self.cal_tbox.setValidator(self.validator)
        self.cal_lyt.addWidget(self.cal_tbox)

        # Price
        self.pri_lyt = Qtw.QVBoxLayout()
        self.pri_lbl = Qtw.QLabel("Precio ($)")
        self.pri_lbl.setAlignment(Qt.AlignCenter)
        self.pri_lyt.addWidget(self.pri_lbl)
        self.pri_tbox = Qtw.QLineEdit()
        self.pri_tbox.setValidator(self.validator)
        self.pri_lyt.addWidget(self.pri_tbox)

        # Buttons
        self.btn_lyt = Qtw.QHBoxLayout()
        self.clean_btn = Qtw.QPushButton("Limpiar")
        self.clean_btn.clicked.connect(self.clean_inputs)
        self.btn_lyt.addWidget(self.clean_btn)
        self.add_btn = Qtw.QPushButton("Añadir")
        self.add_btn.clicked.connect(self.insert_rec)
        self.btn_lyt.addWidget(self.add_btn)
        self.update_btn = Qtw.QPushButton("Actualizar")
        self.update_btn.clicked.connect(self.update_rec)
        self.btn_lyt.addWidget(self.update_btn)
        self.delete_btn = Qtw.QPushButton("Borrar")
        self.delete_btn.clicked.connect(self.delete_rec)
        self.btn_lyt.addWidget(self.delete_btn)

    @abstractmethod
    def locate_rec(self, record):
        pass

    @abstractmethod
    def upload_object(self):
        pass

    @abstractmethod
    def download_object(self):
        pass

    @abstractmethod
    def clean_inputs(self):
        pass

    @abstractmethod
    def insert_rec(self):
        pass

    @abstractmethod
    def load_recs(self):
        pass

    @abstractmethod
    def update_rec(self):
        pass

    @abstractmethod
    def delete_rec(self):
        pass

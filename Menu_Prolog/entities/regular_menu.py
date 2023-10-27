class RegularMenu:
    def __init__(self, id_regular_menu=0):
        self.id_regular_menu = id_regular_menu
        self.cals = 0
        self.price = 0


class Plate(RegularMenu):
    def __init__(self, id_regular_menu=0, id_protein=0, id_garrison1=0, id_garrison2=0, id_garrison3=0):
        super().__init__(id_regular_menu)
        self.id_protein = id_protein
        self.id_garrison1 = id_garrison1
        self.id_garrison2 = id_garrison2
        self.id_garrison3 = id_garrison3


class Combo(Plate):
    def __init__(self, id_regular_menu=0, id_protein=0, id_garrison1=0, id_garrison2=0, id_garrison3=0,
                 id_drink=0, id_dessert=0):
        super().__init__(id_regular_menu, id_protein, id_garrison1, id_garrison2, id_garrison3)
        self.id_drink = id_drink
        self.id_dessert = id_dessert

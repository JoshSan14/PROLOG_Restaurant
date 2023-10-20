class Order:
    def __init__(self, id_order):
        self.id_order = id_order
        self.cals = 0
        self.price = 0


class Plate:
    def __init__(self, id_order, id_protein, id_garrison1, id_garrison2, id_garrison3):
        super().__init__(id_order)
        self.id_protein = id_protein
        self.id_garrison1 = id_garrison1
        self.id_garrison2 = id_garrison2
        self.id_garrison3 = id_garrison3


class Combo:
    def __init__(self, id_order, id_protein, id_garrison1, id_garrison2, id_garrison3, id_drink, id_dessert):
        super().__init__(id_protein, id_garrison1, id_garrison2, id_garrison3, id_order)
        self.id_drink = id_drink
        self.id_dessert = id_dessert

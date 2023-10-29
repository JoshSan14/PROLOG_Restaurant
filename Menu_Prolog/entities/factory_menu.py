class MenuFactory:
    @staticmethod
    def create_plate(id_menu, cals, price,  id_protein, id_garrison1, id_garrison2, id_garrison3):
        return Plate(id_menu, cals, price, id_protein, id_garrison1, id_garrison2, id_garrison3)

    @staticmethod
    def create_combo(id_menu, cals, price, id_protein, id_garrison1, id_garrison2, id_garrison3, id_drink, id_dessert):
        return Combo(id_menu, cals, price, id_protein, id_garrison1, id_garrison2, id_garrison3, id_drink, id_dessert)
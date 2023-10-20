from db_conn import DBConn
from abc import ABC, abstractmethod


# @abstractmethod
# def get_ingredient__db(self):
#     return self.db_conn.load_table(self.table_name)
#
#
# @abstractmethod
# def add_ingredient_db(self, new_record):
#     self.db_conn.add_record(self.table_name, new_record)
#     print("Added")
#
#
# @abstractmethod
# def edit_ingredient_db(self, id_column, record_id, new_values):
#     self.db_conn.update_record(self.table_name, id_column, record_id, new_values)
#     print("Updated")
#
#
# @abstractmethod
# def delete_ingredient_db(self, record_id):
#     self.db_conn.delete_record(self.table_name, record_id)
#     print("Deleted")

class Ingredient:
    def __init__(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner):
        self.id_ingredient = id_ingredient
        self.name = name
        self.cals = cals
        self.diet_nat = diet_nat
        self.flavor = flavor
        self.price = price
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.db_conn = DBConn("restaurante", "postgres", "1234", "localhost", "5432")
        self.table_name = "ingrediente.ingrediente"

    def create(self):
        new_record = {"nombre": self.name, "calorias": self.cals, "naturaleza_dietetica": self.diet_nat, "sabor": sabor,
                      "precio": self.price, "desayuno": self.desayuno, "almuerzo": self.almuerzo, "cena": self.cena}
        self.db_conn.create_record(self.table_name, new_record)

    @classmethod
    def read(cls, id_ingredient):
        pass

    def update(self, table, id_column, record_id, new_values):
        updated_record = {"nombre": self.name, "calorias": self.cals, "naturaleza_dietetica": self.diet_nat, "sabor": sabor,
                        "precio": self.price, "desayuno": self.desayuno, "almuerzo": self.almuerzo, "cena": self.cena}

    def delete(self):
        pass

class Drink(Ingredient, ABC):
    def __init__(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, category,
                 temperature, base):
        super().__init__(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.category = category
        self.temperature = temperature
        self.base = base
        self.table_name = "ingrediente.bebida"


class Protein(Ingredient, ABC):
    def __init__(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, origin,
                 texture, cook_met):
        super().__init__(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.origin = origin
        self.texture = texture
        self.cook_met = cook_met
        self.table_name = "ingrediente.proteina"


class Garrison(Ingredient, ABC):
    def __init__(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, category,
                 size, cook_met):
        super().__init__(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.category = category
        self.size = size
        self.cook_met = cook_met
        self.table_name = "ingrediente.guarnicion"


class Dessert(Ingredient, ABC):
    def __init__(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, texture,
                 temperature):
        super().__init__(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.texture = texture
        self.temperature = temperature
        self.table_name = "ingrediente.postre"


if __name__ == "__main__":
    drink = Drink(id_ingredient=1, name="Soda", cals=100, diet_nat=False, flavor="Cola", price=2.50,
                  breakfast=True, lunch=True, dinner=True, category="Soft Drink", temperature="Cold", base="Carbonated")

    protein = Protein(id_ingredient=2, name="Chicken Breast", cals=150, diet_nat=True, flavor="Neutral", price=5.99,
                      breakfast=False, lunch=True, dinner=True, origin="Poultry", texture="Lean", cook_met="Grilled")

    garrison = Garrison(id_ingredient=3, name="French Fries", cals=300, diet_nat=False, flavor="Salty", price=3.00,
                        breakfast=False, lunch=True, dinner=True, category="Side Dish", size="Large",
                        cook_met="Deep Fried")

    dessert = Dessert(id_ingredient=4, name="Chocolate Cake", cals=400, diet_nat=False, flavor="Chocolate", price=4.50,
                      breakfast=False, lunch=False, dinner=True, texture="Moist", temperature="Room Temperature")

    print(drink.get_ingredient_table_name())
    print(drink.get_ingredient_table_name())
    print(garrison.get_ingredient_table_name())
    print(dessert.get_ingredient_table_name())

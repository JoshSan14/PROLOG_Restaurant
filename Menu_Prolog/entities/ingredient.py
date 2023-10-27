from abc import ABC, abstractmethod


# Definimos una clase abstracta llamada 'Ingredient' que servirá como base para otros ingredientes.
class Ingredient(ABC):
    def __init__(self, id_object, name, cals, diet_nat, flavor, price, breakfast, lunch,
                 dinner):
        self.id_object = id_object  # Identificador único del ingrediente
        self.name = name  # Nombre del ingrediente
        self.cals = cals  # Cantidad de calorías
        self.diet_nat = diet_nat  # Naturaleza dietética
        self.flavor = flavor  # Sabor
        self.price = price  # Precio
        self.breakfast = breakfast  # Disponibilidad en el desayuno
        self.lunch = lunch  # Disponibilidad en el almuerzo
        self.dinner = dinner  # Disponibilidad en la cena
        self.id_column = "id"
        self.nat_opts = ["Vegana", "Carnica"]
        self.flav_opts = ["Dulce", "Salado", "Amargo", "Acido", "Umami"]

    @abstractmethod
    def to_dict(self):
        pass


# Creamos una subclase 'Drink' que hereda de 'Ingredient'.
class Drink(Ingredient):

    def __init__(self, id_object=0, name="", cals=0, diet_nat="", flavor="", price=0, breakfast=True, lunch=True,
                 dinner=True, category="", temperature="", base=""):
        super().__init__(id_object, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.category = category  # Categoría de la bebida
        self.temperature = temperature  # Temperatura ideal
        self.base = base  # Base de la bebida
        self.table_name = "ingrediente.bebida"  # Nombre de la tabla en la base de datos
        self.cat_opts = ["Soda", "Natural", "Batido"]
        self.temp_opts = ["Caliente", "Frio", "Tibio"]
        self.base_opts = ["Agua", "Leche", "Gas"]
        self.col_ord = ["id", "nombre", "naturaleza_dietetica", "desayuno", "almuerzo", "cena", "sabor", "categoria",
                        "temperatura", "base", "calorias", "precio"]
        self.col_hdr = ["ID", "Nombre", "Naturaleza Dietética", "Desayuno", "Almuerzo", "Cena", "Sabor", "Categoria",
                        "Temperatura", "Base", "Calorías (Kcal)", "Precio ($)"]

    def to_dict(self):
        return {"nombre": self.name, "calorias": self.cals,
                "naturaleza_dietetica": self.diet_nat, "sabor": self.flavor, "precio": self.price,
                "desayuno": self.breakfast, "almuerzo": self.lunch, "cena": self.dinner, "categoria": self.category,
                "temperatura": self.temperature, "base": self.base}


# Creamos una subclase 'Protein' que hereda de 'Ingredient'.
class Protein(Ingredient):

    def __init__(self, id_object=0, name="", cals=0, diet_nat="", flavor="", price=0, breakfast=True, lunch=True,
                 dinner=True, origin="", texture="", cook_met=""):
        super().__init__(id_object, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.origin = origin  # Origen de la proteína
        self.texture = texture  # Textura
        self.cook_met = cook_met  # Método de cocción
        self.table_name = "ingrediente.proteina"  # Nombre de la tabla en la base de datos
        self.ori_opts = ["Pollo", "Pescado", "Cerdo", "Res", "Marisco"]
        self.tex_opts = ["Suave", "Dura"]
        self.cook_met_opts = ["Asado", "Al vapor", "Fritura", "Horneado", "Asado", "Sofrito"]
        self.col_ord = ["id", "nombre", "naturaleza_dietetica", "desayuno", "almuerzo", "cena", "sabor", "origen",
                        "textura", "metodo_coccion", "calorias", "precio"]
        self.col_hdr = ["ID", "Nombre", "Naturaleza Dietética", "Desayuno", "Almuerzo", "Cena", "Sabor", "Origen",
                        "Textura", "Método de Cocción", "Calorías (Kcal)", "Precio ($)"]

    def to_dict(self):
        return {"nombre": self.name, "calorias": self.cals,
                "naturaleza_dietetica": self.diet_nat, "sabor": self.flavor, "precio": self.price,
                "desayuno": self.breakfast, "almuerzo": self.lunch, "cena": self.dinner, "origen": self.origin,
                "textura": self.texture, "metodo_coccion": self.cook_met}


# Creamos una subclase 'Garrison' que hereda de 'Ingredient'.
class Garrison(Ingredient):
    def __init__(self, id_object=0, name="", cals=0, diet_nat="", flavor="", price=0, breakfast=True, lunch=True,
                 dinner=True, category="", size="", cook_met=""):
        super().__init__(id_object, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.category = category  # Categoría de la guarnición
        self.size = size  # Tamaño
        self.cook_met = cook_met  # Método de cocción
        self.table_name = "ingrediente.guarnicion"  # Nombre de la tabla en la base de datos
        self.cat_opts = ["Grano", "Tuberculo", "Verdura", "Pan"]
        self.size_opts = ["Pequeño", "Mediano", "Grande"]
        self.cook_met_opts = ["Cocido", "Fritura", "Fresco", "Al vapor", "Asado", "Tostado", "Horneado", "Salteado", "Puré"]
        self.col_ord = ["id", "nombre", "naturaleza_dietetica", "desayuno", "almuerzo", "cena", "sabor", "categoria",
                        "tamano", "metodo_coccion", "calorias", "precio"]
        self.col_hdr = ["ID", "Nombre", "Naturaleza Dietética", "Desayuno", "Almuerzo", "Cena", "Sabor", "Categoria",
                        "Tamaño", "Método de Cocción", "Calorías (Kcal)", "Precio ($)"]

    def to_dict(self):
        return {"nombre": self.name, "calorias": self.cals,
                "naturaleza_dietetica": self.diet_nat, "sabor": self.flavor, "precio": self.price,
                "desayuno": self.breakfast, "almuerzo": self.lunch, "cena": self.dinner, "categoria": self.category,
                "tamano": self.size, "metodo_coccion": self.cook_met}


# Creamos una subclase 'Dessert' que hereda de 'Ingredient'.
class Dessert(Ingredient):
    def __init__(self, id_object=0, name="", cals=0, diet_nat="", flavor="", price=0, breakfast=True, lunch=True,
                 dinner=True, texture="", temperature=""):
        super().__init__(id_object, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner)
        self.texture = texture  # Textura del postre
        self.temperature = temperature  # Temperatura ideal
        self.table_name = "ingrediente.postre"  # Nombre de la tabla en la base de datos
        self.tex_opts = ["Suave", "Dura"]
        self.temp_opts = ["Caliente", "Frio", "Tibio"]
        self.col_ord = ["id", "nombre", "naturaleza_dietetica", "desayuno", "almuerzo", "cena", "sabor", "textura",
                        "temperatura", "calorias", "precio"]
        self.col_hdr = ["ID", "Nombre", "Naturaleza Dietética", "Desayuno", "Almuerzo", "Cena", "Sabor", "Textura",
                        "Temperatura", "Calorías (Kcal)", "Precio ($)"]

    def to_dict(self):
        return {"nombre": self.name, "calorias": self.cals,
                "naturaleza_dietetica": self.diet_nat, "sabor": self.flavor, "precio": self.price,
                "desayuno": self.breakfast, "almuerzo": self.lunch, "cena": self.dinner, "textura": self.texture,
                "temperatura": self.temperature}

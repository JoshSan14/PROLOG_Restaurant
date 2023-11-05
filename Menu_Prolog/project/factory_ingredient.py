from abc import ABC, abstractmethod
from ingredient import *


# Factory Method (Método de Fábrica)

# Clase base abstracta para la fábrica de ingredientes
class IngredientFactory(ABC):
    @abstractmethod
    def create_ingredient(self, id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, **kwargs):
        # Este es un método abstracto que define la interfaz para crear ingredientes.
        pass


# Subclase para crear ingredientes de tipo Bebida (Drink)
class DrinkFactory(IngredientFactory):
    @staticmethod
    def create_ingredient(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, **kwargs):
        try:
            # Aquí debes acceder a los valores de kwargs para obtener los valores adicionales, como category, temperature y base.
            category = kwargs.get('category')
            temperature = kwargs.get('temperature')
            base = kwargs.get('base')

            return Drink(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, category,
                         temperature, base)
        except Exception as e:
            print(f"Error reading record: {e}")


# Subclase para crear ingredientes de tipo Proteína (Protein)
class ProteinFactory(IngredientFactory):
    @staticmethod
    def create_ingredient(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, **kwargs):
        try:
            # Accede a los valores de kwargs para obtener los valores adicionales, como origin, texture y cook_met.
            origin = kwargs.get('origin')
            texture = kwargs.get('texture')
            cook_met = kwargs.get('cook_met')

            return Protein(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, origin,
                           texture, cook_met)
        except Exception as e:
            print(f"Error reading record: {e}")


# Subclase para crear ingredientes de tipo Guarnición (Garrison)
class GarrisonFactory(IngredientFactory):
    @staticmethod
    def create_ingredient(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, **kwargs):
        try:
            # Accede a los valores de kwargs para obtener los valores adicionales, como category, size y cook_met.
            category = kwargs.get('category')
            size = kwargs.get('size')
            cook_met = kwargs.get('cook_met')

            return Garrison(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, category,
                            size, cook_met)
        except Exception as e:
            print(f"Error reading record: {e}")


# Subclase para crear ingredientes de tipo Postre (Dessert)
class DessertFactory(IngredientFactory):
    @staticmethod
    def create_ingredient(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, **kwargs):
        try:
            # Accede a los valores de kwargs para obtener los valores adicionales, como texture y temperature.
            texture = kwargs.get('texture')
            temperature = kwargs.get('temperature')

            return Dessert(id_ingredient, name, cals, diet_nat, flavor, price, breakfast, lunch, dinner, texture,
                           temperature)
        except Exception as e:
            print(f"Error reading record: {e}")

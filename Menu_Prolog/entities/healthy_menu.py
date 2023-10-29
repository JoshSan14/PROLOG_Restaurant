import db_conn as dbc
from decimal import Decimal
from pyswip import Prolog as Pl


class HealthyMenu:
    def __init__(self, database):
        self.query_ingredients = Pl()
        self.database = database
        self.drink_db = self.database.retrieve_all_records("ingrediente.bebida")
        self.protein_db = self.database.retrieve_all_records("ingrediente.proteina")
        self.garrison_db = self.database.retrieve_all_records("ingrediente.guarnicion")
        self.dessert_db = self.database.retrieve_all_records("ingrediente.postre")
        self.load_menu_data(self.drink_db, self.protein_db, self.garrison_db, self.dessert_db)
        self.query_ingredients.consult("query.pl")

    def load_menu_data(self, drink, protein, garrison, dessert):
        self.assert_data(drink, "bebida")
        self.assert_data(protein, "proteina")
        self.assert_data(garrison, "guarnicion")
        self.assert_data(dessert, "postre")

    def assert_data(self, data, query):
        for dato in data:
            formatted_data = []
            for item in dato:
                if isinstance(item, float):
                    formatted_data.append(f'{round(item, 1)}')
                else:
                    formatted_data.append(f"'{str(item).lower()}'")
            hecho = f"{query}({', '.join(formatted_data)})"
            self.query_ingredients.assertz(hecho)

    def test_queries(self):
        for query in self.query_ingredients.query(
                "bebida(Id, Nombre, Cals, Naturaleza, Sabor, Precio, Desayuno, Almuerzo, Cena, Categoria, "
                "Temperatura, Base)"):
            print(query)
        for query in self.query_ingredients.query(
                "proteina(Id, Nombre, Cals, Naturaleza, Sabor, Precio, Desayuno, Almuerzo, Cena, Origen, Textura, "
                "Coccion)"):
            print(query)
        for query in self.query_ingredients.query(
                "guarnicion(Id, Nombre, Cals, 'vegana', Sabor, Precio, Desayuno, Almuerzo, Cena, Categoria, "
                "Tamano, Coccion)"):
            print(query)
        for query in self.query_ingredients.query(
                "postre(Id, Nombre, Cals, Naturaleza, Sabor, Precio, Desayuno, Almuerzo, Cena, Textura, "
                "Temperatura)"):
            print(query)

    def menu_query(self, max_res, max_cals, max_pre, br, lu, di, nat, dri_fla, dri_cat, dri_temp, dri_base, pro_fla,
                   pro_ori, pro_tex, pro_coc, gar1_fla, gar1_cat, gar1_size, gar1_coc, gar2_fla, gar2_cat, gar2_size,
                   gar2_coc, gar3_fla, gar3_cat, gar3_size, gar3_coc, des_fla, des_tex, des_temp):
        results = []
        result_count = 0
        for query in self.query_ingredients.query(
                f"menu({max_cals}, {max_pre}, TCALS, TPRE, {br}, {lu}, {di}, {nat}, BID, BNOM, BCALS, {dri_fla}, BPRE, "
                f"{dri_cat}, {dri_temp}, {dri_base}, PRID, PRNOM, PRCALS, {pro_fla}, PRPRE, {pro_ori}, {pro_tex}, "
                f"{pro_coc}, G1ID, G1NOM, G1CALS, {gar1_fla}, G1PRE, {gar1_cat}, {gar1_size}, {gar1_coc}, G2ID, G2NOM, "
                f"G2CALS, {gar2_fla}, G2PRE, {gar2_cat}, {gar2_size}, {gar2_coc}, G3ID, G3NOM, G3CALS, {gar3_fla}, "
                f"G3PRE, {gar3_cat}, {gar3_size}, {gar3_coc}, POID, PONOM, POCALS, {des_fla}, POPRE, {des_tex}, "
                f"{des_temp})"):
            results.append((query["BNOM"], query["PRNOM"], query["G1NOM"], query["G2NOM"], query["G3NOM"],
                            query["PONOM"], round(query["TPRE"], 2), round(query["TCALS"], 2)))
            if result_count >= max_res:
                break
            result_count += 1
        return results

    def main(self):
        try:
            self.test_queries()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            if hasattr(self, "conn"):
                self.conn.close()


if __name__ == "__main__":
    menu = HealthyMenu(dbc.DBConn("restaurante", "postgres", "1234", "localhost", "5432"))
    menu.main()

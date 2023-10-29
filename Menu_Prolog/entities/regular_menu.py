from abc import ABC, abstractmethod


class RegularMenu(ABC):
    def __init__(self, id_menu=0, cals=0, price=0):
        self.id_menu = id_menu
        self.cals = cals
        self.price = price
        self.id_column = "id"

    @abstractmethod
    def to_dict(self):
        pass


class Plate(RegularMenu):
    def __init__(self, id_menu=0, cals=0, price=0, id_protein=0, id_garrison1=0, id_garrison2=0, id_garrison3=0):
        super().__init__(id_menu, cals, price)
        self.id_protein = id_protein
        self.id_garrison1 = id_garrison1
        self.id_garrison2 = id_garrison2
        self.id_garrison3 = id_garrison3
        self.table_name = "menu.plato"
        self.col_ord = ["id", "proteina", "guarnicion_1", "guarnicion_2", "guarnicion_3", "calorias", "precio"]
        self.col_hdr = ["ID", "Proteína", "Guarnición 1", "Guarnición 2", "Guarnición 3", "Calorías (Kcal)",
                        "Precio ($)"]

    def to_dict(self):
        return {"proteina": self.id_protein, "guarnicion_1": self.id_garrison1, "guarnicion_2": self.id_garrison2,
                "guarnicion_3": self.id_garrison3, "calorias": self.cals, "precio": self.price}

    @staticmethod
    def get_all_db_menu(db_conn):
        sql_query = """
        SELECT
            MP.id AS plate_id,
            P.nombre AS proteina_nombre,
            G1.nombre AS guarnicion_1_nombre,
            G2.nombre AS guarnicion_2_nombre,
            G3.nombre AS guarnicion_3_nombre,
            MP.calorias AS calorias_menu_plate,
            MP.precio AS precio_menu_plate
        FROM
            menu.plato AS MP
        LEFT JOIN
            ingrediente.proteina AS P ON MP.proteina = P.id
        LEFT JOIN
            ingrediente.guarnicion AS G1 ON MP.guarnicion_1 = G1.id
        LEFT JOIN
            ingrediente.guarnicion AS G2 ON MP.guarnicion_2 = G2.id
        LEFT JOIN
            ingrediente.guarnicion AS G3 ON MP.guarnicion_3 = G3.id
        ORDER BY MP.id ASC;
        """
        return db_conn.execute_custom_query(sql_query)

    @staticmethod
    def get_db_menu(menu_item_id, db_conn):
        sql_query = """
        SELECT
            MP.id AS plate_id,
            P.nombre AS proteina_nombre,
            G1.nombre AS guarnicion_1_nombre,
            G2.nombre AS guarnicion_2_nombre,
            G3.nombre AS guarnicion_3_nombre,
            MP.calorias AS calorias_menu_plate,
            MP.precio AS precio_menu_plate
        FROM
            menu.plato AS MP
        LEFT JOIN
            ingrediente.proteina AS P ON MP.proteina = P.id
        LEFT JOIN
            ingrediente.guarnicion AS G1 ON MP.guarnicion_1 = G1.id
        LEFT JOIN
            ingrediente.guarnicion AS G2 ON MP.guarnicion_2 = G2.id
        LEFT JOIN
            ingrediente.guarnicion AS G3 ON MP.guarnicion_3 = G3.id;
        WHERE
            MP.id = %s;
        """
        return db_conn.execute_custom_query(sql_query, (menu_item_id,))


class Combo(Plate):
    def __init__(self, id_menu=0, cals=0, price=0, id_protein=0, id_garrison1=0, id_garrison2=0, id_garrison3=0,
                 id_drink=0, id_dessert=0):
        super().__init__(id_menu, cals, price, id_protein, id_garrison1, id_garrison2, id_garrison3)
        self.id_drink = id_drink
        self.id_dessert = id_dessert
        self.table_name = "menu.combo"
        self.col_ord = ["id", "proteina", "guarnicion_1", "guarnicion_2", "guarnicion_3", "bebida", "postre",
                        "calorias", "precio"]
        self.col_hdr = ["ID", "Proteína", "Guarnición 1", "Guarnición 2", "Guarnición 3", "Bebida", "Postre",
                        "Calorías (Kcal)", "Precio ($)"]

    def to_dict(self):
        return {"proteina": self.id_protein, "guarnicion_1": self.id_garrison1, "guarnicion_2": self.id_garrison2,
                "guarnicion_3": self.id_garrison3, "bebida": self.id_drink, "postre": self.id_dessert,
                "calorias": self.cals, "precio": self.price}

    @staticmethod
    def get_all_db_menu(db_conn):
        sql_query = """
        SELECT
            MC.id AS combo_id,
            P.nombre AS proteina_nombre,
            G1.nombre AS guarnicion_1_nombre,
            G2.nombre AS guarnicion_2_nombre,
            G3.nombre AS guarnicion_3_nombre,
            B.nombre AS bebida_nombre,
            Po.nombre As postre_nombre, 
            MC.calorias AS calorias_menu_combo,
            MC.precio AS precio_menu_combo
        FROM
            menu.combo AS MC
        LEFT JOIN
            ingrediente.proteina AS P ON MC.proteina = P.id
        LEFT JOIN
            ingrediente.guarnicion AS G1 ON MC.guarnicion_1 = G1.id
        LEFT JOIN
            ingrediente.guarnicion AS G2 ON MC.guarnicion_2 = G2.id
        LEFT JOIN
            ingrediente.guarnicion AS G3 ON MC.guarnicion_3 = G3.id
        LEFT JOIN
            ingrediente.bebida AS B ON MC.bebida = B.id
        LEFT JOIN
            ingrediente.postre AS Po ON MC.postre = Po.id
        ORDER BY MC.id ASC;
        """
        return db_conn.execute_custom_query(sql_query)

    @staticmethod
    def get_db_menu(menu_item_id, db_conn):
        sql_query = """
        SELECT
            MC.id AS combo_id,
            P.nombre AS proteina_nombre,
            G1.nombre AS guarnicion_1_nombre,
            G2.nombre AS guarnicion_2_nombre,
            G3.nombre AS guarnicion_3_nombre,
            B.nombre AS bebida_nombre,
            Po.nombre As postre_nombre, 
            MC.calorias AS calorias_menu_combo,
            MC.precio AS precio_menu_combo
        FROM
            menu.combo AS MC
        LEFT JOIN
            ingrediente.proteina AS P ON MC.proteina = P.id
        LEFT JOIN
            ingrediente.guarnicion AS G1 ON MC.guarnicion_1 = G1.id
        LEFT JOIN
            ingrediente.guarnicion AS G2 ON MC.guarnicion_2 = G2.id
        LEFT JOIN
            ingrediente.guarnicion AS G3 ON MC.guarnicion_3 = G3.id
        LEFT JOIN
            ingrediente.bebida AS B ON MC.bebida = B.id
        LEFT JOIN
            ingrediente.postre AS Po ON MC.postre = Po.id
        WHERE
            MC.id = %s;
        """
        return db_conn.execute_custom_query(sql_query, (menu_item_id,))

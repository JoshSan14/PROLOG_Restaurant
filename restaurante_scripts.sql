CREATE SCHEMA IF NOT EXISTS ingrediente;

CREATE TABLE ingrediente.general (
	id_ingrediente SERIAL PRIMARY KEY, --Autoincremental.
    nombre VARCHAR(50), 
    calorias NUMERIC,
    naturaleza_dietetica VARCHAR(15), --Vegana o Carnica.
    sabor VARCHAR(10), --Dulce, Salado, Amargo, Acido y Umami.
    precio NUMERIC,
	desayuno BOOLEAN, --¿Es apto para el desayuno?
	almuerzo BOOLEAN, --¿Es apto para el almuerzo?
	cena BOOLEAN --¿Es apto para la cena?
);

CREATE TABLE Ingrediente.bebida (
    categoria VARCHAR(10), --Soda, Natural, Batido en agua o Batido en leche.
    temperatura VARCHAR(10), --Frio, Tibio o Caliente.
    base VARCHAR(10) -- Gas(Si es soda), Agua(Si es natural o batido en agua) o Leche(Si es batido en leche).
) INHERITS (Ingrediente.general);

CREATE TABLE Ingrediente.proteina (
    origen VARCHAR(15), -- Pollo, Pescado, Cerdo o Res.
    textura VARCHAR(10), -- Suave, Dura o Mixta.
    metodo_coccion VARCHAR(20) -- Cocido, Al vapor, Escaldado, Horneado, Fritura, Asado, Tostado o Sofrito.
) INHERITS (Ingrediente.general);

CREATE TABLE Ingrediente.guarnicion (
    categoria VARCHAR(15), -- Grano, Tuberculo, Verdura, Salsa o Pan.
    tamaño VARCHAR(10), -- Pequeño, Mediano o Grande
    metodo_coccion VARCHAR(20) -- Cocido, Al vapor, Escaldado, Horneado, Fritura, Asado, Tostado o Sofrito.
) INHERITS (Ingrediente.general);

CREATE TABLE Ingrediente.postre (
    textura VARCHAR(10), -- Suave, Dura o Mixta.
    temperatura VARCHAR(10) --Frio, Tibio o Caliente.
) INHERITS (Ingrediente.general);


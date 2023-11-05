class Bill:
    def __init__(self, client, description="", payment_type="Efectivo", total=0):
        self.client = client
        self.description = description
        self.payment_type = payment_type
        self.total = total

    def to_dict(self):
        return {
            "client": self.client.name,
            "description": self.description,
            "payment_type": self.payment_type,
            "payment_total": self.payment_total
        }

    def pay_total(self, table):
        # Utilizar la función get_total_tax de la clase Table para obtener el total con impuestos
        self.total = client.get_total_tax()

        # Utilizar to_dict para obtener los datos del registro
        new_rec = self.to_dict()

        # Insertar los datos en la tabla de facturas usando insert_record
        self.insert_record("pago.factura", new_rec)

        # Eliminar los clientes de la mesa
        table.clients = []



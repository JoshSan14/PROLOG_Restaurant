class Table:
    def __init__(self, id_table):
        self.id_table = id_table
        self.clients = []
        self.total_bill = 0

    def get_total_tax(self):
        total_with_tax = 0
        for client in self.clients:
            total_with_tax += client.get_total_tax()
        return total_with_tax

    def generate_client_records(self):
        records = []
        for client in self.clients:
            record = [client.name, client.get_formatted_orders(), f"${client.get_total_tax()}"]
            records.append(record)
        return records
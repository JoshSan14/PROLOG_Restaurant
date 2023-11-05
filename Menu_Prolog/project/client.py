class Client:
    def __init__(self, id_client, name):
        self.id_client = id_client
        self.name = name
        self.order = []
        self.bill = 0

    def get_formatted_orders(self):
        return '\n'.join(self.order)

    def get_total_tax(self):
        total_with_tax = self.bill + (self.bill * 0.13)
        return total_with_tax
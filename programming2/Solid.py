class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def print_invoice(self):
        print(f"Invoice Amount: {self.amount}")

    def save_to_database(self):
        print("Saving invoice to database")


class Invoice:
    def __init__(self, amount):
        self.amount = amount

class InvoicePrinter:
    @staticmethod
    def print_invoice(invoice):
        print(f"Invoice Amount: {invoice.amount}")

class InvoiceSaver:
    @staticmethod
    def save_to_database(invoice):
        print("Saving invoice to database")

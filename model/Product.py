class Product:
    def __init__(self, id, name, category, sub_category, quantity, cost_price, selling_price, vendor_phone):
        self.id = id
        self.name = name
        self.category = category
        self.sub_category = sub_category
        self.quantity = quantity
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.vendor_phone = vendor_phone
    def __str__(self):
        info = f"Information: +Id: {self.id} \n + name: {self.name} \n +Quantity: {self.quantity}"
        return info
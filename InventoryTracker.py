class InventoryTracker:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def display_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def checkStockLevel(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        return "Item not found"

    def alertLowStock(self, item_name, threshold=5):
        if item_name in self.items:
            if self.items[item_name] < threshold:
                return f"Low stock alert: {item_name} has only {self.items[item_name]} items left"
            return f"{item_name} stock is sufficient"
        return "Item not found"
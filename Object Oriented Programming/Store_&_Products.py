class Store():
    def __init__(self):
        self.name = "Game Store"
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        print(self.products)
        return self

    def sell_product(self, id):
        print(self.products[id]['Name'])
        self.products.pop(id)
        print(self.products)
        return self
    
    def inflation(self, percent_increase):
        for i in range(0, len(self.products)):
            self.products[i]['Price'] += ((self.products[i]['Price'] * percent_increase) / 100)
        print(self.products)
        return self

    def clearance(self, percent_discount):
        for i in range(0, len(self.products)):
            self.products[i]['Price'] -= ((self.products[i]['Price'] * percent_discount) / 100)
        print(self.products)
        return self

class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += ((self.price * percent_change) / 100)
        else:
            self.price -= ((self.price * percent_change) / 100)
        print(self.price)

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Category: {self.category}")

store = Store()

store.add_product({'Name' : 'Dreamcast', 'Price' : 299, 'Category' : 'Game Console'})
store.add_product({'Name' : 'Gamecube 2', 'Price' : 99, 'Category' : 'Game Console'})
store.add_product({'Name' : 'Xbox 720', 'Price' : 499, 'Category' : 'Game Console'})

store.sell_product(0)

store.inflation(50)

store.clearance(50)







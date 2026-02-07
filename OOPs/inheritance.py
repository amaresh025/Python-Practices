class Items:  #class
    #constructor
    def __init__(self, name, price, stocks):
        self.name = name
        self.price = price
        self.stocks = stocks
#method
    def show_details(self):
        print(self.name, self.price, self.stocks)
#object
my_products = Items("laptop", 52000, 45)
my_products.show_details()


class Product(Items):
    def __init__(self, name, price, stocks, id, brand):
        super().__init__(name, price, stocks)
        self.id = id 
        self.brand = brand
    def all_details(self):
        super().show_details()
        print(self.id, self.brand)

my_shop = Product("ipad", 25000, 50, 1, "apple")
my_shop.all_details()
my_shop.show_details()


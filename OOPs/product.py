class Product:  #class
    #constructor
    def __init__(self, name, price, stocks):
        self.name = name
        self.price = price
        self.stocks = stocks
#method
    def show_details(self):
        print(self.name, self.price, self.stocks)
#object
my_products = Product("laptop", 52000, 45)
my_products.show_details()



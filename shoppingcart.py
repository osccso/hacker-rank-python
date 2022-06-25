class Item:
    # Implement the Item here
    def _init_(self,name,price):
        self.name = name
        self.price = price
        

class ShoppingCart:
    # Implement the ShoppingCart here
    def _init(self):
        self.cart = []
    
    def _len_(self):
        return len(self.cart)
    
    def add(self,item):
        self.cart.append(item)
    
    def total(self):
        sumPrices = 0
        for item in self.cart :
            sumPrices += item.price
        return sumPrices
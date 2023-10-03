class Shop:
    def __init__(self, buyer):
        self.buyer=buyer
        self.cart=[]#instance attribute
    def add_to_cart(self, item):
        self.cart.append(item)

ahmadulilah=Shop('ahmadullah')
ahmadulilah.add_to_cart("null pad")
ahmadulilah.add_to_cart("palisesh")
ahmadulilah.add_to_cart(" pad")

alamin=Shop('alamin')
alamin.add_to_cart('pen')
print(ahmadulilah.cart) 
print(alamin.cart)
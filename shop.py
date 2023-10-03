class Shop:
    cart=[]
    def __init__(self, buyer):
        self.buyer=buyer
    def add_to_cart(self, item):
        self.cart.append(item)

alamin=Shop("alamin")
alamin.add_to_cart("pen")
alamin.add_to_cart("book")
alamin.add_to_cart("pencel")
alamin.add_to_cart("pen point")
alamin.add_to_cart("pen boll")

print(alamin.cart)
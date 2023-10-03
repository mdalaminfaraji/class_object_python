class Shop:
    cart={}
    def __init__(self, buyer):
        self.buyer=buyer
    def add_to_cart(self, item, value):
        self.cart.update({item:value})

alamin=Shop("alamin")
alamin.add_to_cart("pen", 10)
alamin.add_to_cart("book", 20)
alamin.add_to_cart("pencel", 30)
alamin.add_to_cart("pen point", 40)
alamin.add_to_cart("pen boll", 50)

print(alamin.cart)
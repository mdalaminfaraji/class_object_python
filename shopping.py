class Shopping:
    def __init__(self, name):
        self.name=name
        self.cart=[]
    def add_to_cart(self, item, price, quantity):
        product={"item":item, 'price':price, 'quantity':quantity}
        self.cart.append(product)
    
    def checkout(self, amount):
        total=0
        for item in self.cart:
            print(item)
            total +=item['price'] *item['quantity']
        print('total price', total)

        if(amount<total):
            print(f' please provide {total - amount} more') 
        else:
            extra=amount-total
            print(f'give me {extra}')

alamin=Shopping('alamin')
alamin.add_to_cart('pen', 122, 23)
alamin.add_to_cart('bol', 122, 23)
alamin.add_to_cart('note', 122, 23)
print(alamin.cart)

alamin.checkout(565)
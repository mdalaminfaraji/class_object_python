class Pen:
    manufactured="china"
    def __init__(self, name, price, weight):
        self.name=name
        self.price=price
        self.weight=weight

matador=Pen('matador pin point', 7, 45.7)
olympic=Pen('olympic pin point', 7, 45.7)
hischool=Pen('hischool pin point', 7, 45.7)

print(matador.name, olympic.name, hischool.name)

        
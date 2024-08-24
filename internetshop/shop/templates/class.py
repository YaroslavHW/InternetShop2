class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        def calculate_price(self, discount):
            return self.price * (100 - discount) / 100

class TechProduct(Product):
    def __init__(self, name, price, fan, illumination):
        self.name = name
        self.price = price
        self.fan = fan
        self.illumination = illumination



class BookProduct(Product):
    def __init__(self, name, price, pages, color):
        self.name = name
        self.price = price
        self.pages = pages
        self.color = color



Product_list = [
    TechProduct(name='Видеокарта',price=45000, fan=3, illumination='yes'),
    BookProduct(name='Тетрадь',price=100,color='Жёлтый',pages=96),
]

print(Product_list[0].calculate_price(10))
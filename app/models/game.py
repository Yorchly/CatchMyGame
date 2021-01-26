class Game:
    id = None
    name = ""
    price = 0
    currency = "No se ha podido obtener"
    link = "No se ha podido obtener"

    def __init__(self, name, price, currency, link):
        self.name = name
        self.price = price
        self.currency = currency
        self.link = link

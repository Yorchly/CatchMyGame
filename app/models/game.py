class Game:
    id = None
    title = "No se ha podido obtener"
    price = "No se ha podido obtener"
    link = "No se ha podido obtener"
    search = ""

    def __init__(self, title, price, link, search):
        self.title = title if title else self.title
        self.price = price if price else self.price
        self.link = link if link else self.link
        self.search = search

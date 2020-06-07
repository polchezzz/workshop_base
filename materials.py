class Material:

    def __init__(self, name, amount, price, renewable):
        self.name = name
        self.amount = amount
        self.price = price
        self.renewable = renewable  # renewable means disposable

    def __str__(self):
        res = "Material: " + str(self.name) + ". Amount: " + str(self.amount) + ". Price: " + str(self.price) + "."
        return res

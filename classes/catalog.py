class Catalog:

    def __init__(self):
        self.number_of_workshops = 0
        self.workshops = []

    def __str__(self):
        ans = "Catalog: \n"
        for workshop in self.workshops:
            ans += workshop.get_full_workshop() + "\n"
        return ans

    def add_workshop(self, workshop):
        self.number_of_workshops += 1
        self.workshops.append(workshop)

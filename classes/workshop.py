from classes.common import *


class Workshop:

    def __init__(self, name, fullname):

        self.name = name
        self.fullname = fullname
        self.materials = []

    def __str__(self):

        ans = "Name: " + self.name + ". Full name: " + self.fullname
        return ans

    def get_materials(self):

        ans = ""
        for material in self.materials:
            ans += str(material) + "\n"
        return ans

    def add_material(self, new_material):

        add_material(self.materials, new_material)

    def add_materials(self, materials):

        self.materials = materials

    def get_full_workshop(self):

        ans = str(self)
        for material in self.materials:
            ans += str(material) + "\n"
        return ans

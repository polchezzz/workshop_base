from classes.common import *
from classes.material import Material


class Storage:

    def __init__(self, name, budget, extra):

        self.name = name
        self.budget = budget
        self.extra_charge = extra
        self.workshops = []
        self.materials = []

    def __str__(self):

        ans = "Storage: " + self.name
        ans += "Budget: " + str(self.budget) + "\n"
        ans += "Extra charge: " + str(self.extra_charge) + "\n"


        ans += "Available materials: \n"
        if len(self.materials) == 0:
            ans += "There are no free materials!\n"
        else:
            for material in self.materials:
                ans += str(material) + "\n"


        ans += "Active workshops: \n"
        if len(self.workshops) == 0:
            ans += "There are no active workshops!\n"
        else:
            for workshop in self.workshops:
                ans += str(workshop) + "\n"
        return ans

    def change_extra(self, new_extra):

        if new_extra < 0:
            return "Extra can't be negative!"
        self.extra_charge = new_extra
        return "Extra updated successfully!"

    def add_budget(self, amount):

        if amount < 0:
            return "Amount of money is negative!"
        self.budget += amount
        return "Amount of money added successfully!"

    def get_materials(self):

        ans = ""
        for material in self.materials:
            ans += str(material) + "\n"
        return ans

    def add_material(self, new_material):

        ans = add_material(self.materials, new_material)
        return ans

    def add_materials(self, materials):

        self.materials = materials

    def find_workshops(self, catalog):

        available_workshops = []


        for workshop in catalog.workshops:
            can_activate = True

            need_to_buy = []

            for material in workshop.materials:
                is_in_materials = False

                for my_material in self.materials:
                    if material.name == my_material.name:
                        is_in_materials = True
                        if material.amount > my_material.amount:
                            need_to_buy.append(Material(my_material.name, material.amount - my_material.amount,
                                                        my_material.price, my_material.renewable))
                if not is_in_materials:
                    need_to_buy.append(Material(material.name, material.amount,
                                                material.price, material.renewable))

            cost = 0
            for material in need_to_buy:
                cost += material.price * material.amount
            cost += cost * self.extra_charge / 100
            if cost > self.budget:
                can_activate = False

            if can_activate:
                available_workshops.append(workshop)

        if len(available_workshops) == 0:
            return "There are no available workshops!"

        ans = "Available workshops: \n"
        for workshop in available_workshops:
            ans += str(workshop)
        return ans

    def add_workshop(self, workshop):

        need_to_buy = []

        for material in workshop.materials:
            is_in_materials = False
            for my_material in self.materials:
                if material.name == my_material.name:
                    is_in_materials = True
                    if material.amount > my_material.amount:
                        need_to_buy.append(Material(my_material.name, material.amount - my_material.amount,
                                                    my_material.price, my_material.renewable))
            if not is_in_materials:
                need_to_buy.append(Material(material.name, material.amount,
                                            material.price, material.renewable))

        cost = 0
        for material in need_to_buy:
            cost += material.price * material.amount
        cost += cost * self.extra_charge / 100
        if cost > self.budget:
            ans = "Workshop: " + workshop.name + ". Not enough money to activate!"
            return False, ans

        self.workshops.append(workshop)
        for material in workshop.materials:
            for my_material in self.materials:
                if material.name == my_material.name:
                    if my_material.amount - material.amount <= 0:
                        self.materials.remove(my_material)
                    else:
                        my_material.amount -= material.amount

        self.budget -= cost
        ans = "Workshop: " + workshop.name + ". Activated successfully!"
        return True, ans

    def delete_workshop(self, workshop_to_del):

        for workshop in self.workshops:
            if workshop.name == workshop_to_del.name:
                for material in workshop.materials:
                    if material.renewable:
                        self.add_material(material)

                self.workshops.remove(workshop)
                ans = "Workshop: " + workshop_to_del.name + ". Deleted successfully!"
                return True, ans
        ans = "Workshop: " + workshop_to_del.name + ". Not found!"
        return False, ans

from classes.material import Material


def add_material(materials, new_material):


    for material in materials:
        if material.name == new_material.name:
            material.amount += new_material.amount
            ans = "Material: " + material.name + ". Amount updated!"
            return ans

    materials.append(new_material)
    ans = "Material: " + new_material.name + ". Added successfully!"
    return ans


def get_materials_from_file(file):
    materials = []
    amount = int(file.readline())
    for i in range(amount):
        temp = file.readline()
        material = temp.split('-')
        name = material[0]
        amount = int(material[1])
        price = int(material[2])
        if int(material[3]) == 1:
            renewable = True
        else:
            renewable = False
        materials.append(Material(name, amount, price, renewable))
    return materials


def write_materials_to_file(file, materials):
    file.write(str(len(materials)) + '\n')

    for i in range(len(materials)):
        material = materials[i].name + '-' + \
                   str(materials[i].amount) + '-' + \
                   str(materials[i].price) + '-'
        if materials[i].renewable:
            material += str(1)
        else:
            material += str(0)
        material += "\n"
        file.write(material)

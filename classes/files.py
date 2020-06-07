import os.path

from classes.storage import Storage
from classes.workshop import Workshop
from classes.common import *


def read_storage(filepath):

    storage_file = open(filepath)
    name = storage_file.readline().split(":")[1]
    budget = int(storage_file.readline().split(":")[1])
    extra = int(storage_file.readline().split(":")[1])
    storage_file.close()
    return Storage(name, budget, extra)


def read_materials(filepath, storage):

    materials_file = open(filepath)
    storage.add_materials(get_materials_from_file(materials_file))
    materials_file.close()


def read_workshops(filepath, catalog):

    for file in os.listdir(filepath):
        path = filepath + file
        workshop_file = open(path)
        name = file.split(".")[0]
        fullname = workshop_file.readline()
        workshop = Workshop(name, fullname)
        workshop.add_materials(get_materials_from_file(workshop_file))
        catalog.add_workshop(workshop)
        workshop_file.close()


def read_active_workshops(filepath, storage):

    workshops = []
    if len(os.listdir(filepath)) != 0:
        for file in os.listdir(filepath):
            path = filepath + "/" + file
            workshop_file = open(path)
            name = file.split(".")[0]
            fullname = workshop_file.readline()
            workshop = Workshop(name, fullname)
            workshop.add_materials(get_materials_from_file(workshop_file))
            workshops.append(workshop)
            workshop_file.close()
    storage.workshops = workshops


def write_storage(filepath, storage):

    storage_file = open(filepath, 'w')
    name = "Name: " + storage.name
    budget = "Budget: " + str(int(storage.budget)) + "\n"
    extra = "Extra charge: " + str(int(storage.extra_charge)) + "\n"
    storage_file.write(name)
    storage_file.write(budget)
    storage_file.write(extra)
    storage_file.close()


def write_materials(filepath, materials):

    materials_file = open(filepath, 'w')
    write_materials_to_file(materials_file, materials)
    materials_file.close()


def write_workshop(filepath, workshop):

    path = filepath + "/" + workshop.name + ".txt"
    workshop_file = open(path, 'w')
    workshop_file.write(workshop.fullname)
    write_materials_to_file(workshop_file, workshop.materials)
    workshop_file.close()


def remove_active_workshop(filepath, name):

    path = filepath + "/" + name + ".txt"
    os.remove(path)

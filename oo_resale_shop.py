from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    #I need the ability to add a computer to the inventory, and return it's computer ID
    def buy(computer: dict):
        inventory.append(computer)
        return inventory.index(computer)

    #I need the ability to edit this inventory to sell, or remove, a computer
    def sell(computer_id: int):
        if inventory[computer_id] is not None:
            inventory.pop(computer_id)
            print("Item", computer_id, "sold!")
        else:
            print("Item", computer_id, "not found. Please select another item to sell.")
        
    
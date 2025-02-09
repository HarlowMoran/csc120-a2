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
    def buy(self, new_computer, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
            self.description = description
            self.processor_type = processor_type
            self.hard_drive_capacity = hard_drive_capacity
            self.memory = memory
            self.operating_system = operating_system
            self.year_made = year_made
            self.price = price
            new_computer = Computer(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
            return new_computer
    #I need the ability to edit this inventory to add the new computer
    inventory.append(buy)
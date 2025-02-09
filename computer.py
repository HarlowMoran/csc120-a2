class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # Remember: in python, all constructors have the same name (__init__)
    #def __init__():
   #     pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    #I need the ability to update a computer with a new id and OS
    def refurbish(self, computer_id, new_OS):
         self.computer_id = computer_id
         self.new_OS = new_OS
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
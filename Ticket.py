class Ticket:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_ticket_info(self):
        return "Name: {self.name}, Phone Number: {self.number}"
    

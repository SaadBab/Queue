class Ticket_Machine:
    
    def __init__(self, location, mnumber):
        self.location = location
        self.mnumber = mnumber
        self.tickets = []

    #enqueue
    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"Ticket added: {ticket.name}, Ticket Number: {ticket.number}")

    #dequeue
    def get_next_ticket(self):
        if self.is_empty():
            print("No tickets available.")
            return None
        return self.tickets.pop(0)
        print("Ticket dequeued: {ticket.name}, Ticket Number: {ticket.number}")
        return ticket

    
    #checks if queue is empty
    def is_empty(self):
        return len(self.tickets) == 0
    
    #returns number of people in queue
    def people_in_queue(self):
        return len(self.tickets)
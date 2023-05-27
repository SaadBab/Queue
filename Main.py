from Ticket_Machine import Ticket_Machine
from Ticket import Ticket

class Main:

    machine = Ticket_Machine("OMA", "machine1")

    ticket1 = Ticket("MSB", 6123123123)
    ticket2 = Ticket("saad", 4678200222)

    machine.add_ticket(ticket1)
    machine.add_ticket(ticket2)

    status = machine.people_in_queue()
    print(f"People in queue: {status}")

    machine.get_next_ticket()
    machine.get_next_ticket()
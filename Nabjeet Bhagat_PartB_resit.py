
# Simple Ferry Booking System

unique_booking_id = 20000

class BookingSystem:
    # Initialize booking
    def __init__(self, form_of_id="", id_number="", passenger_name=""):
        global unique_booking_id
        unique_booking_id += 1
        self.ticket_id = unique_booking_id
        self.form_of_id = form_of_id
        self.id_number = id_number
        self.passenger_name = passenger_name
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

    # Get customer information
    # KISS: Simple method, only collects user input
    # SRP (SOLID): Single Responsibility Principle – only handles customer info
    def customer_info(self):
        self.form_of_id = input("Enter Form of ID (Passport/Driver's License): ")
        self.id_number = input("Enter ID Number: ")
        self.passenger_name = input("Enter Passenger Name: ")

    # Get ferry service details and total price
    # DRY: Uses a loop for multiple services instead of repeating input lines
    # KISS: Keeps total calculation simple
    # SRP: Only calculates total for services
    def ferry_service_details(self):
        num_services = int(input("Enter number of services: "))
        self.total = 0
        for i in range(num_services):
            price = float(input(f"Enter price for service {i+1}: "))
            self.total += price

    # Manager approval
    # KISS: Simple yes/no input determines approval
    # SRP: Only handles approval logic
    def booking_approval(self):
        decision = input("Manager approval required? (yes/no): ").lower()
        if decision == "yes":
            self.status = "Approved"
            # Simple approval reference calculation
            self.approval_ref = self.id_number[:3] + str(self.ticket_id)[-2:]
        else:
            self.status = "Not approved"
            self.approval_ref = "Not available"

    # Print booking info
    # KISS: Simple method, prints info only
    # SRP: Only displays booking info
    def display_booking_info(self):
        print("\nBooking Info:")
        print("Form of ID:", self.form_of_id)
        print("ID Number:", self.id_number)
        print("Passenger Name:", self.passenger_name)
        print("Ticket ID:", self.ticket_id)
        print("Total: $", "{:.2f}".format(self.total))
        print("Status:", self.status)
        print("Approval Ref:", self.approval_ref)

    # Show statistics
    # DRY: Loops through all bookings instead of repeating code for each booking
    # SRP: Only handles statistics display
    def booking_statistic(self, all_bookings):
        total = len(all_bookings)
        approved = 0
        pending = 0
        not_approved = 0

        for b in all_bookings:
            if b.status == "Approved":
                approved += 1
            elif b.status == "Pending":
                pending += 1
            elif b.status == "Not approved":
                not_approved += 1

        print("\nStatistics:")
        print("Total bookings submitted:", total)
        print("Total approved:", approved)
        print("Total pending:", pending)
        print("Total not approved:", not_approved)


# Main program
if __name__ == "__main__":
    bookings = []

    for i in range(2):
        print(f"\nBooking {i+1}")
        b = BookingSystem()
        b.customer_info()
        b.ferry_service_details()
        b.booking_approval()
        bookings.append(b)

    print("\nAll Bookings:")
    for b in bookings:
        b.display_booking_info()

    bookings[0].booking_statistic(bookings)

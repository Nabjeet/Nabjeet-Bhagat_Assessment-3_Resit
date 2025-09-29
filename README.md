# Nabjeet-Bhagat_Assessment-3_Resit
                   Ferry Booking System
Introduction
I made this small Python project for the Ferry Booking System. By adding passenger details, selecting services and receiving management approval it helps users make ferry reservations. A different ticket ID is allocated for each booking that specifies the total charge and stores the booking status. You can also see your reservartion list and simple statistics like how many approved, waiting for approval or not approved reservations you have.
I built this project in order to explore working with classes, methods and data managment in Python, as well as practice of object oriented programming. It will teach you how to handle user input, and some basic ludlomath as well; it’s simple but effective.

Features
1. Customer  Information: They can enter a name, an ID number and the type of identification (such as a passport or driver’s license).
2. Ferry Service Details: It is possible for users to add one or many services with their cost. To actually show the total cost, the system adds them together.
3. Booking Approval: Manager approval is required. If accepted, the booking reaches status “Approved” and is assigned an approval reference number. Otherwise, it’s “Not approved.”
4. Display Booking Info: For each booking, name, ID, ticket ID, total cost, status and approval reference are shown.
5. Booking Statistics: The system shows all booking figures (total bookings, approved, pending and not-approved).

Principles I Used 
I did attempt to keep to some programming guidelines in an attempt to write clear readable code:

KISS (Keep It Simple, Stupid)
Each methods can only perform a single simple operation. Namely, customer_info() takes user input and display_booking_info() just prints the booking.

DRY (Don’t Repeat Yourself)
I had used loops for repetitive when I should have written the same routine many times. For instance, a loop is employed in ferry_service_details() function to calculate multiple type of service pricing and I booking_statistic() function to compute the total number of approved or pending bookings.

SOLID – Single Responsibility Principle (SRP)
Each method should do only one thing. Only acceptance is done by booking_approval(), the totals are computed by ferry_service_details() and information is output with

How to Run Code
Follow the instructions in the program:
Enter your ID type, ID number, and name.
Enter the number of services and their prices.
Decide if the booking is approved by the manager (yes/no).
After entering all bookings, the program will show:
Each booking’s details
Booking statistics (total, approved, pending, not approved)

In conclusion
This project is straightforward but effective for making and overseeing ferry reservations. I was able to practice user input, loops, Python classes, and simple computations thanks to it. The code was clearer and simpler to read because to the application of KISS, DRY, and SRP concepts.

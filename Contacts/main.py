'''We are learning inheritance in Python.
This code defines a Contact class that can be used to create contact objects with a name and email.'''

class Contact:
    all_contacts = []
    
    def __init__(self,name , email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    
    
class Supplier(Contact):
    def order(self, order_number):
        print(f"Order {order_number} placed by {self.name} ({self.email})")
        
        
        

c = Contact("Akansha", "ak@google.com")
s = Supplier("Raghav", "Cancelledplans.com")


'''Let's print the details of the contacts'''
print(f"Contact Name: {c.name}, Email: {c.email}")

print(f"Supplier Name: {s.name}, Email: {s.email}")

'''Let's place an order using the Supplier class'''
s.order(12345)
'''Let's print all contacts'''
print("All Contacts:")
for contact in Contact.all_contacts:
    print(f"Name: {contact.name}, Email: {contact.email}")
'''This code demonstrates the use of inheritance in Python, where Supplier inherits from Contact.
It allows us to create a specialized type of contact that can perform additional actions, such as placing an order.'''


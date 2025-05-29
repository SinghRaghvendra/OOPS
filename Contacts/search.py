
'''Extending builtin list to create a ContactList class 
that can search for contacts by name.'''


from typing import Dict


class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
    
class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Contact.all_contacts.append(self)
        
        

        
        
c1 = Contact('Alice', '123-456-7890')
c2 = Contact('Bob', '987-654-3210')
c3 = Contact('Bob B', '555-555-5555')



results = Contact.all_contacts.search('Bob')
for contact in results:
    print(contact.name, contact.phone)



class LongNameContact(Dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest
    
longkey = LongNameContact()
longkey['short'] = 1
longkey['longer'] = 2
longkey['longest'] = 3
print(longkey.longest_key())  # Output: longest_key


        
        
        
        
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone

    def contact_info(self):
        print(f'''
Name: {self.name} 
Phone: {self.phone}
Email: {self.email}
''')
        
class ContactManager:
    def __init__(self):
        self.contact_book = []

    def add_contact(self, contact):
        self.contact_book.append(contact)

    def remove_contact(self, search):
        for contacts in self.contact_book:
            if contacts.name.lower() == search.lower():
                self.contact_book.remove(contacts)

    def search_contact (self, contact):
        for contacts in self.contact_book:
            if contacts.name.lower() == contact.lower() or contacts.email.lower() == contact.lower():
                contacts.contact_info()
                return
            else:
                print('Contact not found! ')


    def view_contacts(self):
        if len(self.contact_book) == 0:
            print('The contact book is empty! ')
        else:
            for contacts in self.contact_book:
                contacts.contact_info()


contact_manger = ContactManager()


def main():
    while True:
        print('''

1. Add 
2. Remove
3. Search
4. View Contact Book
5. Exit
''')
    
        user_input = input('> ')
        if user_input.isdigit():
            user_input = int(user_input)

            if user_input == 1:
                name = input('Enter the name: ')
                lastname = input('Enter the last name: ')
                phone = input('Enter the phone number: ')
                email = f'{name}.{lastname}@gmail.com'
                contact = Contact(name, phone, email)
                contact_manger.add_contact(contact)
                # print(email)

            elif user_input == 2:
                name = input('Enter the name of the contact u wanna remove: ')
                contact_manger.remove_contact(name)
            
            elif user_input == 3:
                user_input = input('Search: ')
                contact_manger.search_contact(user_input)
            
            elif user_input == 4:
                contact_manger.view_contacts()

            elif user_input == 5:
                break
            
            else:
                print('Invalid option! ')
        else:
            print('Invalid option! ')
                


main()
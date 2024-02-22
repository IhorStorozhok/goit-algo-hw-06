from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
   def __init__(self, name):
       if not name:
           raise ValueError("Name can't be empty")
       self.value = name

class Phone(Field):
    def __init__(self, phone):
        if not phone:
            raise ValueError("Phone can't be empty")
        if len(phone) < 10:
            raise ValueError("Phone must be 10 characters")
        if not phone.isdigit():
            raise ValueError("Phone must be digits")
        self.value = phone

    

    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []







    # реалізація класу
    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
             raise ValueError("Phone not found")

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(new_phone)
        else:
            print("Phone not found")
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            raise ValueError("Phone not found")                

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, Record):
        self.data[Record.name.value] = Record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")
        

# Створення нової адресної книги
book = AddressBook()
print(book)  # Виведення: {}

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")


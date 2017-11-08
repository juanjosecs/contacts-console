# -*- coding: utf-8 -*-
import csv
from contact import Contact

class ContactBook:

    def __init__(self):
        self._contacts = []


    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()


    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._print_contact(contact)    
                name = str(raw_input('Escribe el nuevo nombre del contacto: '))
                phone = str(raw_input('Escribe el nuevo tel del contacto: '))
                email = str(raw_input('Escribe el nuevo email del contacto: '))

                contact.name = name
                contact.phone = phone
                contact.email = email

                self._save()
                break

        else:
            self._not_found()   



    def show_all(self):

        if len(self._contacts) == 0:
            print("No existen contactos registrados")
        else:
            for contact in self._contacts:
                self._print_contact(contact)


    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
        else:
            self._not_found()

    
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def exists_contact(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():                
                return True

        return False


    def _save(self):
        with open("contacts.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow( ("name", "phone", "email") )
            
            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )


    def load_contacts(self):
        try:
            with open("contacts.csv", "r") as f:
                reader = csv.reader(f)
                for idx, row in enumerate(reader):
                    if idx == 0:
                        continue

                    self.add(row[0], row[1], row[2])
        except IOError:
            pass


    def _not_found(self):
        print("--- * --- * --- * --- *")
        print("Contacto no encontrado")
        print("--- * --- * --- * --- *")


    def _print_contact(self, contact):
        print("--- * --- * --- * --- * --- * ---")
        print("Nombre: {0}".format(contact.name))
        print("Teléfono: {0}".format(contact.phone))
        print("Email: {0}".format(contact.email))
        print("--- * --- * --- * --- * --- * ---")

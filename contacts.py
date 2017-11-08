# -*- coding: utf-8 -*-
from contact_book import ContactBook

def run():

    contact_book = ContactBook()

    contact_book.load_contacts()

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))

            if contact_book.exists_contact(name):
                print("{0} ya se encuentra registrado".format(name))

            else:
                phone = str(raw_input('Escribe el tel del contacto: '))
                email = str(raw_input('Escribe el email del contacto: '))
                contact_book.add(name, phone, email)

        elif command == 'ac':            
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.update(name)

        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O   A   L A   A G E N D A')
    run()
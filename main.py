import pandas


# Kontakte anzeigen
def display_contacts():
    print("h")


# Kontakt anlegen
def add_new_contact():
    print("h")


# Kontakt bearbeiten
def edit_contact():
    print("h")


# Kontakt löschen
def delete_contact():
    print("h")

# In die Datei schreiben 
def write_to_file(contact):
    # with csv
    df = pandas.read_csv('daten.csv', sep=';')
    try: 
        with open('contacts.csv', 'a') as file:
            for entry in contact:
                file.write(contact[entry])
    except Exception as e:
        print("Fehler " + e)


# Von der Datei auslesen
def read_from_file():
    print("h")

# Menu
def show_menu():
    while True:
        print('\n' + '*'*40)
        print('Kontaktbuch')
        print('\n' + '*'*40)
        print('1. Kontakte anzeigen')
        print('2. Kontakt anlegen')
        print('3. Kontakt bearbeiten')
        print('4. Kontakt löschen')
        print('5. Programm beenden')

        option = input("Wahl: ")

        if option == '1':
            display_contacts()
        elif option == '2':
            add_new_contact()
        elif option == '3':
            edit_contact()
        elif option == '4':
            delete_contact()
        elif option == '5':
            break
            


# funktion aufrufen
if __name__ == '__main__':
    show_menu()
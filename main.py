# Panda Modul macht beim Laufen des Codes Probleme bei mir, obwohl ich es installiert habe -> sena
# habe es mal auskommentiert
#import pandas

# Notizen Sena -> Ich glaube das Modul CSV ist besser für z.B einzelne Spalten (Name) auszugeben
# Importiert CSV-Modul
import csv

# Kontakte anzeigen
def display_contacts():
    try: 
        # Öffnet Datei im Lesemodus
        with open('contacts.csv', 'r', encoding='utf-8') as file:

            # Ganze CSV ausgeben als Liste
            reader = csv.reader(file, delimiter=';')

            # Ignoriert header (erste Zeile) im CSV 
            next(reader, None)
            
            # Für den Terminal Output 
            print("\n" + "=" * 50)
            print("\t\tMEINE KONTAKTE")
            print("\n" + "=" * 50)

            # Loopt durch die Listen
            for line in reader:
                # Sicherstellen, dass alle Spalten ausgegeben werden
                if len(line) >= 4:
                    print("-" * 40)
                    print(f"Vorname: {line[0]}")   
                    print(f"Nachname: {line[1]}")
                    print(f"Telefon: +{line[2]}")
                    print(f"E-Mail: {line[3]}") 
                else:
                    print("Zeile unvollständig")  

    # Wenn keine Datei existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')

def checkName(name):
    if name != "" and name.replace(" ", "").replace("-", "").isalpha():
        return True
    else:
        return False
    
def checkPhoneNumber(phoneNumber):
    if phoneNumber != "" and phoneNumber.replace(" ", "").replace("+", "").isdigit():
        return True
    else:
        return False
    
def checkEmail(email):
    if email != "" and "@" in email and "." in email:
        return True
    else:
        return False
    

# Kontakt anlegen
def add_new_contact():
    try:
        print("\n" + "=" * 50)
        print("\t\tKONTAKT ANLEGEN")
        print("\n" + "=" * 50)
        print("Bitte gib folgende Informationen ein:")

        # Fragt den User, solange er eine gültige Eingabe macht
        while True: 
            firstNameInput = input("Vorname: ")
            if checkName(firstNameInput):
                firstname = firstNameInput
                break
            else:
                print("Vorname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Vornamen ein.")                

        while True:
            lastNameInput = input("Nachname: ")
            if checkName(lastNameInput):
                lastname = lastNameInput
                break
            else:
                print("Nachname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Nachnamen ein.")

        while True:
            phoneNumberInput = input("Telefonnummer: ")
            if checkPhoneNumber(phoneNumberInput):
                phoneNumber = phoneNumberInput
                break
            else:
                print("Telefonnummer darf nicht leer sein und muss nur Zahlen enthalten. Bitte gib nochmals die Telefonnummer ein. ")
        
        while True:
            emailInput = input("E-Mailadresse: ")
            if checkEmail(emailInput):
                email = emailInput
                break
            else:
                print("E-Mail darf nicht leer sein und muss ein gültiges Format haben (@ und .). Bitte gib nochmals die E-Mailadresse ein.")

        contact = {
            'Vorname': firstname + ';',
            'Name': lastname + ';',
            'Telefon': phoneNumber + ';',
            'E-Mail': email + '\n'
        }
        write_to_file(contact)
        print("\n Kontakt erfolgreich hinzugefügt.")
    except Exception as e:
        print(f'Kontakt konnte nicht hinzugefügt werden: {e}')


def search_contact():
    try:
        with open('contacts.csv', 'r', encoding='utf-8') as file:

            # Ganze CSV ausgeben als Liste
            reader = csv.reader(file, delimiter=';')

            # Ignoriert header (erste Zeile) im CSV 
            next(reader, None)
                
            # Loopt durch die Listen
            for line in reader:
                # Sicherstellen, dass alle Spalten ausgegeben werden
                if len(line) >= 4:
                    # Konvertiert in tuple
                    line = tuple(line)
                    #print(line[0:2])
                    # Setzt Vor- und Nachname zusammen
                    fullname = ' '.join(line[0:2])
                    print(fullname)
                    #print({line[0:2]})   
                else:
                    print("Zeile unvollständig")  

    # Wenn keine Datei existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')

# Kontakt bearbeiten
def edit_contact():
    # User Input: welcher Kontakt wird bearbeitet
    print("editieren")


# Kontakt löschen
def delete_contact():
    # User Input: welcher Kontakt wird gelöscht
    # IF statement
    search_contact()

# In die Datei schreiben 
def write_to_file(contact):
    # with csv
    # Panda Auskommentiert
    #df = pandas.read_csv('daten.csv', sep=';')
    try: 
        with open('contacts.csv', 'a', encoding='utf-8') as file:
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
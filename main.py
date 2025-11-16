# Importiert CSV-Modul
import csv

# Kontakte anzeigen
def display_contacts():
    try: 
        # Öffnet Datei im Lesemodus
        with open('contacts.csv', 'r', encoding='utf-8') as file:

            # Liest alle Zeilen ein
            reader = csv.reader(file, delimiter=';')

            # Ignoriert header (erste Zeile) im CSV 
            next(reader, None)
            
            # Für den Terminal Output 
            print('\n' + '=' * 50)
            print('\t\tMEINE KONTAKTE')
            print('\n' + '=' * 50)

            # Die Liste von a-z sortieren (nach Vornamen)  
            sorted_list = sorted(reader, key=lambda x: x[0])
            reader = sorted_list

            # Loopt durch die Kontakte
            for line in reader:
                # Sicherstellen, dass min. 4 Spalten vorhanden sind
                if len(line) >= 4:
                    print('-' * 40)
                    print(f'Vorname: {line[0]}')   
                    print(f'Nachname: {line[1]}')
                    print(f'Telefon: +{line[2]}')
                    print(f'E-Mail: {line[3]}') 
                else:
                    print('Zeile unvollständig.')  

    # Wenn keine Datei existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')

# Prüft, ob der Name nicht leer, nur aus Buchstaben besteht 
def checkName(name):
    if name != "" and name.replace(" ", "").replace("-", "").isalpha():
        return True
    else:
        return False

# Prüft, ob die Nummer nicht leer ist, nur aus Ziffern besteht
def checkPhoneNumber(phoneNumber):
    if phoneNumber != "" and phoneNumber.replace(" ", "").replace("+", "").isdigit():
        return True
    else:
        return False

# Prüft, ob die E-Mail nicht leer ist, ein @-Zeichen und Punkt (.) enthält  
def checkEmail(email):
    if email != "" and "@" in email and "." in email:
        return True
    else:
        return False
    

# Kontakt anlegen
def add_new_contact():
    try:

        # Output für den Terminal
        print('\n' + '=' * 50)
        print('\t\tKONTAKT ANLEGEN')
        print('\n' + '=' * 50)
        print('Bitte gib folgende Informationen ein: ')

        # Fragt den User, bis er eine gültige Eingabe macht
        while True: 
            firstNameInput = input('Vorname: ')
            if checkName(firstNameInput):
                firstname = firstNameInput
                break
            else:
                print('Vorname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Vornamen ein.')                

        while True:
            lastNameInput = input('Nachname: ')
            if checkName(lastNameInput):
                lastname = lastNameInput
                break
            else:
                print('Nachname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Nachnamen ein.')

        while True:
            phoneNumberInput = input('Telefonnummer: ')
            if checkPhoneNumber(phoneNumberInput):
                phoneNumber = phoneNumberInput
                break
            else:
                print("Telefonnummer darf nicht leer sein und muss nur Zahlen enthalten. Bitte gib nochmals die Telefonnummer ein. ")
        
        while True:
            emailInput = input('E-Mailadresse: ')
            if checkEmail(emailInput):
                email = emailInput
                break
            else:
                print('E-Mail darf nicht leer sein und muss ein gültiges Format haben (@ und .). Bitte gib nochmals die E-Mailadresse ein.')

        # Struktur für den neuen Kontakt-Eintrag ins CSV
        contact = {
            'Vorname': firstname + ';',
            'Name': lastname + ';',
            'Telefon': phoneNumber + ';',
            'E-Mail': email + '\n'
        }
        write_to_file(contact)
        print('\n Kontakt wurde erfolgreich hinzugefügt.')
    except Exception as e:
        print(f'Kontakt konnte nicht hinzugefügt werden: {e}')


def search_contact(contact):
    try:
        with open('contacts.csv', 'r', encoding='utf-8') as file:

            # Liest alle Zeilen ein
            reader = csv.reader(file, delimiter=';')

            # Ignoriert header (erste Zeile) im CSV 
            next(reader, None)
                
            # Loopt durch die Kontakte
            for line in reader:
                # Sicherstellen, dass min. 4 Spalten vorhanden sind
                if len(line) >= 4:
                    # Setzt Vor- und Nachname zusammen
                    fullname = ' '.join(line[0:2]).lower()
                    # Vergleicht den CSV-Eintrag mit dem User-Input
                    if fullname == contact:
                        print(f'Kontakt gefunden: {fullname}')
                        # Ganze CSV-Zeile ausgeben
                        csv_entry = line
                        print(csv_entry)
                        return csv_entry
            else:
                print(f'Kontakt nicht gefunden: {contact}')  
                return None  
           
    # Wenn keine Datei existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')

# Kontakt bearbeiten
def edit_contact():
    try:
        # User Input: welcher Kontakt wird bearbeitet
        contact = input('Gib den Vor- und Nachnamen des Kontakts zur Bearbeitung ein: ').lower()
        found_contact = search_contact(contact)
    
        # Output für Konsole
        print('\n' + '=' * 50) 
        print('\t\tKONTAKT BEARBEITEN')
        print('\n'+ '=' * 50)

        if found_contact:
            print('Gib die neuen Informationen ein (leer lassen, um den aktuellen Wert beizubehalten): ')

            # User Input: Eingabe eines neuen Wertes oder Beibehaltung des Wertes
            while True:
                newFirstname = input(f'Vorname ({found_contact[0]}): ') or found_contact[0]
                if (checkName(newFirstname)):
                    newFirstname = newFirstname
                    break
                else:
                    print('Vorname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Vornamen ein.')   

            while True:
                newLastname = input(f'Nachname ({found_contact[1]}): ') or found_contact[1]
                if (checkName(newLastname)):
                    newLastname = newLastname
                    break
                else:
                    print('Nachname darf nicht leer sein und darf nur Buchstaben beinhalten. Bitte gib nochmals den Nachnamen ein.') 


            while True:
                newPhone = input(f'Telefon ({found_contact[2]}): ') or found_contact[2]
                if (checkPhoneNumber(newPhone)):
                    newPhone = newPhone
                    break
                else:
                    print('Telefonnummer darf nicht leer sein und muss nur Zahlen enthalten. Bitte gib nochmals die Telefonnummer ein. ')

            while True:
                newEmail = input(f'E-Mail ({found_contact[3]}): ') or found_contact[3]
                if (checkEmail(newEmail)):
                    newEmail = newEmail
                    break
                else:
                    print('E-Mail darf nicht leer sein und muss ein gültiges Format haben (@ und .). Bitte gib nochmals die E-Mailadresse ein.')

            # Struktur der Liste vorgeben
            updated_contact = [newFirstname, newLastname, newPhone, newEmail]

            # Datei öffnen zum Lesen
            with open('contacts.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                lines = list(reader)

            # Datei öffnen zum Schreiben
            with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                # Loopt durch die Kontakte
                for line in lines:
                    if line == found_contact:
                        # Überschreibt die CSV mit dem Updated (veränderten) Kontakt
                        writer.writerow(updated_contact)
                    else:
                        # Die orginale Zeile wird geschrieben
                        writer.writerow(line)

            print('Kontakt wurde erfolgreich aktualisiert.')
    # Wenn Datei nicht existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')


# Kontakt löschen
def delete_contact():
    try:
        # User Input: welcher Kontakt wird gelöscht
        contact = input('Gib den Vor- und Nachnamen des Kontakts zur Löschung ein: ').lower()
        found_contact = search_contact(contact)

        # Output für Konsole
        print("\n" + "=" * 50)
        print("\t\tKONTAKT LÖSCHEN")
        print("\n" + "=" * 50)

        if found_contact:
            while True:
                confirm = input(f'Dieser Kontakt: {found_contact} wird gelöscht. Möchten Sie fortfahren? (j/n): ').lower()
                # Bestätigung der User abholen
                if confirm == 'j':
                    # Öffnet Datei im Lesemodus 
                    with open('contacts.csv', 'r', encoding='utf-8') as file:
                        # Liest alle Zeilen ein
                        reader = csv.reader(file, delimiter=';')
                        # Alle Zeilen speichern 
                        lines = list(reader)         
                    # Datei öffnen zum Schreiben
                    with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file, delimiter=';')
                        # Überschreibt die Datei mit den restlichen Einträgen
                        for line in lines:
                            if line != found_contact:
                                writer.writerow(line)
                    print('Kontakt wurde erfolgreich gelöscht.')
                    break
                elif confirm == 'n':
                    print('Kontakt wurde nicht gelöscht.')
                    break
                else:
                    print("Ungültige Eingabe! Bitte wählen Sie (j) oder (n).")
                    continue
    # Wenn Datei nicht existiert
    except FileNotFoundError as e:
        print(f'Datei nicht gefunden: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')


# In die Datei schreiben 
def write_to_file(contact):
    try: 
        # Neue Kontakte werden angehängt 
        with open('contacts.csv', 'a', encoding='utf-8') as file:
            for entry in contact:
                file.write(contact[entry])
    except Exception as e:
        print(f'Fehler: {e}')


# Menu
def show_menu():
    while True:
        print('\n' + '*'*40)
        print('\t\tKontaktbuch')
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
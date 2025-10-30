import pandas

# Notizen Sena -> Ich glaube das Modul CSV ist besser für z.B einzelne Spalten (Name) auszugeben
# Importiert CSV-Modul
import csv

# Kontakte anzeigen
def display_contacts():
    try: 
        with open('contacts.csv', 'r', encoding='utf-8') as file:
            # Zum Testen
            print(f"Datei erfolgreich geöffnet: {file}")

            # Ganze CSV ausgeben als Liste
            reader = csv.reader(file, delimiter=';')
            
            # Für den Terminal Output # wird noch angepasst
            print("\n" + "=" * 50)
            print("\tMEINE KONTAKTE")
            print("\n" + "=" * 50)

            # https://ingo-janssen.de/csv-dateien-lesen-mit-python/
            for line in reader:
                # Sicherstellen, dass alle Spalten ausgegeben werden
                if len(line) <= 4:
                    print("-" * 40)
                    print(f"Vorname: {line[0]}")   
                    print(f"Nachname: {line[1]}")
                    print(f"Telefon: +{line[2]}")
                    print(f"E-Mail: {line[3]}") 
                else:
                    print("landet hier")  

    # Wenn keine Datei existiert
    except FileNotFoundError as e:
        print(f'Datei existiert nicht: {e}')
    except Exception as e:
        print(f'Fehlermeldung: {e}')



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
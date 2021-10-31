# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("...\contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("...\contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")
    write_database(db)
    sumNums(db)

def add_kon(db):
    print("Enter the contact's first and last name:")
    name = input("> ")
    print("Enter the contact's phone number:")
    phone = input("> ")
    print("Enter the age of the contact:")
    age = input("> ")
    print("Enter contact email:")
    email = input("> ")
    new_db = (name, phone, age, email)
    db.append(new_db)
    write_database(db)
    print("Contact added and saved")
    

def edit(db):
    row = int(input("Row ->"))
    column = int(input("Column (Enter number: 0 - Name, 1 - Phone, 2 - Age, 3 - Email) -> "))
    new_contact = input("New contact -> ")
    db[row][column] = new_contact
    write_database(db)

def remove(db):
    row = int(input("Row to removing -> "))
    db[row] = ""
    write_database(db)

def sumNums(db):
    with open('...\contacts.txt', 'r') as db:
        count = i = 0
        for line in db:
            name, phone, age, email = line.split(',')
            if age.strip().isdigit():
                count += int(age)
            i += 1
        print("Средний возраст", count / i)


def print_out_commands(db):
    print("Commands are:")
    print("1. list ")
    print("2. edit ")
    print("3. add ")
    print("3. remove ")
    while True:
        command = input("What is your command?: ")
        if command == 'list':
            print_out_database(db)
        elif command == 'edit':
            edit(db)
        elif command == 'add':
            add_kon(db)
        elif command == 'remove':
            remove(db)
        else:
            print("There is no such command")



def main():
    db = read_database()
    print_out_database(db)
    print_out_commands(db)
    
    
main()

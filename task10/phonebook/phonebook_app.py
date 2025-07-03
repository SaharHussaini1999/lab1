import csv
from db_connect import connect


# A - insert from the csv file


def insert_from_csv(csv_file):
    conn = connect()
    cur = conn.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data from CSV inserted.")
    cur.close()
    conn.close()

# B - insert from the console


def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted successfully.")
    cur.close()
    conn.close()

# 3 - UPDATE DATA


def update_phone_by_name():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter the name to update: ")
    new_phone = input("Enter new phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s",
                (new_phone, name))
    conn.commit()
    print("Updated successfully.")
    cur.close()
    conn.close()

# 4 - QUERY WITH FILTERS


def query_by_name():
    conn = connect()
    cur = conn.cursor()
    prefix = input("Enter name prefix: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (prefix + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 5 - Delete by Name or Phone


def delete_by_name():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    print("Deleted successfully.")
    cur.close()
    conn.close()


def delete_by_phone():
    conn = connect()
    cur = conn.cursor()
    phone = input("Enter phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Deleted successfully.")
    cur.close()
    conn.close()

# 6 - Main Menu


def main():
    while True:
        print("""
        1. Insert from console
        2. Insert from CSV
        3. Update phone by name
        4. Query by name
        5. Delete by name
        6. Delete by phone
        0. Exit
        """)
        choice = input("Choose option: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            csv_file = input("Enter CSV file path: ")
            insert_from_csv(csv_file)
        elif choice == '3':
            update_phone_by_name()
        elif choice == '4':
            query_by_name()
        elif choice == '5':
            delete_by_name()
        elif choice == '6':
            delete_by_phone()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

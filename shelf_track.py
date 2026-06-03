# CAPSTONE PROJECT - SHELF TRACKER 
import sqlite3
import os
# Creating database file connection and cursor object
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

# Funtions
def show_error():
    print("Invalid ID, please ensure you entered the right format (####)")
    
def add_book(id,title,authorID,qty):
    cursor = db.cursor()
    new_book = [id, title, authorID, qty]
    cursor.execute(
        '''
        INSERT INTO book (id, title, authorID, qty)
        VALUES (?,?,?,?)
        ''', new_book
    )
    db.commit()
    os.system("clear")
    print("\n  New book added succesfully! ")

def search_and_show(book_id):
    cursor = db.cursor()
    cursor.execute(
        '''
        SELECT id, title, authorID, qty
        FROM book
        WHERE id = ? 
        ''',(book_id,)
    )
    db.commit()
    found_book = cursor.fetchone()
    print(found_book)
    if found_book:
        print(f"\n Book {book_id} found: \n ")
        print(
            f'''
            \t ID:             {found_book[0]}
            \t Title:          {found_book[1]}
            \t Author ID:      {found_book[2]}
            \t Quantity:       {found_book[3]} 
            '''
        )
        return 1
    else:
        return 0

def update_qty(book_id):
    print("- - - - - - UPDATING EXISTENCE - - - - - ")
    while True:
        try:
            new_quantity = int(input("Quantity: "))
            if new_quantity >= 0:
                break
            else:
                print("Error. Quantity must be natural number. ")
        except TypeError:
            break
    cursor = db.cursor()
    cursor.execute(
        '''
        UPDATE book
        SET qty = ?
        WHERE id = ?
        ''', (new_quantity,book_id)
    )
    db.commit()
    print("\n  Book Updated succesfully! ")


def edit_author_id(book_id):
    print("- - - - - - Editing Author ID - - - - - ")
    while True:
        new_author_id = input("New Author ID: ")
        try:
            if len(new_author_id) == 4:
                edited_author_id = int(new_author_id)
                break
            else:
                show_error()
        except TypeError:
            print("Invalid entry. Try again. ")
    cursor = db.cursor()
    cursor.execute(
        '''
        UPDATE book
        SET authorID = ?
        WHERE id = ?
        ''', (edited_author_id,book_id)
    )
    db.commit()
    os.system("clear")
    print("\n  Author ID Edited succesfully! ")
    return edited_id


def edit_title(book_id):
    print("- - - - - - Editing TITLE - - - - - ")
    edited_title = input("New Title: ")
    cursor = db.cursor()
    cursor.execute(
        '''
        UPDATE book
        SET title = ?
        WHERE id = ?
        ''', (edited_title,book_id)
    )
    db.commit()
    os.system("clear")
    print("\n  Book TITLE Edited succesfully! ")

def delete_book(book_id):
    cursor.execute(
        '''
        DELETE FROM book
        WHERE id = ?
        ''', (book_id,)
    )
    db.commit()
    os.system("clear")
    print(f" Book {book_id} has been deleted succesfully. ")

# Create Table 'book'
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        authorID INTEGER,
        qty INTEGER
    )
    '''
)
db.commit()
#print("Table created")

# Defining data for the table 

books_info = [
    (3001, 'A Tale of Two Cities', 1290, 30),
    (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
    (3004, 'The Lord of the Rings', 6380, 37),
    (3005, "Alice's Adventures in Wonderland", 5620, 12)
]

cursor.executemany(
    '''
    INSERT INTO book (id, title, authorID, qty)
    VALUES (?,?,?,?)
    ''', books_info
)

db.commit()


# Displaying Menu

while True:
    print(
        '''
        \t WELCOME TO YOUR BOOKSTORE DATABASE

        1. Enter book
        2. Update book
        3. Delete book 
        4. Search book 
        0. Exit  
        '''
    )
    menu = input("Enter (0 ~ 5): ")

    if menu == "1":
        os.system("clear")
        print(" - - - - - - - - -  Adding new Book - - - - - - - - - - ")
        while True: 
            new_id = input("Book ID: ")
            if len(new_id) == 4:
                try:
                    newer_id = int(new_id)
                    break
                except TypeError:
                    print("Invalid entry (Numbers only). Try again. ")
            else:
                show_error()
        new_title = input("Title: ")
        while True:
            new_authorID = input("Author ID: ")
            if len(new_authorID) == 4:
                try:
                    newer_authorID = int(new_authorID)
                    break
                except Exception:
                    print("Invalid entry (Numbers only). Try again. ")
            else:
                show_error()

        while True:
            try:
                new_qty = int(input("Quantity: "))
                if new_qty > 0:
                    break
                else:
                    print("Error. Quantity must be natural number. ")
            except Exception:
                break
        add_book(newer_id,new_title,newer_authorID,new_qty)


    elif menu == "2":
        os.system("clear")
        print("- - - - - - - - - - Updating book - - - - - - - - - - - ")
        while True:
            update_target = int(input("Enter book ID you wish to update: "))
            search_and_show(update_target)
            if search_and_show(update_target) == 0:
                print(f"Book with ID {update_target} was not found. Verify Book ID again")
                continue
            break

        update_qty(update_target)
        while True:
            opc_2 = input(
                """ 
                Do you need to make more changes to the current Book?
                1. Edit Title 
                2. Edit Author ID
            
                0 to return
                """
            )
            if opc_2 == "1":
                edit_title(update_target)
            elif opc_2 == "2":
                edit_author_ID(update_target)
            elif opc_2 == "0":
                break
            else:
                print("Invalid option")

    elif menu == "3":
        os.system("clear")
        print("- - - - - - - - - - -  Deleting Book - - - - - - - ")
        while True:
            delete_target = int(input("Enter book ID you wish to delete: "))
            search_and_show(delete_target)
            if search_and_show(delete_target) == 0:
                print(f"Book with ID {update_target} was not found. Verify Book ID again")
                continue
            break

        delete_book(delete_target)

    elif menu == "4":
        print("- - - - - - - - - - Searching Books - - - - - - - - - - -")
        while True:
            target = int(input("Enter book ID you want to search: "))
            search_and_show(target)
            if search_and_show(target) == 0:
                print(f"Book with ID {target} was not found. Verify Book ID again")
                continue
            break

    else:
        os.system("clear")

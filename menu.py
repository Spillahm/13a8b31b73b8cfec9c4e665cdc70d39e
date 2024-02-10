"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
#sqlite database connection;
db = 'records.db'
# create database table OR set up Peewee model to create table

with sqlite3.connect(db) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, name TEXT UNIQUE )")
def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    with sqlite3.connect(db) as conn:

        #cursor to execute queries
        cursor = conn.execute('SELECT * FROM records')
        records = cursor.fetchall() # to retrive or show all records , if you want one use fetchone
        print('All records')

    for row in records:
        print(row)



def search_by_name():
    name = input('Enter name look for')
    with sqlite3.connect(db) as conn:
        cursor = conn.execute('SELECT * FROM records WHERE name = ?', (name,))
        record = cursor.fetchone() # the fetchone gets one record from the rest of the records availbale
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')


def add_new_record():
    new_id = int(input('Enter new id: '))
    new_name = input('Enter a new record: ')

    with sqlite3.connect(db) as conn:
        try:
            conn.execute(f'INSERT INTO records VALUES (?, ?)', (new_id, new_name))
            print('record added')
        except:
             print('record already exists')



def edit_existing_record():
    new_name = input('Enter a new name: ')
    update_id = int(input('Enter id for record to be editted: '))

    with sqlite3.connect(db) as conn:
        cursor = conn.execute('UPDATE records SET name = ? WHERE id = ?',(new_name, update_id) )
        if cursor.rowcount > 0: # the if statement to record to be editted exists if not returns error message
            print(f'record  with {update_id} was editted')
        else:
            print(f'record with {update_id} was not found')


    #print('todo edit existing record. What if user wants to edit record that does not exist?')


def delete_record():
    record_name = input('Enter name of the record to delete:')
    with sqlite3.connect(db) as conn:
        cursor = conn.execute('DELETE from RECORDS WHERE name = ?', (record_name,))

        if cursor.rowcount > 0: # checks if record to be delteted is available by lookinf for record name
            print(f'record {record_name} was deleted')
        else:
            print(f'record {record_name} does not exists in records')


   # print('todo delete existing record. What if user wants to delete record that does not exist?')
    conn.close()

if __name__ == '__main__':
    main()
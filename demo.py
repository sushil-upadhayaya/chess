# import sqlite3
# conn=sqlite3.connect('data.db')
# c=conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement,name text,age integer, email text)')
# conn.commit()
# conn.close()
# name=input("ennter the name")
# age=int(input('enter the age'))
# email=input('enter the email')
# # c.execute('select * from users')# 
# rows=c.fetchall()
# conn.close()

# for row in rows:
#     print(row)
# c.execute('update users set name=? where id=?', (name,email))
# conn.commit()
# conn.close()
# c.execute
# conn.commit()
# conn.close()
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a simple table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()

# CRUD Functions

def add_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"User {name} added successfully!")

def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    print(f"User {user_id} updated successfully!")

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"User {user_id} deleted successfully!")

def display_users():
    users = get_all_users()
    if not users:
        print("No users found.")
    else:
        print("\nUsers in the database:")
        for user in users:
            print(f"ID: {user[0]} | Name: {user[1]} | Age: {user[2]}")
    print()
    
def main():
    while True:
        print("==== Database CLI ====")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            # Add User
            name = input("Enter user name: ")
            age = input("Enter user age: ")
            if age.isdigit():
                add_user(name, int(age))
            else:
                print("Invalid age. Please enter a number.")
        
        elif choice == '2':
            # View Users
            display_users()

        elif choice == '3':
            # Update User
            user_id = input("Enter user ID to update: ")
            if user_id.isdigit():
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                if age.isdigit():
                    update_user(int(user_id), name, int(age))
                else:
                    print("Invalid age. Please enter a number.")
            else:
                print("Invalid ID. Please enter a valid user ID.")
        
        elif choice == '4':
            # Delete User
            user_id = input("Enter user ID to delete: ")
            if user_id.isdigit():
                delete_user(int(user_id))
            else:
                print("Invalid ID. Please enter a valid user ID.")

        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()

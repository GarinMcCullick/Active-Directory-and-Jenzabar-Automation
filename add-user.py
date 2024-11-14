# add-user.py

import sys

def add_user_to_system(name, email):
    # Here, you can add logic to store the user data, e.g., in a file or a database.
    with open('user_data.txt', 'a') as f:
        f.write(f'Name: {name}, Email: {email}\n')

if __name__ == '__main__':
    name = sys.argv[1]
    email = sys.argv[2]
    add_user_to_system(name, email)

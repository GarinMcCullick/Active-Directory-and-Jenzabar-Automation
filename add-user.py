import sys

# Function to add user data to the system
def add_user_to_system(firstname, initial, lastname, password, login_name, email, jenzabar_id, department):
    # Here, you can add logic to store the user data, e.g., in a file or a database.
    with open('user_data.txt', 'a') as f:
        f.write(f'Firstname: {firstname}, Initial: {initial}, Lastname: {lastname}, '
                f'Password: {password}, Login Name: {login_name}, Email: {email}, '
                f'Jenabar ID: {jenzabar_id}, Department: {department}\n')

if __name__ == '__main__':
    # Fetching arguments passed via the command line
    firstname = sys.argv[1]
    initial = sys.argv[2]
    lastname = sys.argv[3]
    password = sys.argv[4]
    login_name = sys.argv[5]
    email = sys.argv[6]
    jenzabar_id = sys.argv[7]
    department = sys.argv[8]

    # Call the function to add the user
    add_user_to_system(firstname, initial, lastname, password, login_name, email, jenzabar_id, department)

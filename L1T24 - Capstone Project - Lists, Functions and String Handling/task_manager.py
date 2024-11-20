import datetime

#====Login Section====
with open('user.txt', 'r') as read:
    login_userandpass = read.readlines()

list_login = []

for i in login_userandpass:
    list_login = i.strip().split(', ')

username = input('Enter your username: ')
password = input('Enter your password: ')
login = f'{username}, {password}'

username_correct = list_login[0]
password_correct = list_login[1]
login_correct = f'{username_correct}, {password_correct}'

while login != login_correct:
    print('Incorrect login details, please try again.')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    login = f'{username}, {password}'
    username_correct = list_login[0]
    password_correct = list_login[1]
    login_correct = f'{username_correct}, {password_correct}'

print('Welcome! You are logged in.')

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Main menu
while True:
    menu = input('''Select one of the following options:
r - Register a user
a - Add task
va - View all tasks
vm - View my tasks
s - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        if username != 'admin':
            print("Only the admin user is allowed to register new users.")
        else:
            new_user = input('Enter a new username: ')
            new_pass = input('Enter a new password: ')
            confirm_pass = input('Confirm your password: ')
            
            while new_pass != confirm_pass:
                print('Passwords do not match, try again.')
                new_pass = input('Enter a new password: ')
                confirm_pass = input('Confirm your password: ')
            
            with open('user.txt', 'a') as file:
                file.write(f'{new_user}, {new_pass}\n')
                print(f'User "{new_user}" registered successfully.')
    
    elif menu == 'a':
        user = input('Who will be the user assigned to this task? ')
        title = input('What is the title of the task? ')
        description = input('What is the description of the task? ')
        
        due = input('What is the due date of the task (YYYY-MM-DD)? ')
        while not validate_date(due):
            print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
            due = input('What is the due date of the task (YYYY-MM-DD)? ')
        
        date = input('What is the current date (YYYY-MM-DD)? ')
        while not validate_date(date):
            print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
            date = input('What is the current date (YYYY-MM-DD)? ')
        
        no = 'NO'
        
        with open('tasks.txt', 'a') as new_task:
            new_task.write(f'{user}, {title}, {description}, {due}, {date}, {no}\n')
            print('Task added successfully.')
    
    elif menu == 'va':
        with open('tasks.txt', 'r') as output:
            for line in output:
                parts = line.strip().split(', ')
                print(f"Task: {parts[1]}\nAssigned to: {parts[0]}\nDate assigned: {parts[4]}\nDue date: {parts[3]}\nTask complete: {parts[5]}\nDescription: {parts[2]}\n{'-'*40}")
    
    elif menu == 'vm':
        with open('tasks.txt', 'r') as current:
            for line in current:
                parts = line.strip().split(', ')
                if parts[0] == username:
                    print(f"Task: {parts[1]}\nAssigned to: {parts[0]}\nDate assigned: {parts[4]}\nDue date: {parts[3]}\nTask complete: {parts[5]}\nDescription: {parts[2]}\n{'-'*40}")
    
    elif menu == 's':
        total_tasks = sum(1 for _ in open('tasks.txt'))
        with open('user.txt', 'r') as user_file:
            total_users = sum(1 for _ in user_file)
        print(f"Total number of tasks: {total_tasks}")
        print(f"Total number of users: {total_users}")

    elif menu == 'e':
        print('Goodbye!')
        break

    else:
        print("Invalid input. Please try again.")

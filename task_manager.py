import datetime

def validate_date(date_text, format='%Y-%m-%d'):
    try:
        datetime.datetime.strptime(date_text, format)
        return True
    except ValueError:
        return False

def get_current_date():
    return datetime.datetime.today().strftime('%Y-%m-%d')

def load_users():
    users = {}
    try:
        with open('user.txt', 'r') as file:
            for line in file:
                user, passw = line.strip().split(', ')
                users[user] = passw
    except FileNotFoundError:
        print("User file not found. Please ensure 'user.txt' is in the correct location.")
    return users

def load_tasks():
    tasks = []
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip().split(', '))
    except FileNotFoundError:
        print("Task file not found. Please ensure 'tasks.txt' is in the correct location.")
    return tasks

users = load_users()

#====Login Section====
username = input('Enter your username: ')
password = input('Enter your password: ')

while users.get(username) != password:
    print('Incorrect login details, please try again.')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

print('Welcome! You are logged in.')

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
        
        date = get_current_date()
        
        no = 'No'
        
        with open('tasks.txt', 'a') as new_task:
            new_task.write(f'{user}, {title}, {description}, {due}, {date}, {no}\n')
        print('Task added successfully.')
    
    elif menu == 'va':
        tasks = load_tasks()
        for task in tasks:
            print(f"Task: {task[1]}\nAssigned to: {task[0]}\nDate assigned: {task[4]}\nDue date: {task[3]}\nTask complete: {task[5]}\nDescription: {task[2]}\n{'-'*40}")
    
    elif menu == 'vm':
        tasks = load_tasks()
        for task in tasks:
            if task[0] == username:
                print(f"Task: {task[1]}\nAssigned to: {task[0]}\nDate assigned: {task[4]}\nDue date: {task[3]}\nTask complete: {task[5]}\nDescription: {task[2]}\n{'-'*40}")
    
    elif menu == 's':
        if username != 'admin':
            print("Only the admin user is allowed to view statistics.")
        else:
            total_tasks = len(load_tasks())
            total_users = len(users)
            print(f"Total number of tasks: {total_tasks}")
            print(f"Total number of users: {total_users}")

    elif menu == 'e':
        print('Goodbye!')
        break

    else:
        print("Invalid input. Please try again.")


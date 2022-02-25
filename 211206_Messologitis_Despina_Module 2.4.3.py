contacts = {}

def command_add(name, email, phone):
    contact = [name, email, phone]
    contact_name = contact[0]
    if len(contacts) == 0:
        current_key = 1
    else:
        max_key = max(contacts, key=contacts.get)
        current_key = max_key + 1
    contacts[current_key] = contact
    print(f'{contact_name} was added.')

def command_del(contact_key):
    contact_name = contacts[contact_key][0]
    contacts.pop(contact_key)
    print(f'{contact_name} was deleted.')


def command_display():
    for k, v in contacts.items():
        print(k, v[0])

def command_view(contact_key):
    contact_name = contacts[contact_key][0]
    contact_email = contacts[contact_key][1]
    contact_phone = contacts[contact_key][2]
    print('Name:', contact_name)
    print('Email: ', contact_email)
    print('Phone: ', contact_phone)

# command_add('jen','j@','22')
# command_add('ken','k@','22')
# command_add('ben','b@','22')
# command_display()
# command_view(1)
#


print('COMMAND MENU\n'
      'list - Display all contacts\n'
      'view - View a contact\n'
      'add - Add a contact\n'
      'del - Delete a contact\n'
      'exit - Exit program\n')

command_list = ['list', 'view', 'add', 'del', 'exit']

command = input('Select a command: ')

if command == 'exit':
    i = 0
    print('Bye!')
elif command not in command_list:
    cont = input('Command does not exist. Would you like to continue? y/n ')
    if cont == 'y':
        i = 1
        command = input('Select a command: ')
    else:
        i = 0
        print('Bye!')
else:
    i = 1

while i > 0:

    if command == 'list':
        if len(contacts) == 0:
            print('No contacts exist.')
        else:
            command_display()
    elif command == 'view':
        contact_key = int(input('Select contact number to view: '))
        if contact_key not in contacts:
            print('Contact does not exist.')
        else:
            command_view(contact_key)
    elif command == 'del':
        contact_key = int(input('Select contact number to delete: '))
        if contact_key not in contacts:
            print('Contact does not exist.')
        else:
            command_del(contact_key)
    elif command == 'add':
        name = input('Name: ')
        email = input('Email: ')
        phone = input('Phone: ')
        command_add(name, email, phone)
    elif command == 'exit':
        i = 0
        print('Bye!')
    elif command not in command_list:
        cont = input('Command does not exist. Would you like to continue? y/n ')
        if cont == 'y':
            i = 1
        else:
            i = 0
            print('Bye!')

    if i != 0:
        command = input('\nSelect a command: ')
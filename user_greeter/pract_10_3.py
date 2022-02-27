import greeter

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    username = greeter.Greeter()
    username = username.get_name_from_user()
    file_object.write(f'{username} \n')

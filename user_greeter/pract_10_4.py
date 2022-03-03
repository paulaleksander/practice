import greeter

filename = 'guest_book.txt'

with open(filename, 'a') as file_object:

    while True:
        print('Introduce yourself!')
        print('\t type "q" to leave.')
        username = greeter.Greeter()
        username = username.get_name_from_user()
        if username == None:
            break       
        file_object.write(f'{username} \n')
        print(f'\n\t Hello {username}!')
        
        break        

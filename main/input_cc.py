

def get_role():
    role = input('What do you wish your role to be for the code clinic? ').lower()
    roles = ['doctor', 'patient']
    while len(role) == 0 or role not in roles:
        print('\nYou can either choose to be a \n(1) Doctor or \n(2) Patient.')
        role = input('What do you wish your role to be for the code clinic? ').lower()
    print('Role stored successfully.')
    return role

def get_username():
    username = input("Please enter your username: ")
    if len(username) == 0:
        username = input("Please enter your username: ")
    print(f'Welcome {username}!')
    return


def get_date():
    chosen_date = input('Book a slot in the format dd-mm-yyyy: ')
    chosen_time = input('Book a time slot in the format hh:mm: ')
    chosen_date = chosen_date.split('-')
    chosen_date = [int(i) for i in chosen_date]
    x = datetime.datetime(chosen_date[2], chosen_date[1], chosen_date[0])
    picked_date = x.strftime("%A %d %B")
    print('Timne slot created for:', chosen_time, picked_date)
    return picked_date



if __name__ == "__main__":
    import datetime
    get_role()
    get_username()
    picked_date = get_date()
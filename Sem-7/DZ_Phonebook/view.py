def GetNewPhone():
    first_name = input('Enter name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone: ')
    discrioption = input('Description')
    new_phone = dict
    new_phone[phone_number] = [first_name, last_name, discrioption]
    return new_phone

def GetUserChoice():
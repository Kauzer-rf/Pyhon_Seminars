def GetNewPhone():
    first_name = input('Enter name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone: ')
    discrioption = input('Description')
    new_phone = dict()
    new_phone[phone_number] = [first_name, last_name, discrioption]
    return new_phone

def GetUserChoice():
    return input('Chhose one:\n1. Add new number\n2. Import file\n3. Export file\n4. Exit')

def GetFilePath():
    return input('Enter path to the file')

def GetExportFileType():
    return input('Select file type: \n1. csv\n2. txt\n')

def GetDataType(message):
    print('1. Last_Name_1;First_Name_1;Phone_1;Description_1')
    print('   Last_Name_2;First_Name_2;Phone_2;Description_2')
    print()
    print('2. Last_name_1')
    print('   First_Name_1')
    print('   Phone_1')
    print('   Description_1')
    print()
    print('   Last_name_2')
    print('   First_Name_2')
    print('   Phone_2')
    print('   Description_2')
    return input(f'Choose the type of data you want to {message}')
import logger

def ExportContactsInCSV(path, file_name, contacts):
    with open(path + file_name, 'w') as file:
        file.write(f'First Name;Last Namel Phone Number;Description\n')
        for i in contacts:
            file.writelines(f"{contacts[i]['First Name']}; {contacts[i]['Last Name']};{i};{contacts[i]['Description']}\n")
    logger.Log('Export completed.')

def ExportContactsInTXTColumns(path, contacts):
    with open(path + '\contacts.csv', 'w') as file:
        file.write(f"First Name;Last Name;Phone Number; Description\n")
        for i in contacts:
            file.write(f"First Name: {contacts[i]['First Name']}\n")
            file.write(f"Last Name: {contacts[i]['Last Name']}\n")
            file.write(f"Phone Number: {i}\n")
            file.write(f"Description: {contacts[i]['Description']}\n")
    logger.Log('Export completed')

def SaveData(phonebook):
    with open('Sem-7\DZ_Phonebook\PBData.txt', 'w') as file:
        for i in phonebook:
            file.writelines(f"{phonebook[i]['First Name']}; {phonebook[i]['Last Name']};{i};{phonebook[i]['Description']}\n")
    logger.Log('Data saved')

def GetDataFromRows(path):
    with open(path, 'r') as file:
        pb = file.readlines()
    print(pb)
    new_pb = {}
    new_temp = {}
    for element in pb:
        temp = element.replace('\n','').split(';')
        print(temp)
        pb_key = temp[0]
        new_temp['First Name'] = temp[1]
        new_temp['Last Name'] = temp[2]
        new_temp['Description'] = temp[3]
        print(new_temp)
        new_pb[pb_key] = new_temp
    return new_pb

def MatchingNumbers(phonebook, new_phones):
    for key in new_phones:
        overwrite = ''
        if key in phonebook and (overwrite.lower() != 'y+' or overwrite.lower() != 'n+'):
            overwrite = input(f"{key} is already exist as {phonebook[key]['First Name']}{phonebook[key]['Last Name']}.\nDo you want to change it?\nTo change all phones enter Y+.\nTo cancel all changes enter N+\nY/N/Y+/N+")
        if overwrite.lower() == 'n' or overwrite.lower == 'n+':
            logger.log(f'{key} change denied')
        else:
            phonebook[key] = new_phones[key]
            logger.log(f'{key} change completed')

def GetDataFromColumns(path):
    with open(path, 'r') as file:
        temp = file.readlines()
        new_pb = {}
        for i in range (0, len(temp), 5):
            q = []
            for j in range(1,4):
                q.append(temp[j].replace('\n', ''))
            new_pb[temp[i].replace('\n', '')] = q
    logger.Log('Data (rows) copied')
    return new_pb




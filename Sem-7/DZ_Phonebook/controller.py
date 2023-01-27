import view
import functions

def Start():
    current_phonebook = functions.GetData('Sem-7\DZ_Phonebook\PBData.txt')
    stop = False

    while not stop:
        user_choice = view.GetUserChoice()

        if user_choice == '1':
            new_phone = view.GetNewPhone()
            functions.MatchingNumbers(current_phonebook, new_phone)
        elif user_choice == '2':
            path = view.GetFilePath()

            if view.GetDataType('import') -1:
                new_phones = functions.GetDataFromColumns(path)
            else:
                new_phones = functions.GetDataFromRows(path)
            functions.MatchingNumbers(current_phonebook, new_phones)

        elif user_choice == '3':
            path = view.GetFilePath()

            if view.GetExportFileType() - 1:
                if view.GetDataType() - 1:
                    functions.ExportContaactsInTXTColumns(path, current_phonebook)
                else:
                    functions.ExportContactsInCSV(path, '\contacts.txt', current_phonebook)
            else:
                functions.ExportContactsInCSV(path, '\contacts.csv', current_phonebook)
        else:
            stop = False
    functions.SaveData(current_phonebook)        

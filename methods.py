
import Note


def add_note():
    note = create_note()
    f = open('notes.csv','a')
    f.seek(0).write(Note.Note.to_string(note))
    f.close()
    print("The note is saved")
   
def create_note():
    title =input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return Note.Note(title, body)   

def show_all_notes():
    try: 
        with open('notes.csv', 'r') as f:
            print(f.read() + "\n")

    except OSError:
        print("No file")

def delete_note():
    my_dict = {}
    try: 
        with open('notes.csv', 'r') as f:
            for line in f:
                array = line.split(";")
                my_dict.update({array[0]:line})
    except OSError:
        print("No file")

    show_all_notes()

    flag = True
    while(flag):    
        delete_ID = input('Введите ID заметки, которую надо удалить: \n')
        if delete_ID in my_dict:
            my_dict.pop(delete_ID)
            flag = False
        else:
            print("Incorrect ID\n")

    open('notes.csv', 'w').close()

    with open('notes.csv', 'a') as f:
        for key in my_dict:
            f.write(my_dict.get(key))
    print("Note delete\n")

def show_one_note():
    my_dict = {}
    try: 
        with open('notes.csv', 'r') as f:
            for line in f:
                array = line.split(";")
                my_dict.update({array[0]:line})
    except OSError:
        print("No file")

    show_all_notes()

    flag = True
    while(flag):    
        delete_ID = input('Введите ID заметки, которую нужно вывести на экран: \n')
        if delete_ID in my_dict:
            print(my_dict.get(delete_ID))
            flag = False
        else:
            print("Incorrect ID\n")

def redact_note():
    my_dict = {}
    try: 
        with open('notes.csv', 'r') as f:
            for line in f:
                array = line.split(";")
                my_dict.update({array[0]:line})
    except OSError:
        print("No file")

    show_all_notes()

    flag = True
    while(flag):    
        delete_ID = input('Введите ID заметки, которую нужно изменить: \n')
        if delete_ID in my_dict:
            note = create_note()
            my_dict.pop(delete_ID)
            my_dict.update({Note.Note.get_id(note): Note.Note.to_string(note)})
            flag = False
        else:
            print("Incorrect ID\n")

    open('notes.csv', 'w').close()

    with open('notes.csv', 'a') as f:
        for key in my_dict:
            f.write(my_dict.get(key))
    print("Note redact\n")

def date_note():
    count = 0
    date = input('Введите дату в формате dd.mm.yyyy: \n')
    try: 
        with open('notes.csv', 'r') as f:
            for line in f:
                array = line.split(";")
                key = array[3].split(" ")
                if key[0] == date:
                    count+=1
                    print(line)
    except OSError:
        print("No file")
    
    if count ==0:
        print("There is no note with such a date")

    


  

     

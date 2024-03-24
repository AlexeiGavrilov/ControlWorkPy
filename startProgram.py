
import methods as m


def start():
    flag = True
    while(flag):
        print("Введите 1, чтобы показать все заметки\nВведите 2, чтобы добавить заметку\nВведите 3, чтобы удалить заметку\nВведите 4, чтобы редактировать заметку\n" +
              "Введите 5, чтобы вывести на экран одну заметку\nВведите 6, чтобы вывести заметку по дате \nВведите 7, чтобы выйти из программы\n")
        input_from_user = input().strip()
        if input_from_user == '1':
            m.show_all_notes()
        if input_from_user == '2':
            m.add_note()
        if input_from_user == '3':
            m.delete_note()
        if input_from_user == '4':
            m.redact_note()
        if input_from_user == '5':
            m.show_one_note()
        if input_from_user == '6':
            m.date_note()
        if input_from_user == '7':
            print("Работа с программой завершена")
            flag = False











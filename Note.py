import datetime
import uuid


class Note():

    my_dict = {}
    

    def __init__(self, title, body):
        self.id = str(uuid.uuid1())[0:3]
        self.date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.title = title
        self.body = body
        

    def get_id(note):
        return note.id    
    
    def get_date(note):
        return note.date
    

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body
    

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body


    def to_string(note):
        return (f'{note.id};{note.title};{note.body};{note.date}') 

    
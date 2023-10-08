from .exceptions import *

import json
from datetime import datetime, date

class NoteModel:
    '''Модель, содержащая логику работы с JSON файлом заметок'''

    def scan_notes_db(self):
        with open('models/data_base/NotesDB.json', 'r', encoding='UTF-8') as db:
            json_res = json.load(db)

        return json_res

    def save_new_note(self, note_name, note_data, notes_list):
        if len(notes_list['notes']) == 0:
            note_id = 1
        else:
            note_id = max(notes_list['notes'],
                          key=lambda note: note['id'])['id'] + 1

        note_date = str(date.today()) + datetime.now().strftime(' %H:%M:%S')

        notes_list['notes'].append({'id': note_id,
                                    'name': note_name,
                                    'content': note_data,
                                    'date': note_date})

        self.__save_note(notes_list)

    def del_note(self, id, list_notes: dict):
        note_index = self.__find_note(id, list_notes)

        list_notes['notes'].pop(note_index)

        self.__save_note(list_notes)

    def edit_note(self, id, note_name, note_data, note_list):
        note_index = self.__find_note(id, note_list)
        new_note = note_list['notes'][note_index]

        note_date = str(date.today()) + datetime.now().strftime(' %H:%M:%S')
        new_note['name'], new_note['content'], new_note['date'] = note_name, note_data, note_date

        self.__save_note(note_list)

    def show_note(self, id, note_list):
        note_index = self.__find_note(id, note_list)

        return note_list['notes'][note_index]

    @classmethod
    def __save_note(cls, notes_lst):
        with open('models/data_base/NotesDB.json', 'w', encoding='UTF-8') as db:
            json_to_save = json.dumps(notes_lst, indent=4, ensure_ascii=False)
            db.write(json_to_save)

    @classmethod
    def __find_note(cls, id, note_lst):
        for i, note in enumerate(note_lst['notes']):
            if id == note['id']:
                return i

        raise IdException

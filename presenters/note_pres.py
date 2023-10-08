from views import NoteView
from models import NoteModel, IdException
from time import sleep
from .observer import Observer
from json import JSONDecodeError


class NotePres(Observer):
    '''Презентер для взаимодействия view и model через него,
    согласно паттерну MVP'''

    __is_running: bool = True
    __notes: dict

    def __init__(self, view: NoteView, model: NoteModel) -> None:
        self.__view = view
        self.__model = model
        self.__view.set_observer(self)

    def start_app(self):
        self.__view.print_greetings()

        while self.__is_running:
            try:
                self.__notes = self.__model.scan_notes_db()
            except JSONDecodeError:
                self.__notes = {}
                self.__notes['notes'] = []

            self.__view.print_main_menu(self.__notes)

    def on_save_note(self, note_name, note_data):
        self.__model.save_new_note(note_name, note_data, self.__notes)
        self.__view.print_success_message('add')


    def on_delete_note(self, id):
        try:
            self.__model.del_note(id, self.__notes)
            self.__view.print_success_message('del')
        except IdException:
            self.__view.print_error_message('id')

    def on_edit_note(self, id, note_name, note_data):
        try:
            self.__model.edit_note(id, note_name, note_data, self.__notes)
            self.__view.print_success_message('edit')
        except IdException:
            self.__view.print_error_message('id')

    def on_show_note(self, id):
        try:
            note_to_find = self.__model.show_note(id, self.__notes)
            self.__view.print_one_note(note_to_find)
        except IdException:
            self.__view.print_error_message('id')

    def on_exit_app(self):
        raise SystemExit

from abc import ABC, abstractmethod


class Observer(ABC):
    '''Абстрактный класс для обязательно контракта презентеру,
    с точки зрения паттерна Observer'''

    @abstractmethod
    def on_save_note(self, note_name, note_data):
        pass

    @abstractmethod
    def on_delete_note(self, id):
        pass

    @abstractmethod
    def on_edit_note(self, id, note_name, note_data):
        pass

    @abstractmethod
    def on_show_note(self, id):
        pass

    def on_exit_app(self):
        pass

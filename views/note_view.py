from .ru_text import *
from .validator import Validator
from presenters.observer import Observer

from keyboard import wait
from time import sleep
import os


class NoteView:
    '''Класс, отвечающий за взаимодействие с юзером в консоли'''

    __observer: Observer = None

    def print_main_menu(self, all_notes):
        self.__clear_console()
        self.__print_message(MAIN_MENU)

        user_input = self.__get_user_choice()

        match user_input:
            case '1':
                if len(all_notes['notes']) == 0:
                    self.__clear_console()
                    self.__print_message(EMPTY_NOTES)

                    self.__wait_user_continue()
                    return

                self.__clear_console()
                self.__print_all_notes(all_notes)

                self.__wait_user_continue()
            case '2':
                note_id = self.__get_note_id()

                self.__observer.on_show_note(note_id)
                self.__wait_user_continue()
            case '3':
                note_title, note_cont = self.__get_user_data()

                self.__observer.on_save_note(note_title, note_cont)
            case '4':
                self.__clear_console()

                self.__print_all_notes(all_notes)
                self.__print_message(INPUT_ID_MESSAGE)
                self.__wait_user_continue()

                note_id = self.__get_note_id()
                note_title, note_cont = self.__get_user_data()

                self.__observer.on_edit_note(note_id, note_title, note_cont)
            case '5':
                self.__clear_console()

                self.__print_all_notes(all_notes)
                self.__print_message(INPUT_ID_MESSAGE)
                self.__wait_user_continue()

                self.__observer.on_delete_note(self.__get_note_id())
            case '6':
                self.print_goodbye()
                self.__observer.on_exit_app()
            case _:
                self.__print_message(INPUT_CHOICE_ERROR)
                sleep(2)

    def print_greetings(self) -> None:
        self.__clear_console()
        self.__print_message(GREETINGS)

        sleep(2)

    def print_goodbye(self) -> None:
        self.__clear_console()
        self.__print_message(GOODBYE)

        sleep(2)

    def print_one_note(self, note: dict) -> None:
        print(f'{ID_TEXT}{note["id"]}',
              f'{NAME_TEXT}{note["name"]}',
              f'{CONTENT_TEXT}{note["content"]}',
              f'{CREATE_REDACT_TEXT}{note["date"]}', sep='\n')

    def print_error_message(self, flag: str) -> None:
        match flag:
            case 'id':
                self.__print_message(NOT_FOUND_ID_ERROR)
                self.__wait_user_continue()

    def print_success_message(self, flag: str) -> None:
        match flag:
            case 'del':
                self.__print_message(DEL_SUCCESS)
                self.__wait_user_continue()
            case 'edit':
                self.__print_message(EDIT_SUCCESS)
                self.__wait_user_continue()
            case 'add':
                self.__print_message(ADD_SUCCESS)
                self.__wait_user_continue()

    def set_observer(self, obs) -> None:
        self.__observer = obs

    @classmethod
    def __get_user_choice(cls) -> str:
        user_choice = input().strip()

        return user_choice

    @classmethod
    def __get_note_id(cls) -> int:
        is_input = True

        while is_input:
            os.system('cls')

            id_note = input(INPUT_ID_MESSAGE).strip()

            if Validator.validate_id(id_note):
                cls.__print_message(INPUT_ID_ERROR)
                sleep(2)

                continue

            is_input = False

        return int(id_note)

    @classmethod
    def __get_user_data(cls) -> tuple[str]:
        is_input = True

        while is_input:
            os.system('cls')

            note_name = input(INPUT_NAME_MESSAGE).strip()
            note_content = input(INPUT_CONTENT_MESSAGE).strip()

            if Validator.validate_data((note_name, note_content)):
                cls.__print_message(INPUT_DATA_ERROR)
                sleep(2)

                continue

            is_input = False

        return note_name, note_content

    @classmethod
    def __print_message(cls, message: str) -> None:
        symb_len = len(message)

        print('-' * symb_len, message, '-' * symb_len, sep='\n')

    @classmethod
    def __clear_console(cls) -> None:
        os.system('cls')

    @classmethod
    def __wait_user_continue(cls) -> None:
        cls.__print_message(PRESS_SPACE)
        wait('Space')

    @classmethod
    def __print_all_notes(cls, note_lst: dict) -> None:
        for note in sorted(note_lst['notes'], key=lambda note: note['date']):
            print(f'{ID_TEXT}{note["id"]}',
                  f'{NAME_TEXT}{note["name"]}',
                  f'{CONTENT_TEXT}{note["content"]}',
                  f'{CREATE_REDACT_TEXT}{note["date"]}', sep='\n')
            print()

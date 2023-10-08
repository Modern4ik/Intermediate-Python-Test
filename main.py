from presenters import NotePres, NoteModel, NoteView

if __name__ == '__main__':
    presenter = NotePres(NoteView(), NoteModel())

    presenter.start_app()

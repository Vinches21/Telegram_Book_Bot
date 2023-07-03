import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = min(start + size, len(text))
    for i in range(end, start, -1):
        if text[i-1] in ",.!" and text[i] not in ",.!:?" and (text[i] == " " or "\n"):
            break
        else:
            i = end

    page = text[start:i].rstrip()
    return  page, len(page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
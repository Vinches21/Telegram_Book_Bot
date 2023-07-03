import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_symbols = ',.!:;?'
    if start + page_size >= len(text):
        return text[start:], len(text) - start
    for i in range(start + page_size - 1, start - 1, -1):
        if text[i] in end_symbols and text[i + 1] not in end_symbols:
            return text[start: i + 1], i - start + 1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
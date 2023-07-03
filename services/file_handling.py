import os


BOOK_PATH = '/Users/oleg_polikarpov/PycharmProjects/Telegram_Book_Bot/book/book.txt'
PAGE_SIZE = 900

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
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
        start += page_size
        book[page_number] = page_text.strip()
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
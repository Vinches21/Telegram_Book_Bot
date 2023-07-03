def _get_part_text(text, start, page_size):
    end = min(start + page_size, len(text))
    for i in range(end, start, -1):
        if text[i - 1] in ".,!;:?":
            break
        elif text[i - 2:i] == "..":
            i -= 2
            break
    else:
        i = end
    page = text[start:i].rstrip()
    return page, len(page)

    page = text[start:i].rstrip()
    return page, len(page)


text = 'Раз. Два. Три. Четыре. Пять. Прием!'
print(*_get_part_text(text, 5, 9), sep='\n')
def human_read_format(size):
    s = ["Б", "КБ", "МБ", "ГБ"]
    c = 0
    while (size / 1024) >= 1:
        c = c + 1
        size = size / 1024
    size = round(size)
    return f'{size}{s[c]}'
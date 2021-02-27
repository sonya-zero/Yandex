import os


def get_files_sizes():
    
    def human_read_format(size):
        s = ["Б", "КБ", "МБ", "ГБ"]
        c = 0
        while (size / 1024) >= 1:
            c = c + 1
            size = size / 1024
        size = round(size)
        return f'{size}{s[c]}'
    data = os.listdir()
    gt = []
    for i in data:
        if os.path.isfile(i):
            size = os.path.getsize(i)
            size = human_read_format(size)
            gt.append(f'{i} {size}\n')
    return ''.join(gt)
        
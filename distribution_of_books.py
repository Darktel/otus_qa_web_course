import csv
import json


def read_books_csv_file(file: str):
    '''Чтение csv файла'''
    with open(file, newline='') as __f:
        books = []
        reader = csv.reader(__f)
        header = []
        stg_header = next(reader)
        for _header in stg_header:
            header.append(str(_header).lower())
        for book in reader:
            book[3] = int(book[3])
            books.append(dict(zip(header[:-1], book[:-1])))
    return books


def read_json_file(file: str):
    """ чтение json из файла"""
    with open(file, 'r') as json_file:
        return json.loads(json_file.read())


def write_json_file(file: str, data):
    with open(file, "w") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


def get_user(__json: read_json_file):
    __data = {}
    users = []
    for user in __json:  # формируем шаблон json файла для дальнейшего наполнения книгами
        __data['name'] = user.get('name')
        __data['gender'] = user.get('gender')
        __data['address'] = user.get('address')
        __data['age'] = user.get('age')
        __data["books"] = []
        users.append(__data.copy())
    return users


def distribution_of_books(json_data, books):
    while len(books) > 0:
        for user in json_data:
            if len(books) == 0:
                break
            book = books.pop()
            user['books'].append(book)


if '__main__' == __name__:
    json_data = get_user(read_json_file('users.json'))  # получаем необходимую инфу по пользователям.
    books = read_books_csv_file('books.csv')  # получаем данные по книгам.
    distribution_of_books(json_data, books)  # раздаем книги нуждающимся
    write_json_file('result.json', json_data)  # Записываем файл result.json с полученными данными.

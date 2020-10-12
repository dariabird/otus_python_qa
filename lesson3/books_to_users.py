import csv
import json


def get_users(filename):
    with open(filename) as f:
        return json.load(f)


def get_books(filename):
    books = []
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            book = dict(zip(header, row))
            books.append(book)
    return books


def books_to_users(books, users):
    result = []
    b_len = len(books)
    for i, user in enumerate(users):
        book = [books[i]] if i < b_len else []
        bu_dict = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "books": book
        }
        result.append(bu_dict)
    return result


def write_example_json(bu_dicts, filename="example.json"):
    with open(filename, "w") as f:
        json.dump(bu_dicts, f)


if __name__ == '__main__':
    users = get_users("users-39204-8e2f95.json")
    books = get_books("books-39204-271043.csv")
    bu_dicts = books_to_users(books, users)
    write_example_json(bu_dicts)

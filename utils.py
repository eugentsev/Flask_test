import random, string, csv
import requests

from faker import Faker


def generate_password(password_len=10) -> str:
    if not isinstance(password_len, int):
        raise TypeError('Invalid')

    choices = string.ascii_letters + string.digits + '#$%^'
    result = ''

    for _ in range(password_len):
        result += random.choice(choices)

    return result


def open_file_req():
    file = open('requirements.txt')
    return file.read()


def username_generate(users_count):
    if not isinstance(users_count, int):
        raise TypeError('Invalid')

    fake = Faker('en_US')
    str_1 = ''

    for _ in range(users_count):
        name = fake.name()
        email = fake.email()
        str_1 += f'{name} - {email}\n'

    return str_1


def avg_cvs():
    with open('hw.csv') as file_csv:
        file_reader = csv.reader(file_csv, delimiter=",")
        height_all = []
        weight_all = []

        for row in file_reader:
            if 'Index' not in row:
                for index, element in enumerate(row):
                    if index == 1:
                        element = float(element)
                        height_all.append(element)
                    if index == 2:
                        element = float(element)
                        weight_all.append(element)

        avg_height = (sum(height_all) / len(height_all)) * 2.54
        avg_weight = (sum(weight_all) / len(weight_all)) / 2.205
    return f'{avg_height} сm, {avg_weight} kg'


def space_count():
    r = requests.get('http://api.open-notify.org/astros.json')
    i = 0

    for dict_name in r.json()['people']:
        dict_name.get('name')
        i += 1

    return i
import sqlite3
from flask import Flask, request

from utils import generate_password as gp, open_file_req as file_req, username_generate as ug, avg_cvs, space_count

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/generate-password/')
def generate_password():

    # validate password-len from client
    password_len = request.args.get('password-len')

    if not password_len:
        password_len = 10
    else:
        if password_len.isdigit():
            password_len = int(password_len)
        else:
            return 'Invalid parameter password-len'

    password = gp(password_len)
    print('password_len', password_len)
    return f'{password}\n'


@app.route('/requirements/')
def requirements():
    req = file_req()
    return f'{req}'


@app.route('/generate-users/')
def generate_users():
    users_count = request.args.get('users-count')

    if not users_count:
        users_count = 100
    else:
        if users_count.isdigit():
            users_count = int(users_count)
        else:
            return 'Invalid parameter count'

    generate_user = ug(users_count)
    return f'{generate_user}'


@app.route('/mean/')
def mean():
    avg = avg_cvs()
    return f'{avg}'


@app.route('/space/')
def space():
    space_c = space_count()
    return f'count - {space_c}'


@app.route('/phones/create/')
def phones_create():
    connection = sqlite3.connect('phones.db')
    contact_name = request.args.get('contactName')
    phone_value = request.args.get('phoneValue')
    cursor = connection.cursor()

    if not contact_name:
        sql_query = '''
                    insert into phones (contactName, phoneValue)
                    values ('Eugen', '092732173');
                    '''
    elif contact_name.isdigit():
        return 'Invalid name'
    else:
        sql_query = f'''
                    insert into phones (contactName, phoneValue)
                    values ('{contact_name}', '{phone_value}');
                    '''

    cursor.execute(sql_query)
    connection.commit()
    connection.close()

    return 'phones create'


@app.route('/phones/read/')
def phones_read():
    connection = sqlite3.connect('phones.db')
    contact_name = request.args.get('contactName')
    phone_value = request.args.get('phoneValue')
    cursor = connection.cursor()

    if not contact_name or phone_value:
        sql_query = '''
                    select * from phones;
                    '''
    else:
        sql_query = f'''
                    select * from phones
                    where contactName = '{contact_name}';
                    '''

    cursor.execute(sql_query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()

    return str(result)


@app.route('/phones/update/')
def phones_update():
    connection = sqlite3.connect('phones.db')
    contact_name = request.args.get('contactName')
    phone_value = request.args.get('phoneValue')
    cursor = connection.cursor()

    if not contact_name:
        return 'Please write data for update'
    else:
        sql_query = f'''
                    update phones
                    set contactName = '{contact_name}', phoneValue = '{phone_value}'
                    where contactName = '{contact_name}';
                    '''

    cursor.execute(sql_query)
    connection.commit()
    connection.close()

    return 'phones update'


@app.route('/phones/delete/')
def phones_delete():
    connection = sqlite3.connect('phones.db')
    phone_value = request.args.get('phoneValue')
    cursor = connection.cursor()

    if not phone_value:
        sql_query = '''
                    delete from phones;
                    '''
    else:
        sql_query = f'''
                    delete from phones
                    where phoneValue = '{phone_value}'
                    '''
    cursor.execute(sql_query)
    connection.commit()
    connection.close()

    return 'phones delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
import mysql.connector
from datetime import date


connection = mysql.connector.connect(user='root', password='Dragonball2004*', host='localhost',
                                     database='smartcash', port='3306')


def search_user_id(username):
    cur = connection.cursor()
    sql = f"select id_usuario from usuario where username = '{username}'"
    cur.execute(sql)
    id = cur.fetchall()
    cur.close()
    return id[0][0]


def create_user(user_info):
    cur = connection.cursor()
    id_user = count_users()
    username = user_info['username']
    name = user_info['name']
    last_name = user_info['last_name']
    email = user_info['email']
    password = user_info['password1']
    print('id', id_user)
    sql = f'''insert into usuario(id_usuario, username, nombre, apellido, email, pass) values({id_user}, '{username}', '{name}', '{last_name}', '{email}', '{password}')'''
    print(sql)
    cur.execute(sql)
    connection.commit()
    cur.close()


def count_users():
    cur = connection.cursor()
    sql = 'select count(1) from usuario'
    cur.execute(sql)
    cantidad = cur.fetchall()
    cur.close()
    return cantidad[0][0]


def count_movements():
    cur = connection.cursor()
    sql = f'select count(1) from movimiento'
    cur.execute(sql)
    cantidad = cur.fetchall()
    cur.close()
    return cantidad[0][0]


def create_movement(movements, direction):
    for mov in movements:
        print(mov)
        movement = mov.split(', ')
        print(movement)
        id_user = search_user_id(current_user.username)
        cur = connection.cursor()
        name = movement[0]
        id_movement = count_movements()
        value = movement[1]
        category = movement[2]
        sql = f'''insert into movimiento(nombre_movimiento, id_movimiento, id_usuario, direccion, valor, fecha, 
        categoria) values('{name}', {id_movement}, {id_user}, '{direction}', '{value}', '
{date.today().strftime('%Y-%m-%d')}', '{category}') '''
        cur.execute(sql)
        connection.commit()
        cur.close()


def search_user_movements():
    cur = connection.cursor()
    id_user = search_user_id(current_user.username)
    sql = f"select * from movimiento where id_usuario = {id_user}"
    cur.execute(sql)
    ans = cur.fetchall()
    cur.close()
    return ans


current_user = None


def search_movement_category(category):
    cur = connection.cursor()
    sql = f"select * from movimiento where categoria = '{category}' and id_usuario = {search_user_id(current_user.username)}"
    cur.execute(sql)
    ans = cur.fetchall()
    cur.close()
    return ans




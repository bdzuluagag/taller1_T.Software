
import datetime

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
    sql = f'''insert into usuario(id_usuario, username, nombre, apellido, email, pass) values({id_user}, '{username}', '{name}', '{last_name}', '{email}', '{password}')'''
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
        movement = mov.split(', ')
        id_user = search_user_id(current_user.username)
        cur = connection.cursor()
        name = movement[0]
        id_movement = count_movements()
        value = movement[1]
        category = movement[2]
        user_goals = search_user_goals()
        for goal in user_goals:
            if goal[2].lower() == category.lower():
                print('update')
                sql = f"update meta set cantidadActual = cantidadActual + {value} where id_usuario = {id_user} and nombre = '{category}'"
                cur.execute(sql)
                connection.commit()
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
    category = category.lower()
    cur = connection.cursor()
    sql = f"select * from movimiento where categoria = '{category}' and id_usuario = {search_user_id(current_user.username)}"
    cur.execute(sql)
    ans = cur.fetchall()
    cur.close()
    return ans


def search_user_movement_direction(direction):
    cur = connection.cursor()
    id_user = search_user_id(current_user.username)
    sql = f"select * from movimiento where id_usuario = {id_user} and direccion = '{direction}'"
    cur.execute(sql)
    ans = cur.fetchall()
    cur.close()
    return ans


def consult_user_balance():
    cur = connection.cursor()
    id_user = search_user_id(current_user.username)
    sql = f"select * from movimiento where id_usuario = {id_user}"
    balance = 0
    cur.execute(sql)
    movements = cur.fetchall()
    for movement in movements:
        if movement[3] == 'entrada':
            balance += movement[4]
        else:
            balance -= movement[4]
    return balance


def count_categories():
    cur = connection.cursor()
    sql = f'select count(1) from categoria'
    cur.execute(sql)
    cantidad = cur.fetchall()
    cur.close()
    return cantidad[0][0]


def create_category(category):
    category = category.lower()
    cur = connection.cursor()
    id_user = search_user_id(current_user.username)
    if search_created_category(category):
        return True
    sql = f"insert into categoria(id_categoria, nombre, id_usuario) values({count_categories()}, '{category}', {id_user})"
    cur.execute(sql)
    connection.commit()
    cur.close()
    return False


def search_created_category(category):
    cur = connection.cursor()
    id_user = search_user_id(current_user.username)
    sql = f"select count(1) from categoria where id_usuario = {id_user} and nombre = '{category}'"
    cur.execute(sql)
    cantidad = cur.fetchall()
    cur.close()
    return cantidad[0][0]


def search_user_categories():
    id_user = search_user_id(current_user.username)
    cur = connection.cursor()
    sql = f"select * from categoria where id_usuario = {id_user}"
    cur.execute(sql)
    categories = cur.fetchall()
    cur.close()
    print('categories', categories)
    return categories + [(-1, 'esenciales', id_user), (-1, 'lujos', id_user), (-1, 'fijos', id_user),
                         (-1, 'deudas', id_user)]


def count_goals():
    cur = connection.cursor()
    sql = f'select count(1) from meta'
    cur.execute(sql)
    cantidad = cur.fetchall()
    cur.close()
    return cantidad[0][0]


def create_goal(name, value, goal_date):
    id_user = search_user_id(current_user.username)
    cur = connection.cursor()
    id_goal = count_goals()
    goal_date = list(map(int, goal_date.split('/')))
    goal_date = datetime.date(goal_date[0], goal_date[1], goal_date[2])
    sql = f"insert into meta(id_meta, id_usuario, nombre, fecha, cantidadMeta, cantidadActual) values ({id_goal}, " \
          f"{id_user}, '{name}', '{goal_date.strftime('%Y-%m-%d')}', {value}, {0})"
    cur.execute(sql)
    connection.commit()
    cur.close()


def search_user_goals():
    id_user = search_user_id(current_user.username)
    cur = connection.cursor()
    sql = f"select * from meta where id_usuario = {id_user}"
    cur.execute(sql)
    goals = cur.fetchall()
    cur.close()
    return goals



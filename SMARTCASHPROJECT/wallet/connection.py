import datetime
from .models import Categoria, Movimiento, Meta, EventoFijo, EventoPeriodico
from datetime import date, datetime


def create_default_categories(user):
    lujo = Categoria(usuario=user, nombre='lujos')
    fijo = Categoria(usuario=user, nombre='fijos')
    deuda = Categoria(usuario=user, nombre='deudas')
    esencial = Categoria(usuario=user, nombre='esenciales')
    lujo.save()
    fijo.save()
    deuda.save()
    esencial.save()


def search_category_by_name(category, user):
    ans = Categoria.objects.all().filter(usuario=user, nombre=category.lower())
    return ans[0] if ans else ans


def create_movement(movements, direction, user):
    goals = Meta.objects.all().filter(usuario=user)
    for mov in movements:
        movement = mov.split(', ')
        name = movement[0]
        value = movement[1]
        category = search_category_by_name(movement[2], user)
        for goal in goals:
            if goal.nombre == category.nombre:
                goal.cantidad_actual += int(value)
                goal.save()
        new_movement = Movimiento(nombre=name, valor=value, categoria=category, fecha=date.today(), direccion=direction)
        new_movement.save()


def search_user_movements(user):
    moves = Movimiento.objects.all().filter(categoria__usuario=user)
    return moves


def search_movement_category(category, user):
    category = search_category_by_name(category, user)
    moves = Movimiento.objects.all().filter(categoria=category) if category else None
    return moves


def search_user_movement_direction(direction, user):
    moves = Movimiento.objects.all().filter(direccion=direction, categoria__usuario=user)
    return moves


def consult_user_balance(user):
    moves = Movimiento.objects.all().filter(categoria__usuario=user)
    user_balance = 0
    for move in moves:
        if move.direccion == 'salida':
            user_balance -= move.valor
        else:
            user_balance += move.valor
    return user_balance


def create_category(category, user):
    if category not in [cat.nombre for cat in search_user_categories(user)]:
        category = Categoria(nombre=category.lower(), usuario=user)
        category.save()
        return False
    return True


def search_user_categories(user):
    user_categories = Categoria.objects.all().filter(usuario=user)
    return user_categories


def create_goal(name, value, goal_date, user):
    goal = Meta(usuario=user, nombre=name, cantidad_meta=value, fecha=datetime.strptime(goal_date, '%Y/%m/%d').date(), cantidad_actual=0, fecha_creacion=date.today())
    goal.save()


def search_user_goals(user):
    goals = Meta.objects.all().filter(usuario=user)
    return goals


def create_event(event_type, name, value, day_date, user):
    if event_type == 1:
        event = EventoPeriodico(nombre=name, cantidad=value, dia=day_date, usuario=user)
        event.save()
    else:
        event = EventoFijo(nombre=name, cantidad=value, fecha=datetime.strptime(day_date, '%Y/%m/%d').date(), usuario=user)
        event.save()


def search_periodic_events(user):
    events = EventoPeriodico.objects.all().filter(usuario=user)
    return events


def search_events(user):
    events = EventoFijo.objects.all().filter(usuario=user)
    return events


def search_day_events(periodic, events):
    current_date = date.today()
    ans = []
    if periodic:
        for event in periodic:
            if event.dia == current_date.day:
                ans.append(event)
    if events:
        for event in events:
            if event.fecha == current_date:
                ans.append(event)
    return ans

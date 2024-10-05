from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from wallet import movements as mov
from wallet import connection
from wallet import charts
from datetime import date
import os
from django.conf import settings
from django.http import HttpResponse
import datetime
from wallet import dummy
from .services import MovementService 
from .observers import Subject, GoalCreatedObserver


def home(request):
    connection.current_user = request.user
    current_user = request.user
    if request.user.is_authenticated and len(connection.search_user_categories(request.user)) == 0:
        connection.create_default_categories(request.user)
    return render(request, 'registration/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login(request):
    return render(request, 'registration/login.html')  # redirigir al login


def data_form(request):
    connection.current_user = request.user
    average_income = request.GET.get('average_income')
    life_cost_average = request.GET.get('life_cost_average')
    month_income = request.GET.get('month_income')
    month_life_expenses = request.GET.get('month_life_expenses')
    month_expenses = request.GET.get('month_expenses')
    current_savings = request.GET.get('current_savings')
    return render(request, 'registration/data_form.html',
                  {'average_income': average_income, 'life_cost_average': life_cost_average,
                   'month_income': month_income, 'month_life_expenses': month_life_expenses,
                   'month_expenses': month_expenses, 'current_savings': current_savings})


def movements(request):
    connection.current_user = request.user

    # Inicializa el servicio de movimientos
    movement_service = MovementService(request.user)

    average_income = request.GET.get('average_income')
    life_cost_average = request.GET.get('life_cost_average')
    month_income = request.GET.get('month_income')
    month_life_expenses = request.GET.get('month_life_expenses')
    month_expenses = request.GET.get('month_expenses')
    current_savings = request.GET.get('current_savings')

    income_name = request.GET.get('income_name')
    income_value = request.GET.get('income_value')
    income_category = request.GET.get('income_category')

    exit_name = request.GET.get('exit_name')
    exit_value = request.GET.get('exit_value')
    exit_category = request.GET.get('exit_category')

    incomes = f'{income_name}, {income_value}, {income_category}' if income_value and income_category and income_name else None
    exits = f'{exit_name}, {exit_value}, {exit_category}' if exit_category and exit_name and exit_value else None

    # Usa el servicio para obtener los movimientos del usuario
    user_movements = movement_service.get_user_movements(incomes, exits)

    download_movements = request.GET.get('download_movements')
    if download_movements == '':
        # Usa el servicio para generar el CSV y devolver la respuesta
        return movement_service.generate_movements_csv(user_movements)

    user_categories = [category.nombre for category in connection.search_user_categories(request.user)]

    return render(request, 'registration/movements.html', {'average_income': average_income,
                                                           'life_cost_average': life_cost_average,
                                                           'month_income': month_income,
                                                           'month_life_expenses': month_life_expenses,
                                                           'month_expenses': month_expenses,
                                                           'current_savings': current_savings,
                                                           'movements': user_movements, 
                                                           'user_categories': user_categories})


def categories(request):
    created = None
    connection.current_user = request.user
    category = request.GET.get('category')
    category_to_create = request.GET.get('category_to_create')
    if category_to_create:
        created = connection.create_category(category_to_create, request.user)

    matches = mov.consult_category(category, request.user)
    user_categories = [category.nombre for category in connection.search_user_categories(request.user)]
    return render(request, 'registration/categories.html',
                  {'category': category, 'matches': matches, 'created': created, 'user_categories': user_categories})


def statistics(request):
    connection.current_user = request.user
    charts.pie_chart_movements_direction(connection.search_user_movement_direction('entrada', request.user), 'entrada')
    charts.pie_chart_movements_direction(connection.search_user_movement_direction('salida', request.user), 'salida')
    charts.line_chart_date_direction(connection.search_user_movement_direction('entrada', request.user), 'entrada')
    charts.line_chart_date_direction(connection.search_user_movement_direction('salida', request.user), 'salida')
    return render(request, 'registration/statistics.html')


def suggestions(request):
    connection.current_user = request.user
    balance = connection.consult_user_balance(request.user)
    dic_categories = mov.consult_user_lux(request.user)
    print(dic_categories)
    lujos = dic_categories['lujos'] if 'lujos' in dic_categories else 0
    return render(request, 'registration/suggestions.html', {'balance': balance, 'lujos': lujos})


def goals(request):
    connection.current_user = request.user

    # Creación del sujeto
    goal_subject = Subject()
    # Añadir el observador
    goal_observer = GoalCreatedObserver()
    goal_subject.add_observer(goal_observer)

    goal_name = request.GET.get('goal_name')
    goal_value = request.GET.get('goal_value')
    goal_date = request.GET.get('goal_date')

    if goal_date and goal_name and goal_value:
        connection.create_goal(goal_name.lower(), goal_value, goal_date, request.user)
        connection.create_category(goal_name, request.user)

        # Notificar a los observadores sobre la nueva meta
        goal_subject.notify_observers(f"Meta '{goal_name}' creada con valor {goal_value} y fecha {goal_date}")

    user_goals = connection.search_user_goals(request.user)
    user_estimated_dates = mov.date_estimated(user_goals)

    return render(request, 'registration/goals.html',
                  {'goal_name': goal_name, 'goal_value': goal_value, 'goal_date': goal_date, 'user_goals': user_goals, 'estimated_dates': user_estimated_dates})

def events(request):
    connection.current_user = request.user
    periodic_event_name = request.GET.get('periodic_event_name')
    periodic_event_value = request.GET.get('periodic_event_value')
    periodic_event_day = request.GET.get('periodic_event_day')

    event_name = request.GET.get('event_name')
    event_value = request.GET.get('event_value')
    event_date = request.GET.get('event_date')

    if periodic_event_day and periodic_event_value and periodic_event_name:
        connection.create_event(1, periodic_event_name, periodic_event_value, periodic_event_day, request.user)
    if event_name and event_value and event_date:
        connection.create_event(0, event_name, event_value, event_date, request.user)
    user_events = connection.search_events(request.user)
    user_periodic_events = connection.search_periodic_events(request.user)

    day_events = connection.search_day_events(user_periodic_events, user_events)
    return render(request, 'registration/events.html',
                  {'days': range(1, 32), 'periodic_event_name': periodic_event_name,
                   'periodic_event_value': periodic_event_value, 'periodic_event_day': periodic_event_day,
                   'event_name': event_name, 'event_value': event_value, 'event_date': event_date,
                   'user_events': user_events, 'user_periodic_events': user_periodic_events, 'day_events': day_events,
                   'today': date.today().day})

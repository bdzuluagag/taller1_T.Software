from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from wallet import movements as mov
from wallet import connection
from wallet import charts


def home(request):
    connection.current_user = request.user
    current_user = request.user
    print('user', current_user.username)
    return render(request, 'registration/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            connection.create_user(form.cleaned_data)
            return redirect('dataaform')
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

    print(income_name)
    print(income_value)
    print(income_category)

    incomes = f'{income_name}, {income_value}, {income_category}' if income_value and income_category and income_name else None

    exits = f'{exit_name}, {exit_value}, {exit_category}' if exit_category and exit_name and exit_value else None

    movements = mov.read_movements(incomes, exits)
    user_categories = [category[1] for category in connection.search_user_categories()]

    return render(request, 'registration/movements.html', {'average_income': average_income,
                                                           'life_cost_average': life_cost_average,
                                                           'month_income': month_income,
                                                           'month_life_expenses': month_life_expenses,
                                                           'month_expenses': month_expenses,
                                                           'current_savings': current_savings,
                                                           'movements': movements, 'user_categories': user_categories})


def categories(request):
    created = None
    connection.current_user = request.user
    category = request.GET.get('category')
    category_to_create = request.GET.get('category_to_create')
    if category_to_create:  # puede crear duplicados
        created = connection.create_category(category_to_create)
    matches = mov.consult_category(category)
    user_categories = [category[1] for category in connection.search_user_categories()]
    return render(request, 'registration/categories.html',
                  {'category': category, 'matches': matches, 'created': created, 'user_categories': user_categories})


def statistics(request):
    connection.current_user = request.user
    charts.pie_chart_movements_direction(connection.search_user_movement_direction('entrada'), 'entrada')
    charts.pie_chart_movements_direction(connection.search_user_movement_direction('salida'), 'salida')
    charts.line_chart_date_direction(connection.search_user_movement_direction('entrada'), 'entrada')
    charts.line_chart_date_direction(connection.search_user_movement_direction('salida'), 'salida')
    return render(request, 'registration/statistics.html')


def suggestions(request):
    connection.current_user = request.user
    balance = connection.consult_user_balance()
    return render(request, 'registration/suggestions.html', {'balance': balance})

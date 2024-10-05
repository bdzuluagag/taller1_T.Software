import matplotlib.pyplot as plt
plt.switch_backend('agg')
from django.http import HttpResponse


def create_charts(movements):
    return [line_chart_date(movements), pie_chart_movements(movements)]


def pie_chart_movements(movements):
    categories = {}
    for movement in movements:
        if movement.categoria in categories:
            categories[movement.categoria.nombre] += movement.valor
        else:
            categories[movement.categoria.nombre] = movement.valor
    values, labels = categories.values(), categories.keys()
    plt.figure()
    plt.pie(values, labels=labels)
    plt.savefig('static/images/pie_chart.png')


def pie_chart_movements_direction(movements, direction):
    categories = {}
    for movement in movements:
        if movement.categoria in categories:
            categories[movement.categoria.nombre] += movement.valor
        else:
            categories[movement.categoria.nombre] = movement.valor
    values, labels = categories.values(), categories.keys()
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.0f%%')
    plt.savefig(f'static/images/pie_chart_{direction}.png')


def line_chart_date(movements):
    dates = {}
    for movement in movements:
        if movement.fecha in dates:
            dates[movement.fecha] += movement.valor
        else:
            dates[movement.fecha] = movement.valor
    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure)
    plt.xlabel('Fecha', figure=figure)
    plt.ylabel('Dinero gastado', figure=figure)
    plt.savefig('static/images/line_chart.png')


def line_chart_date_direction(movements, direction):
    dates = {}
    for movement in movements:
        if movement.fecha in dates:
            dates[movement.fecha] += movement.valor
        else:
            dates[movement.fecha] = movement.valor

    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure, color='blue' if direction == 'entrada' else 'red')
    plt.xlabel('fecha', figure=figure)
    plt.ylabel(f'{direction.capitalize()}', figure=figure)
    plt.savefig(f'static/images/line_chart_{direction}.png')

import matplotlib.pyplot as plt, mpld3
from django.http import HttpResponse


def create_charts(movements):
    return [line_chart_date(movements), pie_chart_movements(movements)]


def pie_chart_movements(movements):
    categories = {}
    for movement in movements:
        if movement[-1] in categories:
            categories[movement[-1]] += movement[4]
        else:
            categories[movement[-1]] = movement[4]
    values, labels = categories.values(), categories.keys()
    plt.figure()
    plt.pie(values, labels=labels)
    plt.title('Gastos en categorías')
    plt.savefig('static/images/pie_chart.png')


def line_chart_date(movements):
    dates = {}
    for movement in movements:
        if movement[5] in dates:
            dates[movement[5]] += movement[4]
        else:
            dates[movement[5]] = movement[4]
    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure)
    plt.title('Gastos en el tiempo')
    plt.xlabel('fecha', figure=figure)
    plt.ylabel('dinero gastado', figure=figure)
    plt.savefig('static/images/line_chart.png')


def line_chart_date_direction(movements, direction):
    dates = {}
    for movement in movements:
        if movement[5] in dates:
            dates[movement[5]] += movement[4]
        else:
            dates[movement[5]] = movement[4]
    figure = plt.figure()
    values, labels = dates.values(), [x.strftime("%m/%d/%Y") for x in dates.keys()]
    plt.plot(labels, values, figure=figure)
    plt.title(f'{direction}s en el tiempo')
    plt.xlabel('fecha', figure=figure)
    plt.ylabel(f'{direction}', figure=figure)
    plt.savefig(f'static/images/line_chart_{direction}.png')

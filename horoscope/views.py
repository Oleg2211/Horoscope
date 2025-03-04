from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.template.loader import render_to_string


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_dates = {
    'aries': [date(2025, 3, 21).timetuple().tm_yday, date(2025, 4, 20).timetuple().tm_yday],
    'taurus': [date(2025, 4, 21).timetuple().tm_yday, date(2025, 5, 21).timetuple().tm_yday],
    'gemini': [date(2025, 5, 22).timetuple().tm_yday, date(2025, 6, 21).timetuple().tm_yday],
    'cancer': [date(2025, 6, 22).timetuple().tm_yday, date(2025, 7, 22).timetuple().tm_yday],
    'leo': [date(2025, 7, 23).timetuple().tm_yday, date(2025, 8, 21).timetuple().tm_yday],
    'virgo': [date(2025, 8, 22).timetuple().tm_yday, date(2025, 9, 23).timetuple().tm_yday],
    'libra': [date(2025, 9, 24).timetuple().tm_yday, date(2025, 10, 23).timetuple().tm_yday],
    'scorpio': [date(2025, 10, 24).timetuple().tm_yday, date(2025, 11, 22).timetuple().tm_yday],
    'sagittarius': [date(2025, 11, 23).timetuple().tm_yday, date(2025, 12, 22).timetuple().tm_yday],
    'capricorn': [date(2025, 12, 23).timetuple().tm_yday, date(2025, 1, 20).timetuple().tm_yday],
    'aquarius': [date(2025, 1, 21).timetuple().tm_yday, date(2025, 2, 19).timetuple().tm_yday],
    'pisces': [date(2025, 2, 20).timetuple().tm_yday, date(2025, 3, 20).timetuple().tm_yday]
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['libra', 'aquarius', 'gemini'],
    'water': ['pisces', 'cancer', 'scorpio']
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {

        'zodiacs': zodiacs
    }

    return render(request, 'horoscope/index.html', context=context)

def get_info_abaut_sign_zodiac(requesrt, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac
    }
    return render(requesrt, "horoscope/info_zodiac.html", context=data) #04.03/2025



def get_info_abaut_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Нет такого знака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)

def type(request):
    types = list(types_dict)
    type_elements = ''
    for type_el in types:
        redirect_path = reverse('element-name', args=(type_el,))
        type_elements += f'''<li><a href ='{redirect_path} '>{type_el.title()}</a></li>'''
    response = f'''<ul>{type_elements}</ul>'''
    return HttpResponse(response)

def get_element(request, element: str):
    get_el = types_dict.get(element, None)
    res = ''
    for el in get_el:
        redirect_path = reverse('horoscope-name', args=(el,))
        res += f'''<li><a href = '{redirect_path}'>{el.title()}</a></li>'''
    response = f'''<ol>{res}</ol>'''
    return HttpResponse(response)


def get_sign_by_date(request, day, month):
    my_date = date(2024, month, day).timetuple().tm_yday
    for k, v in zodiac_dates.items():
        if my_date in range(v[0], v[1]+2):
            redirect_path = reverse('horoscope-name', args=(k,))
            return HttpResponse(f''' День: {day} <br>
                                     Месяц: {month}<br>
            Знак зодика: <a href ='{redirect_path}'>{k.title()}</a>''')

    return HttpResponse("Введите коректную дату")


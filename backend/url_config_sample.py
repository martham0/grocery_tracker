import datetime


def get_city_urls():
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=30)

    return {
        'san_gabriel': f'https://www.sangabrielcity.com/calendar.aspx',
        'temple': f'https://www.ci.temple-city.ca.us/calendar.aspx?CID=23',
        'alhambra': f'https://www.cityofalhambra.org/calendar.aspx?CID=14',
        'pasadena': 'https://www.cityofpasadena.net/events/'
    }

from collections import defaultdict
import logging

from helpers.fetch_html import fetch_html
from helpers.parse_html import parse_html
from helpers.extract_events_arc import extract_events_arc
from helpers.extract_events_sg import extract_events_sg
from helpers.extract_events_pas import extract_events_pas


def main():
    """Main function to fetch, parse, and extract event data."""
    # Fetch the HTML content
    san_gabriel_url = ['San Gabriel','https://www.sangabrielcity.com/calendar.aspx?CID=20']
    temple_url = ['Temple','https://www.ci.temple-city.ca.us/calendar.aspx?CID=23&Keywords=&startDate=&enddate=&']
    alhambra_url = ['Alhambra','https://www.cityofalhambra.org/calendar.aspx?CID=14']
    pasadena_city_url = ['Pasadena','https://www.cityofpasadena.net/events/list/?tribe_eventcategory%5B0%5D=257']

    city_urls = [san_gabriel_url,temple_url,alhambra_url,pasadena_city_url]

    city_events = defaultdict(list)

    for city,url in city_urls:
        html_text = fetch_html(url)

        # Parse html
        html_soup = parse_html(html_text)

        event_list = extract_events_sg(html_soup,city,url) if city != 'Pasadena' else extract_events_pas(html_soup)
        city_events [city] = event_list


    print(city_events.keys())
    print(city_events['Alhambra'][0])




if __name__ == "__main__":
    #TODO:dont push log info
    logging.basicConfig(filename='logs/project.log', level=logging.INFO)
    #TODO:look up cpu usage
    main()

# San Gabriel events

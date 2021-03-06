import requests
import database
import email_sender
from country import Country
from offer import Offer


def connect_for_countries(country_id):
    params = {'productType': 1, 'transportType': 'F', 'countryIds': str(country_id)+':'}

    resp = requests.get("https://www.travelplanet.pl/json/trips/getDestinationsJson/", params=params)
    data = resp.json()

    if len(data) > 0:
        countries = data['countries']
        if len(countries) > 0:
            id = data['countries'][0]['i']
            name = data['countries'][0]['n']
            country = Country(id, name)
            database.Database.getInstance().insert_country(country)
            print(id, name, sep=',')
    pass


def create_offer(offer):
    id = offer['offerId']
    link = 'https://www.travelplanet.pl' + offer['offerUrl']
    country = offer['country']
    region = offer['region']
    hotel_name = offer['hotelName']
    trip_departure_name = offer['tripDepartureName']
    trip_duration = offer['tripDurationText']
    trip_dates = offer['tripDatesText']
    tour_operator = offer['touroperatorName']
    price_one_person = offer['priceOnePerson']

    return Offer(id, link, country, region, hotel_name, trip_departure_name, trip_duration, trip_dates, tour_operator,
                 price_one_person)


def connect_for_offer(country, page_number):
    url = "https://www.travelplanet.pl/json/wczasy/oferty"
    params = {'kierunek': country.id,
              'wylot': '01.04.2019',
              'przylot': '14.11.2019',
              'osoby': 2,
              'czas': '6:8',
              'dojazd': 'F',
              'sortowanie': 1,
              'kolejnosc': 'up',
              'limit': 25,
              'strona': page_number,
              'produkt': 1,
              'category': 'wczasy',
              'wyzywienie': 1,
              'ocena': 5
              }

    headers = {
        'Origin': 'https://www.travelplanet.pl',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'pl',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.140 Chrome/64.0.3282.140 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'https://www.travelplanet.pl/wczasy/oferty/2/?kierunek=14:&wylot=13.07.2018&przylot=02.08.2018&osoby=2&czas=6:8&dojazd=F&sortowanie=11&kolejnosc=down&limit=25',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive'
    }

    resp = requests.post(url, params=params, headers=headers)

    data = resp.json()

    count_offers = data['countOffers']

    if count_offers == 0:
        return

    count_pages = count_offers / 25

    print("Strona: " + str(page_number) + ", stron w sumie: " + str(count_pages))

    offers = data['offers']

    price = database.Database.getInstance().fetch_price()

    for offer in offers:
        if offer['category'] != 0:
            database.Database.getInstance().increase()
            print("https://www.travelplanet.pl" + offer['offerUrl'])
            print(str(offer['priceOnePerson']) + ', ' + offer['touroperatorName'])
            my_offer = create_offer(offer)
            country.add_offer(my_offer)
            if my_offer.price_one_person < price and database.Database.getInstance().offer_does_not_exists(my_offer):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                # email_content = my_offer.print()
                # email_sender.send(email_content)
                database.Database.getInstance().insert_founded_offer(my_offer)

    if count_pages > page_number:
        connect_for_offer(country, page_number + 1)
    pass


def search_travel():
    #connect_for_offer("15_176,15_93,15_2625,15_2635,15_55,15_50", 1)
     for i in range(54):
    #     # if i not in [38, 39]:
         connect_for_countries(i)
         for country in database.Database.getInstance().fetch():
             connect_for_offer(country, 1)

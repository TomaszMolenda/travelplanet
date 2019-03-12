class Offer(object):
    def __init__(self, id, link, country, region, hotel_name, trip_departure_name, trip_duration, trip_dates,
                 tour_operator, price_one_person):
        self.id = id
        self.link = link
        self.country = country
        self.region = region
        self.hotel_name = hotel_name
        self.trip_departure_name = trip_departure_name
        self.trip_duration = trip_duration
        self.trip_dates = trip_dates
        self.tour_operator = tour_operator
        self.price_one_person = price_one_person

    def print(self):
        return '{}\n\nPaństwo: {}\n\nRejon: {}\n\nHotel: {}\n\n' \
               'Lotnisko: {}\n\nIle dni: {}\n\n' \
               'Data: {}\n\nOrganizator: {}\n\nCena: {}'.format(self.link, self.country, self.region, self.hotel_name,
                                                                self.trip_departure_name,
                                                                self.trip_duration, self.trip_dates, self.tour_operator,
                                                                self.price_one_person)

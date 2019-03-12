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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.country == other.country \
                   and self.region == other.region \
                   and self.hotel_name == other.hotel_name \
                   and self.trip_departure_name == other.trip_departure_name \
                   and self.trip_duration == other.trip_duration \
                   and self.trip_dates == other.trip_dates \
                   and self.tour_operator == other.tour_operator \
                   and self.price_one_person == other.price_one_person
        else:
            return False

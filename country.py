class Country(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.offers = []
        self.price_sum = 0
        self.price_average = 0

    def add_offer(self, offer):
        if offer not in self.offers:
            self.offers.append(offer)
            self.price_sum = self.price_sum + offer.price_one_person
            self.price_average = self.price_sum / len(self.offers)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

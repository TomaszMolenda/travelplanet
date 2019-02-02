class Database:
    __instance = None
    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self
        self.countries = []
        self.counter = 0
        self.founded = 0

    def insert_country(self, country):
        self.countries.append(country)

    def fetch(self):
        return self.countries

    def increase(self):
        self.counter = self.counter + 1

    def mark_found(self):
        self.founded = self.founded + 1

    def fetch_counter(self):
        return self.counter

    def fetch_founded(self):
        return self.founded

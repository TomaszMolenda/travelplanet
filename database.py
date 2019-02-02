class Database:

    def __init__(self):
        self.test = []

    def insert(self, _id):

        self.test.append(_id)

    def fetch(self):
        return len(self.test)

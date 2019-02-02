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
        self.test = []

    def insert(self, _id):

        self.test.append(_id)

    def fetch(self):
        return len(self.test)

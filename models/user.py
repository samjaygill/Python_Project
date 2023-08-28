from models.destination import Destination


class User():

    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def full_details(self):
        all_details = (self.name, Destination(self.city), Destination(self.country))
        return all_details
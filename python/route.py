from city import City

class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = sum(a.distance(b) for a, b in zip(self.cities[1:],self.cities[:-1]))
        pass
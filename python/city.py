from dataclasses import dataclass
import math


@dataclass(eq=True, frozen=True)
class City:
    name: str
    x: int
    y: int

    def distance(self, other_city):
        xx = other_city.x - self.x
        yy = other_city.y - self.y

        return math.sqrt(xx**2 + yy**2)

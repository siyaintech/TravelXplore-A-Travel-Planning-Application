from data import cities
from utils import rotate_list

def generate_daily_plan(city, days):
    data = cities[city]
    itinerary = []
    for i in range(days):
        itinerary.append({
            "day": i + 1,
            "spot": rotate_list(data["spots"], i),
            "food": rotate_list(data["food"], i),
            "activity": rotate_list(data["things"], i)
        })
    return itinerary
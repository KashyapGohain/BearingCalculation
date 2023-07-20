import math
import numpy as np

def calculate_bearing(lat1, lon1, lat2, lon2):
    mlon = (lon2 - lon1)
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(mlon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.cos(math.radians(mlon))
    bearing = np.arctan2(x, y)
    initial_bearing = np.degrees(bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

first_latitude = float(input("Enter the first latitude: "))
first_longitude = float(input("Enter the first longitude: "))
second_latitude = float(input("Enter the second latitude: "))
second_longitude = float(input("Enter the second longtude: "))

if __name__ == "__main__":
    print("Calculated bearing of the locations is:", calculate_bearing(first_longitude,first_longitude,second_longitude,second_longitude),'Degree')

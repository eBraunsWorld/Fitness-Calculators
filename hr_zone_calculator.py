def heart_rate_zones(max_heart_rate):
    zones = {}
    zones["Zone 1"] = (int(0.5 * max_heart_rate), int(0.6 * max_heart_rate))
    zones["Zone 2"] = (int(0.6 * max_heart_rate), int(0.7 * max_heart_rate))
    zones["Zone 3"] = (int(0.7 * max_heart_rate), int(0.8 * max_heart_rate))
    zones["Zone 4"] = (int(0.8 * max_heart_rate), int(0.9 * max_heart_rate))
    zones["Zone 5"] = (int(0.9 * max_heart_rate), int(1.0 * max_heart_rate))
    return zones

while True:
    try:
        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError
        max_heart_rate = 220 - age
        heart_rate_zones = heart_rate_zones(max_heart_rate)
        print("Your max heart rate is", max_heart_rate)

        for zone in heart_rate_zones:
            print("{} is between {} and {} beats per minute.".format(zone, heart_rate_zones[zone][0], heart_rate_zones[zone][1]))
        break
    except ValueError:
        print("Error: please enter a positive whole number.")




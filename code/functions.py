from typing import Any


def req_params() :
    sfrom = "SW177TJ" #input("From: ")
    to =  "SW81JJ" #input("To: ")
    via=input("~~Preferences~~\n"
          "Via: ")
    date = input("Date (yyyyMMdd format): ")
    time = input("Time (HHmm format): ")
    mode = input("Modes of travel (Eg: public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle): ")
    preferences = input("Preferences(\"leastinterchange\" | \"leasttime\" | \"leastwalking\"): ")
    parameters0 ={"via":via,
                "mode":mode,
                "date":date,
                "time":time,
                "timeIs":"departing",
                 "preferences":preferences,
                "useRealTimeLiveArrivals" :True
                }
    parameters = {}
    for keys, values in parameters0.items():
        if isinstance(values, str):
            values = values.strip()
        if values != "" and values != None:
            parameters[keys] = values

    return [sfrom, to, parameters]

def display_journey(journey_data): # journey data is an element of the list returned by plan_journey
    print("Displaying journey...")
    print(
        f"\nDuration : {journey_data["duration"]}min"
        f"\nTotal cost: £{journey_data["Total Cost"]},"
        f"\nFrom {journey_data["From"]} to {journey_data["To"]}"
    )
    return 0 
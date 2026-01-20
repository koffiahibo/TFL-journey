import requests
import json

all_commands = ["help", "plan-journey", "check disruptions", "exit"]

close_ttbec = "51.434168, -0.162293"
close_alfc = "51.496212, 0.157618"
mofde = "public-bus"

def req_params():
    sfrom = input("From: ")
    to = input("To: ")
    via=input("~~Preferences~~\n"
          "Via: ")
    date = input("Date (yyyyMMdd format): ")
    time = input("Time (HHmm format): ")
    mode = input("Modes of travel (Eg: public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle): ")
    preferences = input("Preferences(\"leastinterchange\" | \"leasttime\" | \"leastwalking\"): ")
    parameters ={"via":via,
                "mode":mode,
                "date":date,
                "time":time,
                "timeIs":"departing",
                 "preferences":preferences,
                "useRealTimeLiveArrivals" :True
                }
    return [sfrom, to, parameters]
def plan_journey(sfrom, to, params):
    # via = None, mode = None, date = None, time = None, timeAD = None, live_time = None, journey_preferences = None)
    # via = None
    # mode = None
    # date = None
    # time = None
    # timeAD = None
    # live_time = None
    # journey_preferences = None

    print("Planning journey...")
    # Implementation
    journey_url = f"https://api.tfl.gov.uk/Journey/JourneyResults/{sfrom}/to/{to}"
    response = requests.get(journey_url, params=params)
    tex_req = json.loads(response.text)
    journeys=[]
    for journey in tex_req['journeys']:
        start_time = journey['startDateTime']
        end_time = journey['arrivalDateTime']
        duration = journey["duration"]
        try :
            total_cost = journey["fare"]["totalCost"]
            peak_fare = journey["fare"]["fares"][0]["peak"]
        except KeyError :
            total_cost = "N/A"
            peak_fare = "N/A"
        ##
        rleg = journey["legs"]
        legs=[]
        for leg in rleg:
            leg_dict = {"Duration": leg["duration"],
                   "Instruction Summary":leg["instruction"]["summary"],
                    "Mode": leg["mode"]["id"] }
            legs.append(leg_dict)
        ##
        journeys.append({"From": From, "To": To, "start time": start_time, "end time": end_time,
                         "duration": duration, "Total Cost": total_cost,
                         "Peak price": peak_fare, "legs":legs})
    return journeys # list of dictionnaries


def display_journeys(journey_data): # journey data is an element of the list returned by plan_journey
    print("Displaying journey...")
    print(
        f"\nDuration : {journey_data["duration"]}min"
        f"\nTotal cost: £{journey_data["Total Cost"]},"
        f"\nFrom {journey_data["From"]} to {journey_data["To"]}"
    )
    return
sfrom, to, params = req_params()
plan_journey(sfrom, to, params)
display_journeys(plan_journey(sfrom, to, params)[0])
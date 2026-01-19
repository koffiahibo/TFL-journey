import requests
import json

all_commands = ["help", "plan-journey", "check disruptions", "exit"]

close_ttbec = "51.434168, -0.162293"
close_alfc = "51.496212, 0.157618"
mofde = "public-bus"
def plan_journey(From, To, via=None, mode=None, date=None, time=None, timeAD=None, live_time=None, journey_preferences=None):
    # via = None
    # mode = None
    # date = None
    # time = None
    # timeAD = None
    # live_time = None
    # journey_preferences = None

    print("Planning journey...")
    # Implementation
    request = requests.get(" https://api.tfl.gov.uk/Journey/JourneyResults/{sfrom}/to/{to}".format(sfrom=From, to=To))
    tex_req = json.loads(request.text)
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
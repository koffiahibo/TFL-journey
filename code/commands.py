import requests
import json
from functions import *
from ValidData import *

all_commands = ["help", "plan-journey", "check disruptions", "exit"]

close_ttbec = "51.434168, -0.162293"
close_alfc = "51.496212, 0.157618"
mofde = "public-bus"


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
    print(response.request.url)
    tex_req = json.loads(response.text)
    journeys=[]
    for journey in tex_req['journeys']:
        start_time = journey['startDateTime']
        end_time = journey['arrivalDateTime']
        duration = journey["duration"]
        try :
            total_cost = journey["fare"]["totalCost"]/100
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
        journeys.append({"From": sfrom, "To": to, "start time": start_time, "end time": end_time,
                         "duration": duration, "Total Cost": total_cost,
                         "Peak price": peak_fare, "legs":legs})
    return journeys # list of dictionnaries




def arb():
    sfrom, to, params = req_params()
    for a in plan_journey(sfrom, to, params):
        display_journey(a)
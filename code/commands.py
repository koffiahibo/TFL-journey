import requests
import json

all_commands = ["help", "plan-journey", "check disruptions", "exit"]

close_ttbec = "51.434168, -0.162293"
close_alfc = "51.496212, 0.157618"
mofde = "public-bus,overground,train,tube"
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
    for i in range(len(tex_req['journeys'])):
        start_time = tex_req['journeys'][i]['startDateTime']
        end_time = tex_req['journeys'][i]['arrivalDateTime']
        duration = tex_req["journeys"][i]["duration"]
        try :
            total_cost = tex_req["journeys"][i]["fare"]["totalCost"]
            peak_fare = tex_req["journeys"][i]["fare"]["fares"][0]["peak"]
        except KeyError :
            total_cost = "N/A"
            peak_fare = "N/A"
        ##
        rleg = tex_req["journeys"][i]["legs"]
        legs=[]
        for j in range(len(rleg)):
            leg = {"Duration": rleg[j]["duration"],
                   "Instruction Summary":rleg[j]["instruction"]["summary"],
                    "Mode": rleg[j]["mode"]["id"] }
            legs.append(leg)
        ##
        journeys.append({"start time": start_time, "end time": end_time,
                         "duration": duration, "Total Cost": total_cost,
                         "Peak price": peak_fare, "legs":legs})
    return journeys # list of dictionnaries

def display_journey(journey_data):
    print("Displaying journey...")
    # Implementation
    for i in journey_data:
        print(
           i
        )
    return

a = plan_journey(close_ttbec, close_alfc)
print(a[0]["legs"])
# print(type(a))
# display_journey(a)
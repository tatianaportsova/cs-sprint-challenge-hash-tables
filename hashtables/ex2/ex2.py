# python3 hashtables/ex2/ex2_tests.py -v

#  Hint:  You may not need all of these.  Remove the unused functions.
import random

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tickets_cache = {}
    for i in range(len(tickets)):
        if tickets[i].source not in tickets_cache:
            tickets_cache[tickets[i].source] = tickets[i].destination

    route = []
    
    start = random.choice(list(tickets_cache.keys()))
    while start != "NONE":
        start = random.choice(list(tickets_cache.keys()))

    route.append(tickets_cache[start])

    stop = tickets_cache[start]
    while stop != "NONE":
        route.append(tickets_cache[stop])
        stop = tickets_cache[stop]
        
    # if route[-1] =="NONE":
    #     route.pop()
        
    return route

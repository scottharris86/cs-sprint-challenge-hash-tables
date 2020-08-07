#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []
    for item in tickets:
        cache[item.source] = item.destination

    for i in range(length):
        if i == 0:
            route.append(cache["NONE"])
        else:
            route.append(cache[route[i - 1]])
        
    return route

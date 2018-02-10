import copy

def routeCheck(start, end, citiesToll, cityConnections):
    # print(start, end)
    connections = []
    # create a copy of the cities array to hold the cheapest weight
    cheapestPathToCity = cities.copy()
    # create a copy of the cities array to hold visited values
    visited = cities.copy()
    # set the weight of the start point to 0
    cheapestPathToCity[start] = 0
    # variable to hold the cheapest route
    routeValue = None
    if cityConnections[start] is None:
        print("NO")
        return
    connections.append(start)
    # add the vertices from the starting city to the list
    for nextCity in cityConnections[start]:
        connections.append(nextCity)
        # add the weight of the cities into the paths list
        cheapestPathToCity[nextCity] = int(cities[nextCity])
    # loops until there are no more vertices to check
    while len(connections) > 0:
        # grabbing vertice from the front of the queue
        currentCity = connections[0]
        # if currentCity is the end point add its weight to the path list, don't add its vertices to the list
        if currentCity == end:
            routeValue = cheapestPathToCity[currentCity]
        else:
            # looping through the vertices of the current city
            for nextDestination in cityConnections[currentCity]:
                # if visited check the weight of the path, if the current path is smaller adjust the weight
                # and add the vertices back into the list. otherwise don't add it to the list
                if visited[nextDestination] < 0:
                    if int(cheapestPathToCity[nextDestination]) > (int(citiesToll[nextDestination]) + int(cheapestPathToCity[currentCity])):
                        cheapestPathToCity[nextDestination] = int(citiesToll[nextDestination]) + int(cheapestPathToCity[currentCity])
                        connections.append(nextDestination)
                else:
                        # the first time a vertice has been seen, adjust the weight and add it to the list
                        cheapestPathToCity[nextDestination] = int(citiesToll[nextDestination]) + int(cheapestPathToCity[currentCity])
                        connections.append(nextDestination)
                        # set the value to -1 to show its been visited
                        visited[nextDestination] = -1
        # remove the current city from list
        connections.pop(0)
    if routeValue is None:
        print("NO")
    else:
        print(routeValue)




if __name__ == '__main__':
    cityCount = int(input())
    cities = {}
    adjList = {}
    i = 0;
    # Create a dictionary that maps each city with a toll
    while i < cityCount:
        name, toll = input().split(" ")
        cities[name] = int(toll)
        adjList[name] = []
        i += 1
    highways = int(input())
    i = 0
    # Create an adjacency list for each city and what it points to
    while i < highways:
        city1, city2 = input().split(" ")
        adjList[city1].append(city2)
        i += 1
    trips = int(input())
    i = 0
    while i < trips:
        start, end = input().split(" ")
        routeCheck(start, end, cities, adjList)
        i += 1




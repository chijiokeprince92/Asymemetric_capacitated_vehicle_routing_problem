import random
from typing import List

routes = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]
capacity = 300

def asymmetric_cvrp_tabu_search(routes: List[List[int]], capacity: int) -> List[List[int]]:
    tabu_list = []
    best_routes = [[], []]
    best_cost = float('inf')

    for iteration in range(100): # set number of iterations
        # randomize routes
        random.shuffle(routes)

        # assign routes to vehicles
        vehicle1 = []
        vehicle2 = []
        for route in routes:
            if sum(vehicle1) + sum(route) <= capacity:
                vehicle1.append(route)
            else:
                vehicle2.append(route)

        # calculate cost and update best solution
        cost = len(vehicle1) + len(vehicle2)
        if cost < best_cost:
            best_routes = [vehicle1, vehicle2]
            best_cost = cost

            # add current solution to tabu list
            tabu_list.append(best_routes)
            if len(tabu_list) > 10: # set tabu list size
                tabu_list.pop(0)

        # check if best solution is in tabu list
        if best_routes in tabu_list:
            continue

        # perform tabu search
        for i in range(len(best_routes[0])):
            for j in range(len(best_routes[1])):
                new_routes = [best_routes[0][:i] + best_routes[1][j:] + best_routes[0][i+1:], best_routes[1][:j] + best_routes[0][i:] + best_routes[1][j+1:]]
                new_cost = len(new_routes[0]) + len(new_routes[1])
                if new_cost < best_cost and new_routes not in tabu_list:
                    best_routes = new_routes
                    best_cost = new_cost

    return best_routes

print(asymmetric_cvrp_tabu_search(routes, capacity))

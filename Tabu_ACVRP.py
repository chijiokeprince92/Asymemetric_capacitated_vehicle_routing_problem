# import the dependencies
import random
import math
import pandas as pd
import numpy as np

# initialize the Tabu_Search as a class declare all parameters.
class ACVRP_Tabu:
    def __init__(self, num_vehicles, capacities, demand, distance_matrix):
        self.num_vehicles = num_vehicles
        self.capacities = capacities
        self.demand = demand
        self.distance_matrix = distance_matrix

    # run the tabu_search and randomly generate a solution and assign it as the best solution 
    def tabu_search(self, max_iterations, tabu_list_size):
        best_solution = self.random_solution()
        best_cost = self.cost(best_solution)
        tabu_list = []
        # check if the best_neighbour is better than the current solution  and assign as the best_solution if it is.
        for iteration in range(max_iterations):
            current_solution = best_solution
            current_cost = best_cost
            neighbor_solution, neighbor_cost = self.best_neighbor(current_solution, tabu_list)
            if neighbor_cost < best_cost:
                best_solution = neighbor_solution
                best_cost = neighbor_cost
            # check if tabu_list is > tabu_list_size and remove the first element if it is
            if len(tabu_list) >= tabu_list_size:
                tabu_list.pop(0)
            tabu_list.append(current_solution)

        return best_solution, best_cost

    # get the initial solution, calculate the cost and append it to the tabu_list
    def random_solution(self):
        route = [[0] for i in range(self.num_vehicles)]
        unrouted = [each_demand for each_demand in range(1, len(self.demand))]
        random.shuffle(unrouted)

        for node in unrouted:
            for index, lane in enumerate(route):
                load = sum([self.demand[i] for i in lane])
                if load + self.demand[node] <= self.capacities[index]:
                    lane.append(node)
                    break

        return route
    # Get the best neighbour by checking which next move cost less
    def best_neighbor(self, solution, tabu_list):
        best_neighbor_solution = None
        best_neighbor_cost = math.inf

        for i in range(len(solution)):
            for j in range(len(solution)):
                if i == j:
                    continue
                neighbor_solution = self.move(solution, i, j)
                if neighbor_solution in tabu_list:
                    continue
                neighbor_cost = self.cost(neighbor_solution)
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor_solution = neighbor_solution
                    best_neighbor_cost = neighbor_cost

        return best_neighbor_solution, best_neighbor_cost
   
    # Get the next move 
    def move(self, solution, i, j):
        moved_node = solution[i][-1]
        new_solution = [r for r in solution]
        new_solution[i] = [node for node in solution[i] if node != moved_node]
        new_solution[j] = solution[j] + [moved_node]

        return new_solution

    def cost(self, route):
        # check if the elements in the route is less than 2 and return 0 because depot is the first element with value 0.
        if len(route) < 2:
            return float('inf')

        route_cost = 0
        for i in range(len(route) - 1):
            node1 = route[i]
            node2 = route[i+1]
            route_cost += self.distance_matrix[node1][node2]
        node1 = route[-1]
        node2 = 0
        route_cost += self.distance_matrix[node1][node2]

        return route_cost

if __name__ == "__main__":
    # Read the distance and deliveries with pandas and convert to a numpy array
    distance_matrix = pd.read_csv("distances.csv", index_col=0)
    demands = pd.read_csv("deliveries.csv", index_col=0)
    distances = np.array(distance_matrix.iloc[:, 1:])
    demands = np.array(demands).flatten()

    # Set the number of vehicles and capacity for each vehicle
    num_vehicles = int(input("Enter the number of vehicles: ")) # N = 2
    capacities = [int(input("Enter each vehicle capacity: "))] * num_vehicles
    max_iterations = 1000
    tabu_list_size = 100

    acvrp = ACVRP_Tabu(num_vehicles, capacities, demands, distance_matrix)
    best_solution, best_cost = acvrp.tabu_search(max_iterations, tabu_list_size)

    print("Best solution:", best_solution)
    print("Best cost:", best_cost)
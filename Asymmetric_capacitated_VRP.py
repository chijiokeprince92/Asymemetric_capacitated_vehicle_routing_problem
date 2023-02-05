import random
import numpy as np

class ACVRP:
    def __init__(self, n, m, demand, cost_matrix, tabu_list_length):
        self.n = n
        self.m = m
        self.demand = demand
        self.cost_matrix = cost_matrix
        self.tabu_list_length = tabu_list_length
        self.tabu_list = []
        self.current_route = []
        self.current_cost = 0

    def initial_solution(self):
        nodes = [i for i in range(1, self.n)]
        random.shuffle(nodes)
        self.current_route = [0] + nodes
        self.current_cost = self.cost(self.current_route)

    def cost(self, route):
        route_cost = 0
        for i in range(len(route) - 1):
            node1 = route[i]
            node2 = route[i+1]
            route_cost += self.cost_matrix[node1][node2]
        node1 = route[-1]
        node2 = 0
        route_cost += self.cost_matrix[node1][node2]

        return route_cost

    def is_feasible(self, route):
        capacity = 0
        for node in route:
            capacity += self.demand[node]
            if capacity > self.m:
                return False
        return True

    def get_best_neighbour(self):
        best_neighbour = None
        best_cost = float('inf')
        for i in range(len(self.current_route)):
            for j in range(i+1, len(self.current_route)):
                neighbour = self.current_route[:]
                neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
                if neighbour not in self.tabu_list and self.is_feasible(neighbour):
                    cost = self.cost(neighbour)
                    if cost < best_cost:
                        best_neighbour = neighbour
                        best_cost = cost
        return best_neighbour, best_cost

    def search(self):
        self.initial_solution()
        for i in range(100):
            best_neighbour, best_cost = self.get_best_neighbour()
            if best_cost < self.current_cost:
                self.current_route = best_neighbour
                self.current_cost = best_cost
                self.tabu_list.append(best_neighbour)
                if len(self.tabu_list) > self.tabu_list_length:
                    self.tabu_list.pop(0)

if __name__ == '__main__':
    n = 5
    m = 10
    demand = [0, 3, 2, 5, 2]
    cost_matrix = np.array([
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 20, 0, 19, 20],
        [20, 35, 0, 30, 15],
        [25, 25, 30, 0, 20],
        [30, 20, 15, 20, 0]
    ])
    tabu_list_length = 5

    acvrp = ACVRP(n, m, demand, cost_matrix, tabu_list_length)
    acvrp.search()

    print('Best route:', acvrp.current_route)
    print('Best cost:', acvrp.current_cost)

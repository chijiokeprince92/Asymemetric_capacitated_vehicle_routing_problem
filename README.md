The optimisation problem focuses on delivering items to customers from a central depot using multiple vehicles. The goal is to minimise the total distance travelled by all vehicles. To understand the Asymmetric Capacitated variant of the standard Vehicle Routing Problem, we must break the problem down into three distinct elements. 

The Vehicle Routing Problem (VRP) is closely related to the Travelling Salesman Problem except in a VRP there are multiple vehicles available for delivering to customers - not just 1. You must find a route for each vehicle around a subset of all available customers such that every customer is visited exactly once by only one of the vehicles. Each vehicle starts its route at a depot and must return there once all its customers have been visited. Think about what DPD, Amazon Prime or Hermes need to do every day when scheduling deliveries to its customers.

The asymmetric element of the problem refers to the idea that the time taken to travel from customer A to customer B may differ from the time taken to travel from customer B to customer A. The asymmetry becomes clear when you examine the distance matrix (see the example below).  

The capacitated element of the problem refers to the idea that each customer is awaiting the delivery of an item with a specific volume and that each vehicle has a maximum capacity for its delivery items. This effectively adds a bin packing constraint to the routing problem.

The "Tabu_ACVRP.py" file contains the code for multiple vehicles.

The "Asymmetric_capacitated.py" contains the code for finding the best route for a single vehicle.

The "deliveries.csv" file contains the customers orders.

The "distances.csv" file contains the distances between customers.
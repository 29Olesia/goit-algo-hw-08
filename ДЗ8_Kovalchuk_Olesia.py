import heapq

def min_cost_of_cable_connections(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        cost = cable1 + cable2
        total_cost += cost
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

cable_lengths = [4, 2, 8, 6]
result = min_cost_of_cable_connections(cable_lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")

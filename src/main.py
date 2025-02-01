import random
import math


# Визначення функції Сфери
def sphere_function(x):
  return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        next_solution = [current_solution[i] + random.uniform(-epsilon, epsilon) for i in range(len(bounds))]
        next_solution = [max(min(next_solution[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        next_value = func(next_solution)
        
        if next_value < current_value:
            current_solution, current_value = next_solution, next_value
        
        if abs(next_value - current_value) < epsilon:
            break
    
    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best_solution)
    
    for _ in range(iterations):
        candidate_solution = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate_solution)
        
        if candidate_value < best_value:
            best_solution, best_value = candidate_solution, candidate_value
        
        if abs(candidate_value - best_value) < epsilon:
            break
    
    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value
    
    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break
        
        next_solution = [current_solution[i] + random.uniform(-epsilon, epsilon) for i in range(len(bounds))]
        next_solution = [max(min(next_solution[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        next_value = func(next_solution)
        
        if next_value < current_value or random.uniform(0, 1) < math.exp((current_value - next_value) / temp):
            current_solution, current_value = next_solution, next_value
        
        if next_value < best_value:
            best_solution, best_value = next_solution, next_value
    
    return best_solution, best_value


if __name__ == "__main__":
  # Межі для функції
  bounds = [(-5, 5), (-5, 5)]

  # Виконання алгоритмів
  print("Hill Climbing:")
  hc_solution, hc_value = hill_climbing(sphere_function, bounds)
  print("Розв'язок:", hc_solution, "Значення:", hc_value)

  print("\nRandom Local Search:")
  rls_solution, rls_value = random_local_search(sphere_function, bounds)
  print("Розв'язок:", rls_solution, "Значення:", rls_value)

  print("\nSimulated Annealing:")
  sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
  print("Розв'язок:", sa_solution, "Значення:", sa_value)

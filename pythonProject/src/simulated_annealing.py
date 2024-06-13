import math
import random

from src.solution_service import SolutionService


class SimulatedAnnealing:
    def __init__(self, solution_service: SolutionService, limit=50, initial_temperature=5000, geometric_decay_factor=0.99):
        self.solution_service = solution_service
        self.current_solution = self.solution_service.random_solution()
        self.solutions_path = [self.current_solution]
        self.iterations_counter = 0
        self.idle_iterations_counter = 0
        self.k = limit
        self.initial_temperature = initial_temperature
        self.geometric_decay_factor = geometric_decay_factor
        self.temperature = self.initial_temperature
        self.best_solutions_path = None
        self.best_solution = None

    def run(self, n=1, randomize_after_each=False):
        while self.is_not_idle():
            self.iterate()
        self.best_solution = self.current_solution
        self.best_solutions_path = self.solutions_path
        for _ in range(n - 1):
            self.reset()
            if randomize_after_each:
                self.randomize_parameters()
            while self.is_not_idle():
                self.iterate()
            if self.solution_service.f(self.current_solution) < self.solution_service.f(self.best_solution):
                self.best_solution = self.current_solution
                self.best_solutions_path = self.solutions_path

    def iterate(self):
        candidate = self.solution_service.random_neighbour(self.current_solution)
        if (
                self.solution_service.f(candidate) < self.solution_service.f(self.current_solution)
                or random.random() < self.move_probability(candidate)
        ):
            self.current_solution = candidate
            self.idle_iterations_counter = 0
        else:
            self.idle_iterations_counter += 1
        self.lower_temperature()
        self.solutions_path.append(self.current_solution)
        self.iterations_counter += 1

    def is_not_idle(self):
        return self.idle_iterations_counter < self.k

    def move_probability(self, candidate):
        return math.exp(
            - abs(
                self.solution_service.f(self.current_solution) - self.solution_service.f(candidate)) / self.temperature
        )

    def reset(self):
        self.current_solution = self.solution_service.random_solution()
        self.solutions_path = [self.current_solution]
        self.iterations_counter = 0
        self.idle_iterations_counter = 0
        self.temperature = self.initial_temperature

    def randomize_parameters(self):
        self.temperature = random.randint(100, 1000)
        self.k = random.randint(20, 100)
        self.geometric_decay_factor = random.random() * 0.1 + 0.9

    def lower_temperature(self):
        self.temperature *= self.geometric_decay_factor

    def __str__(self):
        message = ''
        for solution in self.best_solutions_path:
            message += f'f({solution}) = {self.solution_service.f(solution)}\n'
        return message

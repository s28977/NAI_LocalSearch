import random
from copy import deepcopy

import numpy as np

from src.solution_service import SolutionService


class SalesmanPathService(SolutionService):
    def __init__(self):
        self.vertices_count = None
        self.adjacency_matrix = None

    def read_file(self, file):
        with open(file, "r") as f:
            lines = f.readlines()
            self.vertices_count = len(lines)
            self.adjacency_matrix = np.zeros((self.vertices_count, self.vertices_count), dtype=int)
            for i, line in enumerate(lines):
                line = line.strip()
                for j, n in enumerate(line.split(' ')):
                    self.adjacency_matrix[i][j] = int(n)

    def random_solution(self):
        path = []
        remaining_vertices = list(range(0, self.vertices_count))
        while len(remaining_vertices) > 0:
            next_vertex_index = random.randint(0, len(remaining_vertices) - 1)
            path.append(remaining_vertices.pop(next_vertex_index))
        return path

    def random_neighbour(self, path):  # some paths represent the same solution, is that a problem?
        new_path = deepcopy(path)
        rand = random.randint(0, self.vertices_count - 1)
        new_path[rand], new_path[rand - 1] = new_path[rand - 1], new_path[rand]
        return new_path

    def f(self, path):
        return sum([self.adjacency_matrix[path[i - 1]][path[i]] for i in range(0, self.vertices_count)])

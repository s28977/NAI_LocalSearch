import abc


class SolutionService(abc.ABC):
    @abc.abstractmethod
    def random_solution(self):
        pass

    @abc.abstractmethod
    def random_neighbour(self, solution):
        pass

    @abc.abstractmethod
    def f(self, solution):
        pass

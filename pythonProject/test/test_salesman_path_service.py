import numpy as np

from src.salesman_path_service import SalesmanPathService

test_data = r'test_data.txt'


def test_read_file():
    test_matrix = np.array(
        [[0, 2, 3, 4],
         [2, 0, 81, 55],
         [3, 81, 0, 3],
         [4, 55, 3, 0]], dtype=int
    )
    salesman = SalesmanPathService()
    salesman.read_file(test_data)
    assert np.array_equal(test_matrix, salesman.adjacency_matrix)


def test_random_solution():
    salesman = SalesmanPathService()
    salesman.read_file(test_data)
    solution1 = salesman.random_solution()
    solution2 = salesman.random_solution()
    assert solution1 != solution2
    assert sorted(solution1) == sorted(solution2) == list(range(0, salesman.vertices_count))


def test_f():
    salesman = SalesmanPathService()
    salesman.read_file(test_data)
    sample_path = [0, 1, 2, 3]
    sample_path_value = 4 + 2 + 81 + 3
    assert salesman.f(sample_path) == sample_path_value


def test_f_same_path():
    salesman = SalesmanPathService()
    salesman.read_file(test_data)
    sample_path = [0, 1, 2, 3]
    same_path = [1, 2, 3, 0]
    same_path_2 = [0, 3, 2, 1]
    assert salesman.f(sample_path) == salesman.f(same_path) == salesman.f(same_path_2)



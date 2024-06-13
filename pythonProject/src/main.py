import configparser

from src.salesman_path_service import SalesmanPathService
from src.simulated_annealing import SimulatedAnnealing

config = configparser.ConfigParser()
config.read(r'C:\Users\Jan\JetBrainsProjects\PycharmProjects\NAI\NAI_LocalSearch\pythonProject\config.ini')
file = config['PATH']['tsp_data_2']

salesman_path_service = SalesmanPathService()
salesman_path_service.read_file(file)
simulated_annealing = SimulatedAnnealing(salesman_path_service)
simulated_annealing.run(100)
print(str(simulated_annealing))

# f([2, 3, 4, 34, 33, 31, 30, 27, 18, 16, 12, 13, 17, 19, 21, 25, 26, 23, 9, 8, 35, 28, 29, 37, 39, 7, 6, 5, 32, 20, 24, 10, 11, 14, 15, 22, 36, 38, 1, 0, 41, 40]) = 1384 is my record
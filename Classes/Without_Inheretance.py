import matplotlib.pyplot as plt
import numpy as np
import random


np.set_printoptions(threshold = 1e6)
PHEROMONE_INIT = 1/1000
RHO = 0.02                      #evaporation rate
ALPHA = 1
BETA = 5
A = 4  #rate of pheromone limit
TOTAL_TIMES = 500
ITER_TIMES = 20


class City(object):

    city = {}
    city_num = 0
    dis = []                  #distance matrix
    pheromone = []
    pheromone_limit = [0, 0]        #pheromone_limit[0] is lower bound, pheromone_limit[1] is upper bound
    best_so_far = [np.inf, []]

    def __init__(self, city):
        self.city = city
        self.city_num = len(city)
        self.distance()
        self.pheromone = np.ones((self.city_num, self.city_num))*PHEROMONE_INIT


    def distance(self):
        self.dis = [[np.linalg.norm((np.array(self.city[column]) - np.array(self.city[row])), 2) \
                        for column in range(self.city_num)] for row in range(self.city_num)]


    def routine_distance(self, routine):
        distance = 0
        for i in range(self.city_num):
            distance = distance + np.array(self.dis)[routine[i], routine[i+1]]
        return distance


    def pheromone_trail(self, iter_best):
        delta_pheromone = 5/iter_best[0]
        iter_best_routine = iter_best[1]
        for i in range(self.city_num):
            departure = iter_best_routine[i]
            arrival = iter_best_routine[i + 1]
            self.pheromone[departure, arrival] = min(self.pheromone[departure, arrival] \
                                                     + delta_pheromone, self.pheromone_limit[1])
            self.pheromone[arrival, departure] = min(self.pheromone[arrival, departure] \
                                                     + delta_pheromone, self.pheromone_limit[1])


    def evaporation(self):
        for row in range(self.city_num):
            for column in range(self.city_num):
                self.pheromone[row, column] = max(self.pheromone[row, column]*(1-RHO),
                                                  self.pheromone_limit[0])


    def update_pheromone_limit(self):
        self.pheromone_limit[1] = 1/(RHO*self.best_so_far[0])
        self.pheromone_limit[0] = self.pheromone_limit[1]/A


    def aco(self):
        for i in range(TOTAL_TIMES):
            iter_best = [np.inf, []]

            for iter_times in range(ITER_TIMES):
#                departure_city = random.randint(0, self.city_num-1)
                departure_city = 1
                ant = Ant(list(self.city.keys()), departure_city)
                ant.move(self.pheromone, self.dis)
                routine = ant.routine
                distance = self.routine_distance(routine)
                if distance < iter_best[0]:
                    iter_best[0], iter_best[1] = distance, routine

            if iter_best[0] < self.best_so_far[0]:
                self.best_so_far[0], self.best_so_far[1] = \
                iter_best[0], iter_best[1]

            self.update_pheromone_limit()
            self.pheromone_trail(iter_best)
            self.evaporation()

        return self.best_so_far[0], self.best_so_far[1]


class Ant(object):

    departure_city = 0
    residual_city = []
    routine = []
    current_city = 0
    city_num = 0

    def __init__(self, city, departure_city):
        self.city_num = len(city)
        city.pop(departure_city)
        self.residual_city = city
        self.departure_city = departure_city
        self.current_city = departure_city
        self.routine = []
        self.routine.append(departure_city)


    def move(self, pheromone=None, distance=None):
        dis = distance + np.diag([1]*self.city_num)
        heuristic_information = 1/dis
        for _ in range(self.city_num-1):

            current_row = pheromone[self.current_city,:]
            current_row_distance = heuristic_information[self.current_city,:]

            residual_city_pheromone = [current_row[i] for i in self.residual_city]
            residual_city_distance = [current_row_distance[i] for i in self.residual_city]

            product = residual_city_pheromone*np.power(residual_city_distance, BETA)
            cumsum_residual_city_pheromone = np.cumsum(product)
            overall_pheromone = sum(product)
            random_num = random.uniform(0, overall_pheromone)

            for i in range(len(cumsum_residual_city_pheromone)):
                if random_num <= cumsum_residual_city_pheromone[i]:
                    destination = self.residual_city[i]
                    break

            self.routine.append(destination)
            self.current_city = destination
            destination_index = self.residual_city.index(destination)
            self.residual_city.pop(destination_index)
            if len(self.residual_city) == 0:
                self.routine.append(self.departure_city)


tsp_filename = 'Rakk.txt'
city_list = {}
x = []
y = []
with open(tsp_filename) as file:
    for fileline in file:
        v = fileline.strip().split(' ')
        city_list[int(v[0])] = [float(v[1]), float(v[2])]

city = City(city_list)
dis, routine = city.aco()

print(city.pheromone)
print(dis, routine)
print('max = , {0}, min = {1}'.format(city.pheromone_limit[0], city.pheromone_limit[1]))

opt_filename = 'Rakk.opt.tour'
opt_routine = []
with open(opt_filename) as opt_file:
    for opt_fileline in opt_file:
        opt_routine.append(int(opt_fileline))


for i in range(len(city_list)):
    position = city_list[i]
    x.append(position[0])
    y.append(position[1])

xl = [x[routine[i]] for i in range(len(routine))]
yl = [y[routine[i]] for i in range(len(routine))]
opt_xl = [x[opt_routine[i]] for i in range(len(opt_routine))]
opt_yl = [y[opt_routine[i]] for i in range(len(opt_routine))]

plt.figure()
plt.plot(x, y, 'o')
plt.plot(xl, yl)
#plt.plot(opt_xl, opt_yl)
plt.show()

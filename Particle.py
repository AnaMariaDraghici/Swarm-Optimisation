class Particle:
    def __init__(self, solution, speed):
        self.solution = solution
        self.speed = speed
        self.pb = solution

    def __str__(self):
        return f'{self.display_solution()} with fitness {self.get_solution_fitness()}'

    def get_solution_fitness(self):
        fitness = 0

        for nr in self.solution:
            fitness += nr * nr

        return fitness

    def get_pb_fitness(self):
        fitness = 0

        for nr in self.pb:
            fitness += nr * nr

        return fitness

    def display_solution(self):
        string = ''
        for nr in self.solution:
            string += f'{nr}, '
        return string[:-2]
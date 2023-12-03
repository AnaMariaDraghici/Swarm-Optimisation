from typing import List, Any
from Particle import Particle
import random
import numpy as np


class PSO:
    current_population: List[Particle]

    def __init__(self, dimensions: int, iterations: int, population_size: int,
                 inertia: float, cognitive: float, social: float, max_velocity: float):
        self.dimensions = dimensions
        self.iterations = iterations
        self.population_size = population_size
        self.inertia = inertia
        self.cognitive = cognitive
        self.social = social
        self.global_best = None
        self.current_population = []
        self.best_from_generation = []
        self.max_velocity = max_velocity

    def evolve(self):
        self.current_population = []
        self.best_from_generation = []

        self.initialise_population()

        for i in range(0, self.iterations):
            if i % 50 == 0:
                print()
            print(i, end=' ')

            if i % 5000 == 1:
                print()
                print(f'current global best is{Particle(self.global_best, 0)}')

            self.calculate_pbs()

            self.calculate_global_best()

            self.calculate_speed()
            self.move_particles()

            self.save_iteration_data()

        return Particle(self.global_best, 0)

    def initialise_population(self):
        for i in range(0, self.population_size):
            # generate a random point
            generated_solution = []
            for j in range(0, self.dimensions):
                generated_solution.append(random.uniform(-5.12, 5.12))

            self.current_population.append(Particle(np.array(generated_solution), 0.0))

    def calculate_pbs(self):
        for j in range(0, self.population_size):
            if self.current_population[j].get_solution_fitness() < self.current_population[j].get_pb_fitness():
                self.current_population[j].pb = self.current_population[j].solution

    def calculate_global_best(self):
        self.global_best = min(self.current_population, key=lambda x: x.get_pb_fitness()).pb

    def calculate_speed(self):
        for i in range(0, self.population_size):
            self.current_population[i].speed = self.get_speed(i)

    def get_speed(self, i):
        speed = self.inertia * self.current_population[i].speed + \
        self.cognitive * random.uniform(0, 1) * (
                self.current_population[i].pb - self.current_population[i].solution) + \
        self.social * random.uniform(0, 1) * (self.global_best - self.current_population[i].solution)
        return np.clip(speed, -self.max_velocity, self.max_velocity)

    def move_particles(self):
        for i in range(0, self.population_size):
            self.current_population[i].solution = self.current_population[i].solution + self.current_population[i].speed

    def save_iteration_data(self):
        self.best_from_generation.append(Particle(self.global_best, 0))

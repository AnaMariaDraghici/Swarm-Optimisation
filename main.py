import time

from PSO import PSO

"""
Functia sfera (aka Functia 1 De Jong)
f(x) = sum(xi^2)
"""


def print_menu():
    print("1.Raport k PSO")
    print("x.Exit\n")


def main():
    while True:
        print_menu()
        option = input()

        if option == "1":
            handle_raport_k_pso()

        elif option == "x":
            print("\ncya")
            break

        else:
            print("\nwhat?")


def handle_raport_k_pso():
    k = input('\nhow many? ')
    solutions = []
    generations_best = []
    iterations = 10
    population_size = 10
    inertia = 1
    cognitive = 1
    social = 3
    max_velocity = 0.2

    pso = PSO(
        dimensions=2,
        iterations=iterations,
        population_size=population_size,
        inertia=inertia,
        cognitive=cognitive,
        social=social,
        max_velocity=max_velocity
    )

    best_run_index = 0
    best_fitness = 999999999
    worst_fitness = 0
    total_fitness = 0

    print(f'\ngenerating {k} solutions:\n')
    f_b = open("current_run_best.txt", "w")
    start_time = time.time()
    for i in range(0, int(k)):
        print('generations:', end=' ')
        solution = pso.evolve()
        solutions.append(solution)

        # save data to file
        f_b.write(f'------------------RUN {i + 1}:\n')
        for value in pso.best_from_generation:
            f_b.write(f'{value.get_solution_fitness()}\n')

        # calculate running best and worst and average
        total_fitness += solution.get_solution_fitness()

        if best_fitness > solution.get_solution_fitness():
            best_fitness = solution.get_solution_fitness()
            best_run_index = i

        if solution.get_solution_fitness() > worst_fitness:
            worst_fitness = solution.get_solution_fitness()

        # save data
        generations_best.append(pso.best_from_generation)

        print(f'\n\nbest of run {i + 1}:\n{solution}\n')

    f_b.close()

    print(f'\nbest one is #{best_run_index + 1}\n{solutions[best_run_index]}')
    print(f'the worst one is {worst_fitness}')
    print(f'the average is {total_fitness / int(k)}')

    print(f'\nall in {time.time() - start_time} seconds\n')


main()

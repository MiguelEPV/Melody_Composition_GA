import random
import math
import copy
import csv
import numpy as np
from indiv import Individual
from operator import attrgetter


class GeneticAlgorithm:

    def __init__(self, pop_size=250, off_size=250,
                 generations=500, mutation=0.01, crossover_rate=1, tourney_size=2, duration_prob=40, pitch_prob=60,
                 chord_prog=["C", "G", "Am", "F"], filename="examples/example1"):

        self.pop_size = pop_size
        self.off_size = off_size
        self.tourney_size = tourney_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.chord_prog = chord_prog
        self.indv_size = len(chord_prog) * 8
        self.duration_prob = duration_prob
        self.pitch_prob = pitch_prob
        self.mutation = mutation
        self.filename = filename

    def initialize_population(self):
        init_pop = []
        for i in range(0, self.pop_size):
            init_pop.append(Individual())
            init_pop[i].create_initial_melody_random_notes()
            init_pop[i].evaluate_melody_2(self.chord_prog)

        return init_pop

    def parent_tournament(self, population):
        parents = []
        for _ in range(0, self.off_size):
            current_winner = 0
            current_best = 0
            for j in range(0, self.tourney_size):
                contestant = random.randint(0, self.pop_size - 1)
                new_value = population[contestant].fitness
                if new_value >= current_best:
                    current_best = new_value
                    current_winner = contestant

            parents.append(population[current_winner])

        return parents

    def random_parents(self, population):
        parents = random.choices(population, k=self.off_size)
        return parents

    def crossover(self, parents):
        offspring = copy.deepcopy(parents)
        for i in range(0, self.off_size, 2):
            cross_prob = random.uniform(0, 1)
            if cross_prob < self.crossover_rate:
                choose_cross = random.randint(0, 1)
                if choose_cross == 0:
                    self.two_point_crossover(offspring[i], offspring[i + 1])
                else:
                    self.measure_crossover(offspring[i], offspring[i + 1])

            # self.uniform_crossover(offspring[i], offspring[i+1])
            self.mutate(offspring[i])
            self.mutate(offspring[i + 1])
            offspring[i].get_melody_notes()
            offspring[i + 1].get_melody_notes()
            offspring[i].evaluate_melody_2(self.chord_prog)
            offspring[i + 1].evaluate_melody_2(self.chord_prog)
        return offspring

    def mutate(self, offspring):
        mutation_types = ["modulate", "duration"]
        for i, note in enumerate(offspring.melody):
            mutation_prob = random.uniform(0, 1)
            if mutation_prob <= self.mutation:
                mutation_result = random.choices(mutation_types, weights=(self.pitch_prob, self.duration_prob), k=1)

                if mutation_result[0] == "modulate":
                    offspring.melody[i] = self.pitch_modulation(offspring.melody[i])
                elif mutation_result[0] == "duration":
                    if i == 0:
                        continue
                    if note == 0:
                        offspring.melody[i] = random.randint(1, 24)
                    else:
                        offspring.melody[i] = 0

    def pitch_modulation(self, note):

        modulate = random.choice([-2, 2])
        if note + modulate < 1:
            note -= modulate
        elif note + modulate > 23:
            note -= modulate
        else:
            note += modulate
        return note

    def two_point_crossover(self, child1, child2):

        p1 = random.randint(0, self.indv_size)
        p2 = random.randint(0, self.indv_size)
        if p1 < p2:
            child1.melody[p1:p2], child2.melody[p1:p2] = child2.melody[p1:p2], child1.melody[p1:p2]
        elif p1 > p2:
            child1.melody[p2:p1], child2.melody[p2:p1] = child2.melody[p2:p1], child1.melody[p2:p1]
        else:
            if p1 == 32:
                p1 = 31
            child1.melody[p1], child2.melody[p1] = child2.melody[p1], child1.melody[p1]

    def uniform_crossover(self, child1, child2):

        for i in range(0, len(child1.melody)):
            cross_prob = random.uniform(0, 1)
            if cross_prob <= self.crossover_rate:
                child1.melody[i], child2.melody[i] = child2.melody[i], child1.melody[i]

    def measure_crossover(self, child1, child2):
        measure = random.randint(1, 4)

        if measure == 1:
            child1.melody[0:8], child2.melody[0:8] = child2.melody[0:8], child1.melody[0:8]
        elif measure == 2:
            child1.melody[8:16], child2.melody[8:16] = child2.melody[8:16], child1.melody[8:16]
        elif measure == 3:
            child1.melody[16:24], child2.melody[16:24] = child2.melody[16:24], child1.melody[16:24]
        else:
            child1.melody[24:32], child2.melody[24:32] = child2.melody[24:32], child1.melody[24:32]

    def selection(self, population, offspring):
        intermediate_pop = population + offspring
        intermediate_pop.sort(reverse=True, key=lambda x: x.fitness)
        return intermediate_pop[0:self.pop_size]

    def run_genetic_algorithm(self):
        stats = {"best_fitness": 0,
                 "mean_fitness": 0,
                 "best_gen": 0,
                 "std_dev": 0,
                 "best_fitness_it": [],
                 "mean_fitness_it": [],
                 "generations": 0,
                 "evaluations": 0
                 }

        population = self.initialize_population()
        best_fit_indiv = max(population, key=attrgetter('fitness'))
        best_fit = best_fit_indiv.fitness
        overall_best = best_fit
        average_fit = np.mean([x.fitness for x in population])
        stdv_mean = np.std([x.fitness for x in population])
        stats["best_fitness"] = best_fit
        stats["mean_fitness"] = average_fit
        stats["best_fitness_it"].append(best_fit)
        stats["mean_fitness_it"].append(average_fit)
        stats["evaluations"] = self.pop_size
        print("Initial Generation: ")
        print("Best Fitness = ", best_fit)
        print("Average Fitness = ", average_fit)
        # self.save_stats(0, best_fit, average_fit, stdv_mean, stats["evaluations"], best_fit_indiv)
        for i in range(0, self.generations):
            parents = self.parent_tournament(population)
            children = self.crossover(parents)
            stats["evaluations"] += self.off_size
            population = self.selection(population, children)
            best_fit = population[0].fitness
            best_fit_indiv = population[0]
            average_fit = np.mean([x.fitness for x in population])
            stdv_mean = np.std([x.fitness for x in population])
            # self.save_stats(i, best_fit, average_fit, stdv_mean, stats["evaluations"], best_fit_indiv)
            if best_fit > overall_best:
                overall_best = best_fit
                stats["best_gen"] = i
            stats["best_fitness"] = best_fit
            stats["mean_fitness"] = average_fit
            stats["best_fitness_it"].append(best_fit)
            stats["mean_fitness_it"].append(average_fit)
            rounded_best = round(best_fit,10)
            rounded_avg = np.round(average_fit, 10)
            average_fit = average_fit.item()
            stats["generations"] = i
            print("Generation: ", i)
            print("Best Fitness = ", best_fit)
            print("Average Fitness = ", average_fit)
            if math.isclose(rounded_best, 1.0):
                break
        best_indiv = population[0]
        # best_indiv.save_melody(self.chord_prog, self.filename)
        # best_indiv.play_melody(self.chord_prog)
        return stats

    def save_stats(self, iteration, best, mean, stdv, evaluations, indiv):
        FILEPATH = "./test_results/evolution_C-G-Am-F-2.csv"
        res = [iteration, best, mean, stdv, evaluations]
        indiv.save_melody(self.chord_prog, "melody_evolution_C-G-Am-F-2/" + "gen_" + str(iteration))
        with open(FILEPATH, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(res)



# ga1 = GeneticAlgorithm()
# results = ga1.run_genetic_algorithm()






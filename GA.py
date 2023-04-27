import random
import copy
import numpy as np
from indiv import Individual
from music21 import *
from music import *
from operator import attrgetter


class GeneticAlgorithm:

    def __init__(self, pop_size=500, off_size=500, tourney_size=0.2,
                 generations=500, mutation=0.1, rand_note_prob=0.00, duration_prob=50, pitch_prob=50,
                 crossover_rate=0.9, chord_prog=["C", "A", "G", "F"]):

        self.pop_size = pop_size
        self.off_size = off_size
        self.tourney_size = int(pop_size * tourney_size)
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.chord_prog = chord_prog
        self.indv_size = len(chord_prog) * 8
        self.random_note_prob = rand_note_prob
        self.duration_prob = duration_prob
        self.pitch_prob = pitch_prob
        self.mutation = mutation

    def initialize_population(self):
        init_pop = []
        for i in range(0, self.pop_size):
            init_pop.append(Individual())
            # init_pop[i].create_initial_melody_chords(self.chord_prog)
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
        parents = random.choices(population, k=self.pop_size)
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
                        offspring.melody[i] = random.randint(1, 23)
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
                 "std_dev": 0,
                 "best_fitness_it": [],
                 "mean_fitness_it": []

                 }
        population = self.initialize_population()
        best_fit_indiv = max(population, key=attrgetter('fitness'))
        best_fit = best_fit_indiv.fitness
        average_fit = np.mean([x.fitness for x in population])
        stats["best_fitness"] = best_fit
        stats["mean_fitness"] = average_fit
        stats["best_fitness_it"].append(best_fit)
        stats["mean_fitness_it"].append(average_fit)
        for i in range(0, self.generations):
            print("Generation: ", i)
            print("Best Fitness = ", best_fit)
            print("Average Fitness = ", average_fit)
            # parents = self.parent_tournament(population)
            parents = self.random_parents(population)
            children = self.crossover(parents)
            population = self.selection(population, children)
            best_fit = population[0].fitness
            average_fit = np.mean([x.fitness for x in population])
            stats["best_fitness"] = best_fit
            stats["mean_fitness"] = average_fit
            stats["best_fitness_it"].append(best_fit)
            stats["mean_fitness_it"].append(average_fit)
        population[0].play_melody(self.chord_prog)
        phenotype = genotype_translation(population[0].melody)
        # print(phenotype)
        # for i in phenotype:
        #     print(i[0], end=",")
        best_indiv = population[0]
        print("Best Individual Objective Values")
        print("O1: ", best_indiv.o1)
        print("O2: ", best_indiv.o2)
        print("O3: ", best_indiv.o3)
        print("O4: ", best_indiv.o4)
        print("O5: ", best_indiv.o5)
        print("O6: ", best_indiv.o6)
        print("O7: ", best_indiv.o7)
        print("O8: ", best_indiv.o8)
        print("O9: ", best_indiv.o9)
        print("O10: ", best_indiv.o10)
        print("O11: ", best_indiv.o11)
        return stats


# ga1 = GeneticAlgorithm()
# ga1.run_genetic_algorithm()
# for i in range(0,len(parent)):
#     print("Parent")
#     print(parent[i].melody)
#     print(parent[i].fitness)
#     print("Child")
#     print(child[i].melody)
#     print(child[i].fitness)

0.8157603686635945
0.8157603686635947

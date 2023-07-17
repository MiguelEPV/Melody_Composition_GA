import json
import csv
import time
import matplotlib.pyplot as plt
import numpy as np
from GA import GeneticAlgorithm


RES_FILEPATH = "./test_results/results.csv"

average_pop_fitness = []
best_fitness = []
execution_time = []
json_file = open("./test_data/tests_crossover.json")
test_values = json.load(json_file)

for key, value in test_values.items():
    GRAPH_FILEPATH = "./graphs/crossover/"+key
    average_pop_fitness = []
    best_fitness = []
    execution_time = []
    evaluations = 0
    ga_test = GeneticAlgorithm(value["population"], value["offspring"], value["generations"],
                               value["mutation"], value["crossover"], filename="crossover/" + key)

    for _ in range(10):
        st = time.time()
        stats = ga_test.run_genetic_algorithm()
        et = time.time()
        total_time = et - st
        evaluations = stats["evaluations"]
        average_pop_fitness.append(stats["mean_fitness"])
        best_fitness.append(stats["best_fitness"])
        execution_time.append(total_time)

    avg_fitness = np.mean(average_pop_fitness)
    std_af = np.std(average_pop_fitness)
    avg_best_fitness = np.mean(best_fitness)
    std_bf = np.std(best_fitness)
    avg_time = np.mean(execution_time)
    std_time = np.std(execution_time)

    res = [value["population"], value["offspring"], value["generations"],
           value["mutation"], value["crossover"],
           avg_fitness, std_af, avg_best_fitness, std_bf, avg_time, std_time, evaluations]

    with open(RES_FILEPATH, 'a', newline="") as f:

        writer = csv.writer(f)
        writer.writerow(res)

    plt.plot(range(ga_test.generations + 1), stats["best_fitness_it"], color='#800080')
    plt.title("Evolution of the best fitness value")
    plt.ylabel("Fitness Value")
    plt.xlabel("Generation")
    plt.grid()
    plt.savefig(GRAPH_FILEPATH + "-best_fit" + ".jpg")
    plt.close()

    plt.plot(range(ga_test.generations + 1), stats["mean_fitness_it"], color='#800080')
    plt.title("Evolution of the mean fitness value")
    plt.ylabel("Fitness Value")
    plt.xlabel("Generation")
    plt.grid()
    plt.savefig(GRAPH_FILEPATH + "-mean_fit" + ".jpg")
    plt.close()

    plt.plot(range(ga_test.generations + 1), stats["mean_fitness_it"], label="mean fitness", color='#800080')
    plt.plot(range(ga_test.generations + 1), stats["best_fitness_it"], label="best fitness", color='#29e37d')
    plt.title("Comparison of evolution between best and mean fitness value")
    plt.ylabel("Fitness Value")
    plt.xlabel("Generation")
    plt.grid()
    plt.legend()
    plt.savefig(GRAPH_FILEPATH + "-mean_vs_best_fit" + ".jpg")
    plt.close()

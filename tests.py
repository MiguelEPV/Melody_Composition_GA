import json
import csv
import matplotlib.pyplot as plt
from GA import GeneticAlgorithm

FILEPATH = "./graphs/"
FILENAME = "test-1"

ga_test = GeneticAlgorithm()
stats = ga_test.run_genetic_algorithm()

plt.plot(range(ga_test.generations + 1), stats["best_fitness_it"], color='#800080')
plt.title("Evolution of the best fitness value")
plt.ylabel("Fitness Value")
plt.xlabel("Generation")
plt.grid()
plt.savefig(FILEPATH + "best_fit" + ".jpg")
plt.close()

plt.plot(range(ga_test.generations + 1), stats["mean_fitness_it"], color='#800080')
plt.title("Evolution of the mean fitness value")
plt.ylabel("Fitness Value")
plt.xlabel("Generation")
plt.grid()
plt.savefig(FILEPATH + "mean_fit" + ".jpg")
plt.close()

plt.plot(range(ga_test.generations + 1), stats["mean_fitness_it"], label="mean fitness", color='#800080')
plt.plot(range(ga_test.generations + 1), stats["best_fitness_it"], label="best fitness", color='#29e37d')
plt.title("Comparison of evolution between best and mean fitness value")
plt.ylabel("Fitness Value")
plt.xlabel("Generation")
plt.grid()
plt.legend()
plt.savefig(FILEPATH + "mean_vs_best_fit" + ".jpg")
plt.close()

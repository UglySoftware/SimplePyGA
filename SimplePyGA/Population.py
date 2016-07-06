# Python library imports
import copy
import random

# SimplePyGA imports
import Gene
import Individual
import FitnessCalc

# Constants
POPULATION_SIZE_DEFAULT = 20

# Population base class
class Population(object):
    """The population of individuals to evolve using GA"""

    breedingPoolSize = 3

    def __init__(   self,
                    popSize = POPULATION_SIZE_DEFAULT,
                    IndividualClass = Individual.Individual,
                    fitnessCalc = FitnessCalc.FitnessCalc()):
        self.IndividualClass = IndividualClass
        self.fitnessCalc = fitnessCalc
        self.individuals = [self.IndividualClass() for i in range(popSize)]

    def size(self):
        return len(self.individuals)

    def mutate(self):
        for i in self.individuals:
            i.mutate()

    def selectForBreeding(self):
        selectedIndices = [random.randrange(0, self.size() - 1) for i in range(self.breedingPoolSize)]
        return [self.individuals[i] for i in selectedIndices]

    def evolve(self, goal):
        for i in range(self.size()):
            parent1 = FitnessCalc.getFittest(self.selectForBreeding(), goal, self.fitnessCalc)
            parent2 = FitnessCalc.getFittest(self.selectForBreeding(), goal, self.fitnessCalc)
            self.individuals[i] = Individual.breed(parent1, parent2)
        self.mutate()

    def printPop(self, goal):
        for i in self.individuals:
            print i.toString(), ":", self.fitnessCalc.getFitness(i, goal)

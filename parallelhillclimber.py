import constants as c
from solution import SOLUTION
import copy
import os
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del body*.urdf")
        os.system("del fitness_*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        self.randomSeed = c.randomSeed
        self.graph = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, self.randomSeed)
            # print(self.nextAvailableID, 'init')
            self.nextAvailableID += 1
            self.graph[i] = []
    def EVOLVE(self):
        self.Evaluate(self.parents)
            # print("\nFITNESS: " + str(self.parents[parent].fitness))
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Show_Best(self):
        lowest_parent = self.parents[0]
        d = 0
        for i in self.parents.keys():
            if self.parents[i].fitness > lowest_parent.fitness:
                lowest_parent = self.parents[i]
                d = i
        # print('\n Lowest fitness: ' + str(lowest_parent.fitness) + '\n')
        print(self.graph[d])
        input("start")
        lowest_parent.Start_Simulation('GUI')
        # x = [i for i in range(0, c.numberOfGenerations)]
        # for i in self.graph.keys():
        #     plt.plot(x, [-j for j in self.graph[i]])
        # plt.legend()
        plt.show()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print('\n')        
        # self.Print()
        print('\n')
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents.keys():
            self.children[parent] = copy.deepcopy(self.parents[parent])
            # print(self.nextAvailableID, 'spawn')
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation('DIRECT')
        for i in solutions: 
            solutions[i].Wait_For_Simulation_To_End()
        
    def Print(self):
        for i in self.parents.keys():
            print("\nParent: " + str(self.parents[i].fitness) + " Child: " + str(self.children[i].fitness))

    def Select(self):
        for i in self.parents.keys():
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]
            self.graph[i].append(self.parents[i].fitness)

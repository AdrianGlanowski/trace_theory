import networkx as nx
from no_more_equations_exception import NoMoreEquationsException
from equation import Equation
from exporter import Exporter

class Solution:
    def __init__(self, file_name):
        self.file_name = file_name
        self.equations = []
        with open(f"examples/{file_name}.txt", "r") as f:
            while True:
                line = f.readline()
                try:
                    self.equations.append(Equation(line))
                except NoMoreEquationsException:
                    word = f.readline().replace(" ", "").split("=")[1]
                    break
                
        self.word = word
    
    def create_dependency_relation(self):
        self.dependent = []
        for i in range(len(self.equations)):
            for j in range(i, len(self.equations)):
                eq1 = self.equations[i]
                eq2 = self.equations[j]
                
                eq1_all_variables = set(eq1.left) | set(eq1.right)
                eq2_all_variables = set(eq2.left) | set(eq2.right)
                
                if self.equations[i].left in eq2_all_variables or self.equations[j].left in eq1_all_variables:
                    self.dependent.append((eq1, eq2))
        
    def create_independency_relation(self):
        self.independent = [(self.equations[i], self.equations[j]) 
                            for i in range(len(self.equations)) 
                                for j in range(i+1, len(self.equations)) 
                                    if (self.equations[i], self.equations[j]) not in self.dependent]

    def create_graph(self):
        edges = []
        for i in range(len(self.word)):
            for j in range(i+1, len(self.word)):
                if (self.word[i], self.word[j]) in map(lambda x: (x[0].action, x[1].action), self.dependent) or (self.word[j], self.word[i]) in map(lambda x: (x[0].action, x[1].action), self.dependent):
                    edges.append((i, j))

        #reduction of pointless edges based on transitivity of dependency relation
        self.graph = nx.transitive_reduction(nx.DiGraph(edges))

        self.labels = {i: w for i, w in enumerate(self.word)}

    def create_FNF(self):
        self.topology = list(nx.topological_generations(self.graph))

        topology_layer = ["".join(map(lambda x: self.word[x], array)) for array in self.topology]
        all_layers = [f"({"".join(x)})" for x in topology_layer]
        self.fnf_string = "".join(all_layers)

    def solve(self):
        self.create_dependency_relation()
        self.create_independency_relation()
        self.create_graph()
        self.create_FNF()
        self.export_results()
        
    def export_results(self):
        exporter = Exporter(self)
        exporter.export_results()
            
    def __repr__(self):
        return f"{"\n".join([str(x) for x in self.equations])}"
import networkx as nx
import matplotlib.pyplot as plt
import os

class Exporter:

    def __init__(self, solution):
        self.solution = solution

    def dag_layout(self, G):
        """
            Graph layout that uses topological generations,
            nodes from the same generation are on the same level
        """
        
        layers = list(nx.topological_generations(G))
        pos = {}
        for i, layer in enumerate(layers):
            for j, node in enumerate(layer):
                pos[node] = (j, -i)
        return pos

    def show_graph(self):
        """Save graph as a .png file, then display it for user"""
        _, ax = plt.subplots(figsize=(10, 8))
        nx.draw(self.solution.graph, pos=self.dag_layout(self.solution.graph), with_labels=True, labels=self.solution.labels, arrows=True)
        ax.set_title(f"Dependency graph for {self.solution.file_name}") 
        plt.savefig(f"output/{self.solution.file_name}/{self.solution.file_name}.png")
        if not self.solution.test:
            plt.show()

    def graph_dot_format(self):
        """Convert graph to dot format"""
        edges = self.solution.graph.edges()
        edges_str = "\n".join(f"{u+1} -> {v+1}" for u, v in edges) #1 based indexing
        labels_str = "\n".join(f"{i+1}[label={w}]" for i, w in self.solution.labels.items()) #1 based indexing
        return f"digraph g{{\n{edges_str}\n{labels_str}\n}}"

    def fnf_string_format(self):
        """Convert to string like (equation+)* where equation belongs in A"""
        self.solution.topology_layer = ["".join(map(lambda x: self.solution.word[x], array)) for array in self.solution.topology]
        all_layers = [f"({"".join(x)})" for x in self.solution.topology_layer]
        return "".join(all_layers)

    def export_results(self):
        """Export results to .txt file and show created graph."""
        os.makedirs(f"output/{self.solution.file_name}", exist_ok=True)
        with open(f"output/{self.solution.file_name}/{self.solution.file_name}.txt", "w+") as f:
            #dependency
            f.write("D = {" + ", ".join(f"({a.action}, {b.action})" for a, b in self.solution.dependent) + "}\n")
            #independency
            f.write("I = {" + ", ".join(f"({a.action}, {b.action})" for a, b in self.solution.independent) + "}\n")
            #FNF
            f.write(f"FNF({self.solution.word}) = {self.fnf_string_format()}\n")
            #graph
            f.write(self.graph_dot_format())
            f.close()
        
        self.show_graph()
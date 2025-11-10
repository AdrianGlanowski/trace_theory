import os

class Exporter:

    def __init__(self, solution):
        self.solution = solution

    def export_results(self):

        
        os.makedirs(f"output/{self.solution.file_name}", exist_ok=True)
        with open(f"output/{self.solution.file_name}/{self.solution.file_name}.txt", "w+") as f:
            #dependency
            f.write("D = {" + ", ".join(f"({a.action}, {b.action})" for a, b in self.solution.dependent) + "}\n")
            #independency
            f.write("I = {" + ", ".join(f"({a.action}, {b.action})" for a, b in self.solution.independent) + "}\n")
            #FNF
            f.write(f"FNF({self.solution.word}) = {self.solution.fnf_string}\n")
            #graph
            f.write(self.solution.graph_dot_format())
            f.close()

        self.solution.show_graph()
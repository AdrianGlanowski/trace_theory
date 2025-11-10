from no_more_equations_exception import NoMoreEquationsException
import re


class Equation:

    def __init__(self, line: str):
        values = self.parse(line)
        self.action = values[0]
        self.left = values[1]
        self.right = values[2]

    def parse(self, line: str):
        line = line.replace(" ", "")
        variable = r"[a-z]"
        multiplied_variable = fr"\d*{variable}"
        operator = r"(\+|-|\\|\*)"

        full_pattern = re.compile(fr"\((?P<action>{variable})\)(?P<left>{variable}):={multiplied_variable}({operator}{multiplied_variable})*")
        
        match = full_pattern.match(line)
        if match is None: 
            raise NoMoreEquationsException
        
        dict_val = match.groupdict()
        variable_list = []
        variables = re.finditer(variable, line.split(":=")[1])
        for variable_match in variables:
            char = variable_match.group()[-1]
            variable_list.append(char)

        return dict_val["action"], dict_val["left"], variable_list

    def full_repr(self):
        return f"({self.action}) {self.left} := {self.right}"

    def __repr__(self):
        return f"{self.action}"
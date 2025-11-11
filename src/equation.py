from no_more_equations_exception import NoMoreEquationsException
import re


class Equation:

    def __init__(self, line: str):
        values = self.parse(line)
        self.action = values[0]
        self.left = values[1]
        self.right = values[2]

    
    def parse(self, line: str):
        """ Parser for .txt file input.
            Format of said file in regex-like interpretation:
            (action_1) left_1 := right_1
            ...
            (action_n) left_n := right_n
            A = {action_1, action_2, ..., action_n}
            w = [action_1, action_2, ..., action_n]+

            where left_i is variable name
            and right_i is a series of variables multiplied by numbers, 
            serpated by basic mathematical operator.
            
            When the NoMoreEquationsException is raised, 
            that means A = {action_1, action_2, ..., action_n},
            so another line is read to aquire word w.
        """

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

    def __repr__(self):
        return f"{self.action}"
import re

def evalform(formula, *args):
    variable = sorted(set(re.findall(r'[a-zA-Z]+', formula)))
    namespace = {}
    for var, value in zip(variable, args):
        namespace[var] = value

    return eval(formula, namespace)
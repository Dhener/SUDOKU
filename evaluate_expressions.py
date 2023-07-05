import math
class ExpBinaries:
    def __init__(self, exp_before, operator, exp_after):
        self.tag = "Binaries"
        self.exp_before = exp_before
        self.operator = operator
        self.exp_after = exp_after

class ExpUnary:
    def __init__(self, exp):
        self.tag = "Unary"
        self.exp = exp

class ExpEmpty:
    def __init__(self):
        self.tag = "Empty"

class ExpFunctions:
    def __init__(self,  func, exp):
        self.tag = "Functions"
        self.func = func
        self.exp = exp

class ExpNumbers:
    def __init__(self,  value):
        self.tag = "Numbers"
        self.value = value

class ExpBrackets:
    def __init__(self, exp):
        self.tag = "Brackets"
        self.exp = exp
class ExpVariables:
    def __init__(self, name):
        self.tag = "Variables"
        self.name = name


def solve(exp, library):
    if exp.tag == "Binaries":
        a = solve(exp.exp_before, library)
        b = solve(exp.exp_after, library)
        if exp.operator == "+":
            return a + b
        elif exp.operator == "*":
            return a * b
        elif exp.operator == "-":
            return a - b
        elif exp.operator == "/":
            return a / b
        else:
            assert(False)
    elif exp.tag == "Unary":
        a = solve(exp.exp, library)
        return -1 * a
    elif exp.tag == "Functions":
        a = solve(exp.exp, library)
        if exp.func == "sqrt":
            return math.sqrt(a)
        elif exp.func == "sin":
            return math.sin(a)
        elif exp.func == "cos":
            return math.cos(a)
        else:
            assert(False)
    elif exp.tag == "Variables":
        return library[exp.name] 
    elif exp.tag == "Numbers":
        return exp.value
    else:
        assert(False)

def putBrackets(exp):
    if exp.tag == "Binaries":
        a = putBrackets(exp.exp_before)
        b = putBrackets(exp.exp_after)
        return "(" + a + exp.operator +  b + ")"
    elif exp.tag == "Functions":
        a = putBrackets(exp.exp)
        return "(" + exp.func + "(" + a + ")" + ")"
    elif exp.tag == "Variables":
        return exp.name
    elif exp.tag == "Numbers":
        return str(exp.value)
    else:
        assert(False)

exp = ExpBinaries(ExpNumbers(1), "+", ExpBinaries(ExpNumbers(2), "*", ExpNumbers(3)))
exp_test1 = ExpBinaries(ExpVariables("a"), "+", ExpBinaries(ExpVariables("b"), "*", ExpVariables("c")))
valores = {'a': 1, 'b': 2, 'c':3 }
exp_test = ExpBinaries(ExpNumbers(1), "+", ExpFunctions("sqrt", ExpBinaries(ExpNumbers(2), "*", ExpNumbers(2))))
print(f"Valor da expressao: {solve(exp_test1, valores)}")
print(f"Expressap com parenteses: {putBrackets(exp_test1)}")

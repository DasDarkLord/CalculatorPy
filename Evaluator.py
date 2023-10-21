import math


def evaluate(tree):
    if tree.type == "number":
        return tree.value
    elif tree.type == "add":
        return float(evaluate(tree.left)) + float(evaluate(tree.right))
    elif tree.type == "sub":
        return float(evaluate(tree.left)) - float(evaluate(tree.right))
    elif tree.type == "mul" or tree.type == "imul":
        return float(evaluate(tree.left)) * float(evaluate(tree.right))
    elif tree.type == "div":
        return float(evaluate(tree.left)) / float(evaluate(tree.right))
    elif tree.type == "pow":
        return math.pow(float(evaluate(tree.left)), float(evaluate(tree.right)))

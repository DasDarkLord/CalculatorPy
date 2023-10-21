from Lexer import *
from NodeParser import *
from Evaluator import evaluate


if __name__ == '__main__':
    while True:
        expr = input("Expression: ")
        tokens = lexString(expr)
        tree = parseTokens(tokens)

        print(expr)
        print(tokens)
        print(tree)
        print(evaluate(tree))

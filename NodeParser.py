from Token import *
from TreeNode import *


class NodeParser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parseNumber(self):
        token = self.tokens[self.index]
        self.index += 1
        return TreeNode("number", value=token.value)

    def parseExpression(self):
        leftNode = self.parseTerm()
        while self.index < len(self.tokens) and (
                self.tokens[self.index].type == ADDITION_TOKEN or self.tokens[self.index].type == SUBTRACTION_TOKEN):
            operator = self.tokens[self.index].type.id
            self.index += 1
            rightNode = self.parseTerm()
            leftNode = TreeNode(operator, leftNode, rightNode)
        return leftNode

    def parseTerm(self):
        leftNode = self.parseExponent()
        while self.index < len(self.tokens) and (self.tokens[self.index].type == MULTIPLICATION_TOKEN or self.tokens[self.index].type == DIVISION_TOKEN):
            operator = self.tokens[self.index].type.id
            self.index += 1
            rightNode = self.parseExponent()
            leftNode = TreeNode(operator, leftNode, rightNode)
        return leftNode

    def parseExponent(self):
        leftNode = self.parseFactor()
        while self.index < len(self.tokens) and self.tokens[self.index].type == EXPONENT_TOKEN:
            operator = self.tokens[self.index].type.id
            self.index += 1
            rightNode = self.parseFactor()
            leftNode = TreeNode(operator, leftNode, rightNode)
        return leftNode

    def parseFactor(self):
        if self.tokens[self.index].type == NUMBER_TOKEN:
            return self.parseNumber()
        elif self.tokens[self.index].type == OPAREN_TOKEN:
            self.index += 1
            expressionNode = self.parseExpression()
            if self.index < len(self.tokens) and self.tokens[self.index].type == CPAREN_TOKEN:
                self.index += 1
                return expressionNode


def parseTokens(tokens):
    parser = NodeParser(tokens)
    return parser.parseExpression()

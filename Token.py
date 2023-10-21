from dataclasses import dataclass


@dataclass
class TokenType:
    id: str
    word: str = None


NUMBER_TOKEN = TokenType("num")
STRING_TOKEN = TokenType("string")
IDENTIFIER_TOKEN = TokenType("identifier")
FUNCTION_CALL_TOKEN = TokenType("func_call")
ADDITION_TOKEN = TokenType("add", "+")
SUBTRACTION_TOKEN = TokenType("sub", "-")
MULTIPLICATION_TOKEN = TokenType("mul", "*")
IMPLICIT_MULTIPLICATION_TOKEN = TokenType("imul")
DIVISION_TOKEN = TokenType("div", "/")
EXPONENT_TOKEN = TokenType("pow", "^")
OPAREN_TOKEN = TokenType("oparen", "(")
CPAREN_TOKEN = TokenType("cparen", ")")

TOKEN_VALUES = [
    NUMBER_TOKEN,
    ADDITION_TOKEN, SUBTRACTION_TOKEN, MULTIPLICATION_TOKEN, IMPLICIT_MULTIPLICATION_TOKEN, DIVISION_TOKEN, EXPONENT_TOKEN
]


@dataclass
class Token:
    type: TokenType
    value: any


from Token import *


def lexString(src: str):
    tokens = []
    position = 0
    source = src.strip()

    while position < len(source):
        if source[position].isdigit():
            num = ""
            amountPoint = 0
            while position < len(source) and (source[position].isdigit() or (source[position] == "." and amountPoint == 0)):
                if source[position] == ".":
                    amountPoint += 1

                num = num + source[position]
                position += 1

            position -= 1

            tokens.append(Token(
                NUMBER_TOKEN,
                float(num)
            ))
        else:
            for tokenType in TOKEN_VALUES:
                if tokenType.word is not None and tokenType.word == source[position]:
                    tokens.append(Token(
                        tokenType,
                        str(tokenType.word)
                    ))

        position += 1

    return tokens

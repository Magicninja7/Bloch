import sys
import re
from enum import Enum

exit_code = 0


class TokenType(Enum):
    NONE = -2
    EOF = -1

    STRING = 0
    NUMBER = 1
    IDENTIFIER = 2

    LEFT_PAREN = 3
    RIGHT_PAREN = 4
    LEFT_BRACE = 5
    RIGHT_BRACE = 6
    COMMA = 7
    DOT = 8
    MINUS = 9
    PLUS = 10
    SEMICOLON = 11
    STAR = 12
    SLASH = 13
    EQUAL_EQUAL = 14
    EQUAL = 15

    BANG_EQUAL = 16
    BANG = 17
    LESS_EQUAL = 18
    LESS = 19
    GREATER_EQUAL = 20
    GREATER = 21

    AND = 22
    OR = 23
    IF = 24
    ELSE = 25
    FOR = 26
    WHILE = 27
    TRUE = 28
    FALSE = 29
    CLASS = 30
    SUPER = 31
    THIS = 32
    VAR = 33
    FUN = 34
    RETURN = 35
    PRINT = 36
    NIL = 37

    def __str__(self):
        return self.name





























def main():
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize" and command != "parse":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_tokens = file.read()







    if command == 'tokenize':
        reserved = {
            'and': 'AND',
            'class': 'CLASS',
            'else': 'ELSE',
            'false': 'FALSE',
            'for': 'FOR',
            'fun': 'FUN',
            'if': 'IF',
            'nil': 'NIL',
            'or': 'OR',
            'print': 'PRINT',
            'return': 'RETURN',
            'super': 'SUPER',
            'this': 'THIS',
            'true': 'TRUE',
            'var': 'VAR',
            'while': 'WHILE'
        }

        characters = {
            "(": "LEFT_PAREN",
            ")": "RIGHT_PAREN",
            "{": "LEFT_BRACE",
            "}": "RIGHT_BRACE",
            ".": "DOT",
            ",": "COMMA",
            "*": "STAR",
            ";": "SEMICOLON",
            "+": "PLUS",
            "-": "MINUS",
            "=": "EQUAL",
            "!": "BANG",
            "<": "LESS",
            ">": "GREATER",
            "/": "SLASH",
            "+": "PLUS",
            "-": "MINUS"
        }
        error_msg = []
        token = []
        error = False
        for line_number, string in enumerate(file_tokens.split("\n")):
            count = 0

            while count < len(string):
                p = string[count]
                if p in characters:
                    if p == '=' and count < len(file_tokens) -1 and string[count+1] == '=':
                        token.append(f"EQUAL_EQUAL == null")
                        count+=1
                    elif p == '!' and count < len(file_tokens) -1 and string[count+1] == '=':
                        token.append(f'BANG_EQUAL != null')
                        count+=1
                    elif p == '>' and count < len(file_tokens) -1 and string[count+1] == '=':
                        token.append(f'GREATER_EQUAL >= null')
                        count+=1
                    elif p == '<' and count < len(file_tokens) -1 and string[count+1] == '=':
                        token.append(f'LESS_EQUAL <= null')
                        count+=1
                    elif p == '/' and count < len(file_tokens) -1 and string[count+1] == '/':
                        break
                    else:
                        token.append(f"{characters[p]} {p} null")

                elif p.isdigit():
                    number = p
                    while count+1 < len(string):
                        count += 1
                        q = string[count]
                        if q == '.' and q in number:
                            break
                        elif q == '.' or q.isdigit():
                            number = f'{number}{q}'
                        else:
                            count -= 1
                            break

                    if '.' in number:
                        r, t = number.split('.')
                        t = t.lstrip('0')
                        if t == '':
                            t = '0'
                        token.append(f'NUMBER {number} {r}.{t}')
                    else:
                        token.append(f'NUMBER {number} {number}.0')              

                elif p in [" ", "\t"]:
                    pass

                elif p == '\n':
                    line_number += 1
                    pass

                elif p == '"':
                    temp = ''
                    for _ in range(len(string)-count):
                        count += 1
                        try:
                            if string[count] == '"':
                                token.append(f'STRING "{temp}" {temp}')
                                break
                        except IndexError:
                            error = True
                            error_msg.append(
                                f"[line {line_number+1}] Error: Unterminated string.")
                            continue

                        temp = f"{temp}{string[count]}"

                elif p.isalpha() or p == '_':
                    ident = p
                    while count+1 < len(string):
                        count += 1
                        d = string[count]
                        if d in characters or d == ' ':
                            count -= 1
                            break

                        ident = f'{ident}{string[count]}'
                    if ident in reserved:
                        token.append(f'{reserved[ident]} {ident} null')
                    else:
                        token.append(f'IDENTIFIER {ident} null')
                else:
                    error = True
                    error_msg.append(
                        f"[line {line_number+1}] Error: Unexpected character: {p}")
                count += 1



    elif command == 'parse':

        for line_number, string in enumerate(file_tokens.split("\n")):
            count = 0
            equation = []

            while count < len(string):
                w = string[count]
                if p.isalpha() or p == '_':
                    ident = p
                    while count+1 < len(string):
                        count += 1
                        d = string[count]
                        if d in characters or d == ' ':
                            count -= 1
                            break

                        ident = f'{ident}{string[count]}'
                    if ident in reserved:
                        token.append(ident)
                    else:
                        token.append(f'IDENTIFIER {ident} null')

                elif isinstance(w, int):

                        

                        
                else:                    
                    error = True
                    error_msg.append(
                        f"[line {line_number+1}] Error: Unexpected character: {p}")
                count += 1
                
                






        
                


    print('\n'.join(error_msg), file=sys.stderr)
    if token:
        print('\n'.join(token))

    print("EOF  null")
    if error:
        exit(65)
    exit(0)


if __name__ == "__main__":
    main()


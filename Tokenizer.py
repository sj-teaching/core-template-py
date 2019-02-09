class Token:
    PROGRAM = 1
    BEGIN = 2
    END = 3
    INT = 4
    IF = 5
    THEN = 6
    ELSE = 7
    WHILE = 8
    LOOP = 9
    READ = 10
    WRITE = 11
    AND = 12
    OR = 13
    SEMICOL = 14
    COMMA = 15
    ASSIGN = 16
    NOT = 17
    LBRACK = 18
    RBRACK = 19
    LPAREN = 20
    RPAREN = 21
    PLUS = 22
    MINUS = 23
    STAR = 24
    NEQ = 25
    EQ = 26
    GEQ = 27
    LEQ = 28
    GT = 29
    LT = 30
    NUM = 31
    ID = 32
    EOF = 33

    def __init__(self, name, line, code):
        self.name = name
        self.line = line
        self.code = code

class Tokenizer:
    # TODO Add any class/instance variables

    def __init__(self):
        # TODO Initialize the Tokenizer
        pass

    def tokenize(self, file_path):
        """Removes white space and tokenizes the file at the given file_path."""

        # TODO Declare the appropriate File handlers and open them.
        # TODO Make sure you handle any exceptions this may lead to.

        # TODO Implement the tokenizer per the algorithm given below

        # 1. Get a character from the input stream
        # 2. While it's a valid character (What does this mean?)
        # 2.1. Track the line numbers and ignore white-spaces
        # 2.2. If it's a lowercase, check if it results in a reserved word
        # 2.3. If it's uppercase, check if it's a valid ID
        # 2.4. If it's a digit, check if it's a valid NUMBER
        # 2.5. Otherwise, check if it's one of the valid special characters
        #       Note: be extra careful about tokens like '==' and '='.
        #             You should always extract a '==' first if it exists.
        # 3. Once the entire input stream is tokenized, add the special
        #    End-of-stream (33) token to the list of Tokens

        pass

    def current_token(self):
        """Returns the current token as a `Token` object."""
        return nil

    def next_token(self):
        """Advances to the next token in the token stream."""
        pass

    def has_next(self):
        """Reports whether the token stream has another token on it."""
        return False

    # Note: Feel free to add any other methods you may need.


import sys
def main(argv):
    if len(argv) != 1:
        print 'Invalid number of arguments\nUsage: python Tokenizer.py <core input file>\n'
        sys.exit(1)
 
    t = Tokenizer()
    t.tokenize(argv[0])
    while (t.has_next()):
        token = t.current_token()
        print token.code
        t.next_token()


if __name__ == '__main__':
    main(sys.argv[1:])

from smolcalc.tokens import TokenType
from smolcalc.nodes import *

class Parser:
    def __init__(self,tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expr()

        if self.current_token != None:
            self.raise_error()
        return result

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if  self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.exponent()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if  self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.exponent())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.exponent())

        return result

    def exponent(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type == TokenType.EXPONENT:
                self.advance()
                result = ExponentNode(result, self.factor())


        return result




    def factor(self):
        token = self.current_token

        if token is None: # maybe that could be prettier in another version
            self.raise_error()

        if token.type == TokenType.SQUAREROOT:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return SquarerootNode(result)

        if token.type == TokenType.NLOG:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return NLOG_Node(result)

        if token.type == TokenType.LOG_10:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return LOG_10_Node(result)

        if token.type == TokenType.FACTORIAL:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return FactorialNode(result)




        if token.type == TokenType.LPARPEN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return result

        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        self.raise_error()

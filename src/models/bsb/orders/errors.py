__author__ = 'nabee1'

class BSBOrderException(Exception):
    def __init__(self, message):
        self.message = message

class BRBOrderNotFoundException(BSBOrderException):
    pass

from ex_mock.outputter import Outputter
from ex_mock.creator import Creator


class Greeter:
    """ 挨拶します """

    def __init__(self, greet, outputter):
        """
        ARGS
            greet 挨拶
        """
        self.__greet = greet
        self.__outputter = outputter

    def greet(self, name):
        """
        ARGS
            name 名前
        """
        creator = Creator()
        message = creator.create(self.__greet, name)
        self.__outputter.output(message)

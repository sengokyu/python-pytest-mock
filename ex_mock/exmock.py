from ex_mock.outputter import Outputter
from ex_mock.greeter import Greeter


class ExMock:
    def __init__(self):
        self.__greeter = Greeter('Hello', Outputter())

    def exec(self, name):
        self.__greeter.greet(name)

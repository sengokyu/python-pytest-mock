from ex_mock.outputter import Outputter
from ex_mock.creator import Creator
from ex_mock.greeter import Greeter


class TestGreeter:
    def test_greet(self, mocker):
        """ Creator.createをモック化、戻り値を変更 """
        # Given
        result = 'result'
        mocker.patch.object(Creator, 'create', return_value=result)
        outputter = mocker.Mock(Outputter)
        instance = Greeter('Hi', outputter)

        # When
        instance.greet('Jane')

        # Then
        outputter.output.assert_called_once_with(result)
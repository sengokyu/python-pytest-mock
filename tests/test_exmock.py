from ex_mock.exmock import ExMock
from ex_mock.greeter import Greeter


class TestExmock:
    def test_create_instance(self):
        # When
        actual = ExMock()

        # Then
        assert actual is not None
        assert isinstance(actual, ExMock)

    def test_exec(self, mocker):
        """ Greeter.greet をモック化。呼び出されるかテスト """
        # Givin
        greet = mocker.patch.object(Greeter, 'greet')
        instance = ExMock()
        name = "world"

        # When
        instance.exec(name)

        # Then
        greet.assert_called_once_with(name)

    def test_init(self, mocker):
        """ Greeterコンストラクタをモック化 """
        # Given
        outputter = mocker.patch('ex_mock.exmock.Outputter', autospec=True)
        greeter = mocker.patch('ex_mock.exmock.Greeter', autosec=True)

        # When
        instance = ExMock()

        # Then
        outputter.assert_called_once()
        greeter.assert_called_once()

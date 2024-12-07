from .calculator_4 import Calculator4
from typing import Dict
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [10, 10, 10, 10, 10]})

    calculator = Calculator4() 
    response = calculator.calculate(mock_request)

    assert response == {
        "data": {
            "Calculator": 4,
            "result": 10
        }
    }


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": []})
    calculator_4 = Calculator4()

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"

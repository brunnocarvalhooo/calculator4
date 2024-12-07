from typing import Dict, List
from flask import request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        calc_result = self.process(input_data)

        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> List:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        
        return input_data

    def process(self, numbers: List[float]) -> float:
        total = sum(numbers)
        average = total / len(numbers)

        return average

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(calc_result, 2)
            }
        }

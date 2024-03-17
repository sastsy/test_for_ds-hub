import yaml
import json
from typing import List

from convolution_func import convolution


TESTS_FILENAME = 'tests.yaml'

def load_tests(filename: str) -> List:
    '''Функция парсит тесты из файла'''
    with open(filename, 'r') as file:
        tests = yaml.safe_load(file)

    return tests['tests']


def run_tests(tests: List) -> None:
    '''
    Функция принимает на вход список тестов
    и проверяет, проходит ли их convolution()
    '''
    for test in tests:
        data = test['data']
        func = eval(test['function'])
        expected_output = test['expected_output']

        answer = convolution(data, func)

        assert json.dumps(expected_output) == json.dumps(answer),\
            f"{test['name']}\nОжидалось: {expected_output}\nОтвет: {answer}"


if __name__ == '__main__':
    tests = load_tests(TESTS_FILENAME)
    try:
        run_tests(tests)
    except AssertionError as e:
        print(f"Ошибка на тесте {e}")
    else:
        print("Все тесты пройдены успешно.")

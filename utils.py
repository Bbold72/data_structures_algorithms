from typing import Tuple

def run_tests(f, inputs: Tuple, answers: Tuple):
    for input, ans in zip(inputs, answers):
        result = f(input)
        assert result == ans, f'Error. Expected {ans} for input {input}. Got {result}'
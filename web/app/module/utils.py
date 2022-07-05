from flask import request

def get_input(input_name : str) -> str:
    input_value = request.form[input_name]

    if input_value is None or len(input_value) == 0:
        raise AssertionError(f"{input_name}")
    
    return input_value
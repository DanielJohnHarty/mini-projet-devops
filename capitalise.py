def capital_case(input_string):
    # Ensures first letter of string
    # is capitalised
    if type(input_string) is not str:
      raise TypeError('Input is not a string!')

    lower_case_input = input_string.lower()
    capitalised_string = \
        lower_case_input[0].upper() + lower_case_input[1:]
    return capitalised_string

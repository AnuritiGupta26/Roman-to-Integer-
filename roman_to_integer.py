def roman_to_int(numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    special_cases = {
        "CM": 900, "CD": 400, 
        "XC": 90, "XL": 40, 
        "IX": 9, "IV": 4
    }
    final_answer = 0
    for special in special_cases:
        if special in numeral:
            final_answer += special_cases[special]
            numeral = numeral.replace(special, "")  # Remove the special case from numeral 
    for char in numeral:
        if char in roman_values:
            final_answer += roman_values[char]  
    return final_answer
numeral_input = input("Enter the Roman numerals you want to convert: ").upper()
result = roman_to_int(numeral_input)
print(f"The Roman numerals you entered translate to: {result}!")

import random

# Original code snippet
original_snippet_concatenation = '"....." + a * b + "....."'
original_snippet_interpolation = '"....." + a * b + "....."'

# Error types
error_types_concatenation = [
        lambda s: s.replace('*', '/'),  
        lambda s: s.replace('+', '-'),  
        lambda s: s.replace('+ "', ''),
        lambda s: s.replace('" +', ''),  
        lambda s: s.replace('....."', '"'),  
        lambda s: s + ' + c',  
        lambda s: s.replace('a * b', 'a * '),  
        lambda s: s.replace('a * b', '* b'),
    ]

# List to hold permutations
# permutations = []

# Function to introduce an error into a code snippet
def introduce_error(snippet, error_types):
    
    # Select a random error to introduce
    error_func = random.choice(error_types)
    return error_func(snippet)

def error_concatenation():
    erroneous_snippet = introduce_error(original_snippet_concatenation, error_types_concatenation)
    return erroneous_snippet

def error_interpolation():
    erroneous_snippet = introduce_error(original_snippet_concatenation, error_types_concatenation)
    return error_interpolation

# Generate 5 permutations with errors
# for _ in range(5):
#     erroneous_snippet = introduce_error(original_snippet)
#     permutations.append(erroneous_snippet)

# # Display the generated permutations
# for i, permutation in enumerate(permutations, start=1):
#     print(f"Permutation {i}: {permutation}")
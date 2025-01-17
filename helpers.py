import json

# Load and parse the JSON data file
def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
    
def calculate_total_inflation(inflation_rate, years):

    return (1 + inflation_rate) ** years
    
def calculate_total_discount(discount_rate, years):

    return (1 + discount_rate) ** years


def calculate_total_hazard_probability(hazard_probability, years):

    # This is the probability of a hazard happening, over the number of years given as input.
    return 1 - (1 - hazard_probability) ** years
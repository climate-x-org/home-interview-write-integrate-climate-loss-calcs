import json
import math

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

# Calculate total projected loss with additional complexity and errors
def calculate_projected_losses(building_data, years):
    discount_rate = 0.05  # Assuming a 5% discount rate

    # Calculate the discount rate, compounded over the years
    total_discount = calculate_total_discount(discount_rate, years)

    total_loss = 0
    for building in building_data:
        floor_area = building['floor_area']
        construction_cost = building['construction_cost']
        yearly_hazard_probability = building['hazard_probability']
        inflation_rate = building['inflation_rate']

        # Calculate total inflation, over years
        total_inflation = calculate_total_inflation(inflation_rate, years)

        # Calculate future cost
        future_cost = construction_cost * total_inflation

        # Calculate total hazard probability, over years
        total_hazard_probability = calculate_total_hazard_probability(yearly_hazard_probability, years)

        # Calculate risk-adjusted loss
        risk_adjusted_loss = future_cost * (total_hazard_probability)

        # Calculate present value of the risk-adjusted loss
        present_value_loss = risk_adjusted_loss / total_discount

        # Calculate maintenance and total maintenance cost
        maintenance_cost = floor_area * 50  # assuming a flat rate per square meter

        # Calculate the total maintenance cost, over the years, adjusted by inflation
        total_maintenance_cost = maintenance_cost * years * total_inflation

        # Discounting total maintenance cost, by today's value
        discounted_tot_maintenance_cost = total_maintenance_cost / total_discount

        # Total loss calculation
        total_loss += present_value_loss + total_maintenance_cost

    return total_loss

def calculate_complex_loss(
    construction_cost,
    inflation_rate,
    floor_area,
    hazard_probability,
    standard_discount_rate,
    years
):
    # Calculate total inflation, over years
    total_inflation = calculate_total_inflation(inflation_rate, years)
    inflated_construction_cost = construction_cost * (math.e ** (total_inflation * floor_area / 1000))
    
    total_hazard_probability = calculate_total_hazard_probability(hazard_probability, years)
    
    future_loss_estimate = inflated_construction_cost * total_hazard_probability

    # Calculate the discount rate, compounded over the years
    total_discount = calculate_total_discount(standard_discount_rate, years)

    return future_loss_estimate / total_discount


# Main execution function
def main():
    data = load_data('data.json')
    total_projected_loss = calculate_projected_losses(data, 10)
    print(f"Total Projected Loss: ${total_projected_loss:.2f}")

if __name__ == '__main__':
    main()
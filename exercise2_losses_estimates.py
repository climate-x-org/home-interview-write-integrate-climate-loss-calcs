import math

from helpers import load_data, calculate_total_inflation, calculate_total_discount, calculate_total_hazard_probability
from constants import discount_rate


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


def calculate_all_losses(
    building_data, years
):
    total_loss = 0
    for building in building_data:
        building_loss_estimate = calculate_complex_loss(
            building['construction_cost'],
            building['inflation_rate'],
            building['floor_area'],
            building['hazard_probability'],
            discount_rate,
            years,
        )
        print(f"Estimated losses for building {building['buildingId']}: ${building_loss_estimate:.2f}")

        total_loss += building_loss_estimate
    return total_loss


# Main execution function
def main():
    json_file = 'data.json'
    print('Exercise 2:')
    print(f"Loading data from {json_file}")
    data = load_data(json_file)
    total_loss = calculate_all_losses(data, 20)

    print(f"Estimated total losses for all buildings: ${total_loss:.2f}")

if __name__ == '__main__':
    main()
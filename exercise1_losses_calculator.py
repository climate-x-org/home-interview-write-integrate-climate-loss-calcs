import math

from helpers import load_data, calculate_total_inflation, calculate_total_discount, calculate_total_hazard_probability

from constants import discount_rate

# Calculate total projected loss with additional complexity and errors
def calculate_projected_losses(building_data, years):
    
    # Considerations about estimating the loss of money caused by a hazard event VS
    # estimating the loss of money due to the maintenance of a building:
    #
    # We assume that a "hazard event" would always cause the building to be completely destroyed,
    # so all of its value would be lost. This has to be adjusted by the probability of it happening
    # though, because it may or may not happen.
    #
    # Conversely, maintenance costs can be considered as a "loss" that will happen for sure
    # Because we know that every year, each building will require some maintenance, for which 
    # we know the cost.
    #
    # This is of course an over semplification on many fronts. The most important one 
    # is the fact that is a building collapses, its maintenance costs will become 0 for all 
    # of the following years.

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
        discounted_total_maintenance_cost = total_maintenance_cost / total_discount

        # Total loss calculation
        total_loss += present_value_loss + discounted_total_maintenance_cost

    return total_loss

# Main execution function
def main():
    json_file = 'data.json'
    print('Exercise 1:')
    print(f"Loading data from {json_file}")
    data = load_data(json_file)
    total_projected_loss = calculate_projected_losses(data, 10)
    print(f"Total Projected Loss: ${total_projected_loss:.2f}")

if __name__ == '__main__':
    main()
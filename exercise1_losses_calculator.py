import json
from typing import Optional


# Load and parse the JSON data file
def load_data(filepath: str) -> list[dict]:
    with open(filepath, "r") as file:
        return json.load(file)


def potential_financial_losses_estimate(
    years: int,
    floor_area: float,
    construction_cost: float,
    hazard_probability: float,
    inflation_rate: float,
    discount_rate: float = 0.05,
) -> float:
    """
    A more complex loss calculation formula.

    Args:
        years: number of years from now for which loss should be calculated
        floor_area: floor area in sq meters of the property
        construction_cost: construction cost per square meter, in USD ($)
        hazard_probability: likelihood of experiencing a climate-related hazard
        inflation_rate: annual inflation rate applicable to the construction cost
        discount_rate: standard annual discount rate

    Returns:
        financial losses estimate
    """

    raise NotImplementedError


def simple_loss_estimate(
    years: int,
    floor_area: float,
    construction_cost: float,
    hazard_probability: float,
    inflation_rate: float,
    discount_rate: float = 0.05,
) -> float:
    """
    A simple loss calculation formula.

    Args:
        years: number of years from now for which loss should be calculated
        floor_area: floor area in sq meters of the property
        construction_cost: construction cost per square meter, in USD ($)
        hazard_probability: likelihood of experiencing a climate-related hazard
        inflation_rate: annual inflation rate applicable to the construction cost
        discount_rate: standard annual discount rate
    """
    # Calculate future cost, compounding annually
    future_cost = construction_cost * ((1 + inflation_rate) ** years)

    # Calculate risk-adjusted loss
    risk_adjusted_loss = future_cost * hazard_probability

    # Calculate present value of the risk-adjusted loss, annualized
    present_value_loss = risk_adjusted_loss / (1 + discount_rate) ** years

    # Calculate maintenance and total maintenance cost
    maintenance_cost = floor_area * 50  # assuming a flat rate per square meter
    discounted_maintainence_costs = [
        maintenance_cost
        / (1 + discount_rate) ** year  # costs vary per year due to discounting
        for year in range(years)
    ]
    total_maintenance_cost = sum(discounted_maintainence_costs)

    # Total loss calculation
    total_loss = present_value_loss + total_maintenance_cost

    return total_loss


def calculate_projected_losses(
    building_data: list[dict], years: Optional[int] = None
) -> float:
    """
    Calculate total projected loss with additional complexity and errors

    Args:
        building_data: list of formatted building data dictionaries with floor_area,
            construction_cost, hazard_probability, and inflation_rate
        years (optional): how many years into the future losses should be projected
            (if present, must be positive)

    Returns:
        total loss value over the portfolio for the specified number of years
    """
    if years is None:
        years = 1
    elif years <= 0:
        raise ValueError("Years value needs to be strictly positive.")

    total_loss = 0.0
    for building in building_data:
        floor_area = building["floor_area"]
        construction_cost = building["construction_cost"]
        hazard_probability = building["hazard_probability"]
        inflation_rate = building["inflation_rate"]
        total_loss += simple_loss_estimate(
            years=years,
            floor_area=floor_area,
            construction_cost=construction_cost,
            hazard_probability=hazard_probability,
            inflation_rate=inflation_rate,
        )

    return total_loss


# Main execution function
def main():
    data = load_data("data.json")
    years = 1
    total_projected_loss = calculate_projected_losses(data, years)
    print(
        f"Total Projected Loss Over {years} Year{'s' if years > 1 else ''}: ${total_projected_loss:.2f}"
    )


if __name__ == "__main__":
    main()

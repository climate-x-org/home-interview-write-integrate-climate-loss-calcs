import json
from math import exp
from typing import Optional


# Load and parse the JSON data file
def load_data(filepath: str) -> list[dict]:
    with open(filepath, "r") as file:
        return json.load(file)


def simple_loss_estimate(
    years: int,
    floor_area: float,
    construction_cost: float,
    hazard_probability: float,
    inflation_rate: float,
    discount_rate: float = 0.05,
) -> float:
    """
    Exercise 1: A simple loss calculation formula.

    Note that we _exclude_ the cost of maintainence, as that is an expected running
    cost and not a financial loss.  If desired, maintainence can be computed as
        ```
        maintenance_cost = floor_area * 50  # assuming a flat rate per square meter
        discounted_maintainence_costs = [
            maintenance_cost
            / (1 + discount_rate) ** year  # costs vary per year due to discounting
            for year in range(years)
        ]
        total_maintenance_cost = sum(discounted_maintainence_costs)
        ```

    Args:
        years: number of years from now for which loss should be calculated
        floor_area: floor area in sq meters of the property
        construction_cost: construction cost per square meter, in USD ($)
        hazard_probability: likelihood of experiencing a climate-related hazard
        inflation_rate: annual inflation rate applicable to the construction cost
        discount_rate: standard annual discount rate

    Returns:
        present value loss
    """
    # Calculate future cost, compounding annually, for the entire building
    future_cost = construction_cost * floor_area * ((1 + inflation_rate) ** years)

    # Calculate risk-adjusted loss
    risk_adjusted_loss = future_cost * hazard_probability

    # Calculate present value of the risk-adjusted loss, annualized
    present_value_loss = risk_adjusted_loss / (1 + discount_rate) ** years

    return present_value_loss


def potential_financial_losses_estimate(
    years: int,
    floor_area: float,
    construction_cost: float,
    hazard_probability: float,
    inflation_rate: float,
    discount_rate: float = 0.05,
) -> float:
    """
    Exercise 2: A more complex loss calculation formula.

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
    raw_loss_estimate = (
        construction_cost * floor_area * exp(inflation_rate * floor_area / 1000)
    )
    risk_adjusted_loss = raw_loss_estimate * hazard_probability
    discount_factor = 1 / (1 + discount_rate) ** years
    total_loss_estimate = risk_adjusted_loss * discount_factor
    return total_loss_estimate


def calculate_projected_losses(
    building_data: list[dict], years: Optional[int] = None, method: str = "simple"
) -> dict:
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

    if method.lower() == "simple":
        estimate_function = simple_loss_estimate
    elif method.lower() == "complex":
        estimate_function = potential_financial_losses_estimate
    else:
        raise ValueError(
            f"Expected one of 'simple' or 'complex' for method; recieved '{method}'."
        )

    losses = {}
    for building in building_data:
        id = building["buildingId"]
        floor_area = building["floor_area"]
        construction_cost = building["construction_cost"]
        hazard_probability = building["hazard_probability"]
        inflation_rate = building["inflation_rate"]
        losses[id] = estimate_function(
            years=years,
            floor_area=floor_area,
            construction_cost=construction_cost,
            hazard_probability=hazard_probability,
            inflation_rate=inflation_rate,
        )

    return losses


def _format_and_print_losses(losses: dict, method: str = "") -> None:
    if len(method) > 0:
        print(f"=== {method.upper()} METHOD ===")
    print("ID\t| Loss USD")
    print("---\t| ---")
    for id, loss in losses.items():
        print(f"{id}\t| ${loss:.2f}")
    print("---\t| ---")

    total_projected_loss = sum(losses.values())
    print(f"Total\t| ${total_projected_loss:.2f}\n")


# Main execution function
def main():
    data = load_data("data.json")
    years = 1
    print(f"Projected Losses Over {years} Year{'s' if years > 1 else ''}")

    total_projected_losses_simple = calculate_projected_losses(
        data, years, method="simple"
    )
    _format_and_print_losses(losses=total_projected_losses_simple, method="simple")

    total_projected_losses_complex = calculate_projected_losses(
        data, years, method="complex"
    )
    _format_and_print_losses(losses=total_projected_losses_complex, method="complex")


if __name__ == "__main__":
    main()

import json
import random
from typing import NamedTuple


class ValueRange(NamedTuple):
    min_value: int
    max_value: int
    scale_factor: int = 1

    def get_value(self) -> float | int:
        value = random.randint(self.min_value, self.max_value) / self.scale_factor
        if self.scale_factor == 1:
            return int(value)
        return value


FloorAreaRange = ValueRange(min_value=1500, max_value=2500)
ConstructionCostRange = ValueRange(min_value=1000, max_value=1600)
HazardProbabilityRange = ValueRange(min_value=1, max_value=16, scale_factor=100)
InflationRateRange = ValueRange(min_value=1, max_value=6, scale_factor=100)


def generate_dataset(n: int):
    """
    Generate synthetic data for a building dataset consisting of n buildings.

    Args:
        n: number of synthetic buildings to generate
    """
    buildings = []
    for i in range(n):
        building = {
            "buildingId": i,
            "floor_area": FloorAreaRange.get_value(),
            "construction_cost": ConstructionCostRange.get_value(),
            "hazard_probability": HazardProbabilityRange.get_value(),
            "inflation_rate": InflationRateRange.get_value(),
        }
        buildings.append(building)
    return buildings


def main():
    n = 100
    output_file = f"data/bigger_data_{n}.json"
    print(f"Writing {n} buildings to file '{output_file}'...")
    buildings = generate_dataset(n)
    with open(output_file, "w") as file:
        json.dump(buildings, file)
    print("Done.")


if __name__ == "__main__":
    main()

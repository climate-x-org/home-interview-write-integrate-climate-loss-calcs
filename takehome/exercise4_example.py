import time
from typing import NamedTuple
import numpy as np
from matplotlib import pyplot as plt

from generate_data import generate_dataset

benchmark_ns = [5, 10, 100, 1_000, 10_000, 1_000_000]


class BuildingData(NamedTuple):
    ids: list[int]
    floor_area: np.ndarray
    construction_cost: np.ndarray
    hazard_probability: np.ndarray
    inflation_rate: np.ndarray


def vectorized_financial_losses_estimate(
    years: int,
    floor_area: np.ndarray,
    construction_cost: np.ndarray,
    hazard_probability: np.ndarray,
    inflation_rate: np.ndarray,
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
        construction_cost * floor_area * np.exp(inflation_rate * floor_area / 1000)
    )
    risk_adjusted_loss = raw_loss_estimate * hazard_probability
    discount_factor = 1 / (1 + discount_rate) ** years
    total_loss_estimate = risk_adjusted_loss * discount_factor
    return total_loss_estimate


def data_to_arrays(data: list[dict]) -> BuildingData:
    """
    Convert building data from list of dictionary to structured numpy arrays.
    """
    ids = []
    floor_area = []
    construction_cost = []
    hazard_probability = []
    inflation_rate = []
    for building in data:
        ids.append(building["buildingId"])
        floor_area.append(building["floor_area"])
        construction_cost.append(building["construction_cost"])
        hazard_probability.append(building["hazard_probability"])
        inflation_rate.append(building["inflation_rate"])
    return BuildingData(
        ids=ids,
        floor_area=np.array(floor_area),
        construction_cost=np.array(construction_cost),
        hazard_probability=np.array(hazard_probability),
        inflation_rate=np.array(inflation_rate),
    )


def benchmark_losses(n: int) -> float:
    """
    Benchmark how quickly the complex loss calculation runs for n buildings.

    Args:
        n: number of simulated buildings over which the algorithm should be run

    Returns:
        total runtime
    """

    data = generate_dataset(n=n)
    building_data = data_to_arrays(data)
    start_time = time.time()
    losses = vectorized_financial_losses_estimate(
        years=1,
        floor_area=building_data.floor_area,
        construction_cost=building_data.construction_cost,
        hazard_probability=building_data.hazard_probability,
        inflation_rate=building_data.inflation_rate,
    )
    total_time = time.time() - start_time
    print(f"{n}\t|{total_time}")
    return total_time


def main():
    losses_time = []
    print("n\t|time(s)\n---\t|---")
    for n in benchmark_ns:
        losses_time.append(benchmark_losses(n))

    # create figure
    plt.subplots(1, 1)
    plt.loglog(benchmark_ns, losses_time, ".-")
    plt.title("Linear Scaling of Implementation")
    plt.xlabel("n buildings")
    plt.ylabel("runtime (s)")
    plt.savefig("takehome/vectorized_benchmark.png")


if __name__ == "__main__":
    main()

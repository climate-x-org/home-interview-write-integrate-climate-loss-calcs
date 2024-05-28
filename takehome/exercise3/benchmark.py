import time

from takehome.exercise1and2.exercise1_losses_calculator import (
    calculate_projected_losses,
)
from takehome.exercise3.generate_data import generate_dataset

benchmark_ns = [5, 10, 100, 1000, 10000]


def benchmark_losses(n: int) -> float:
    """
    Benchmark how quickly the complex loss calculation runs for n buildings.

    Args:
        n: number of simulated buildings over which the algorithm should be run

    Returns:
        total runtime
    """

    data = generate_dataset(n=n)
    start_time = time.time()
    losses = calculate_projected_losses(data, years=1, method="complex")
    total_time = time.time() - start_time
    print(
        f"Computed losses for {n} buildings in {total_time}s, rate of {total_time/n:0.3f} s/building"
    )
    return total_time


def main():
    for n in benchmark_ns:
        benchmark_losses(n)


if __name__ == "__main__":
    main()

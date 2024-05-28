import time

from exercise1and2_losses_calculator import calculate_projected_losses
from generate_data import generate_dataset
from matplotlib import pyplot as plt

benchmark_ns = [5, 10, 100, 1_000, 10_000, 1_000_000]


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
    plt.savefig("takehome/benchmark.png")


if __name__ == "__main__":
    main()

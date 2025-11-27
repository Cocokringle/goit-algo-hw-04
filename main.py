import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort


algorithms = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
    "Tim sort": sorted,
}

sizes = [100, 500, 1000, 2000, 5000, 10000]

def compare_sorting_algorithms():
    for name, algorithm in algorithms.items():
        print(f"\n{name} Performance:")
        print(f"{'N (quantity)':<15} | {'Time (sec)':<15} | {'Time increment'}")
        print("-" * 50)

        prev_time = None

        for size in sizes:
            test_data = [random.randint(0, 10000) for _ in range(size)]
            repeats = 6
            timer = timeit.Timer(lambda: algorithm(test_data.copy()))
            total_time = timer.timeit(number=repeats)
            avg_time = total_time / repeats

            growth = f"{avg_time / prev_time:.2f}x" if prev_time else "-"

            print(f"{size:<15} | {avg_time:.6f}        | {growth}")

            prev_time = avg_time

if __name__ == "__main__":
    compare_sorting_algorithms()
from random import randrange
from datetime import datetime

# Algos
from mergesort import merge_sort
from quicksort import quick_sort
from bogosort import bogo_sort
from bubblesort import bubble_sort

if __name__ == "__main__":
    sorting_algos = {
        "Merge Sort": {
            'algo': merge_sort,
            'time': 0
        },
        "Quick Sort": {
            'algo': quick_sort,
            'time': 0
        },
        "Bubble Sort": {
            'algo': bubble_sort,
            'time': 0
        }
    }

    # Create a list of random elements to sort
    items_to_sort = [randrange(1,10_000) for _ in range(1000)]

    for name, info in sorting_algos.items():
        then = datetime.now()
        info['algo'](items_to_sort)
        now = datetime.now()
        diff_ms = now.microsecond - then.microsecond
        info['time'] = diff_ms
    
    print("\n".join(f"Algorithm: {name}\tTime (ms): {info['time'] // 1000}" for name, info in sorting_algos.items()))

        



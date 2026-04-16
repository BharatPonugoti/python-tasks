# Smart Data Processing Pipeline
import numpy as np
import pandas as pd
import time

# Decorator to measure time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper

# Generator to read file
def read_numbers(file):
    with open(file, "r") as f:
        for line in f:
            try:
                yield float(line.strip())
            except ValueError:
                print("Invalid data skipped")

@timer
def process_data(file):
    data = list(read_numbers(file))

    arr = np.array(data)

    mean = np.mean(arr)
    std = np.std(arr)

    df = pd.DataFrame({
        "Mean": [mean],
        "Std Dev": [std]
    })

    print(df)

process_data("numbers.txt")
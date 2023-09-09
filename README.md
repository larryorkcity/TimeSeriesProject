# TimeSeriesProject
Preprocessing API for Time Series Data (Stream)



# Data Gap Correction with Linked Lists

## Overview

This code utilizes a linked list to identify and correct gaps between data points. By doing so, it significantly improves the efficiency of data processing, offering a more effective alternative to array-based approaches.

## Code Components

- `repair_data_gaps(data)`: This method checks for gaps between data points and, if necessary, performs corrections. It examines the time gap between the current node and the next node, and if it exceeds 1, it proceeds to restore the data.

- `main()`: This function conducts database operations, creates a linked list for data insertion, and executes the data gap correction process.

- `@measure_execution_time`: A decorator to measure the execution time of the code.

## Usage

1. `repair_data_gaps(data)`: Checks for and corrects data gaps within the linked list, starting from the current node to the next.

2. `main()`: Executes database operations, inserts data into the linked list, and performs data gap correction.

## Optimization and Benefits

- By utilizing a linked list, the code maintains a time complexity of O(n) for identifying and correcting data gaps.
- This results in a more efficient data processing approach, ultimately enhancing overall performance.









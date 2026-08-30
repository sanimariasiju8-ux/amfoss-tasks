# Task 09 — Matrix Multiplication Showdown

## Overview

This project is a terminal-based matrix multiplication application that implements and compares three different matrix multiplication algorithms:

1. Naive Matrix Multiplication
2. Divide and Conquer Matrix Multiplication
3. Strassen's Matrix Multiplication

The program takes two matrices as input from the user, calculates their product using all three approaches, measures the execution time of each algorithm, and verifies that all three methods produce the same result.

---

## Features

- Accepts matrix dimensions and elements from the user.
- Validates whether the two matrices can be multiplied.
- Implements three matrix multiplication algorithms.
- Displays the resulting matrix.
- Measures the execution time of each algorithm.
- Compares the outputs of all three methods.
- Verifies that all algorithms produce the same result.
- Runs completely through the terminal.
- Supports rectangular matrices with compatible dimensions.
- Automatically pads matrices to a square power-of-two size for Divide and Conquer and Strassen algorithms.
- Removes padding after multiplication to obtain the correct original dimensions.

---

## Algorithms Used

### 1. Naive Matrix Multiplication

The Naive approach is the standard method of matrix multiplication. It uses three nested loops to calculate each element of the resulting matrix.
For every element of the result matrix, a row from the first matrix is multiplied with a column from the second matrix and the products are added together.
Time Complexity : O(n³)
Space Complexity : O(n²)

### 2. Divide and Conquer Matrix Multiplication
The Divide and Conquer approach divides each matrix into four smaller submatrices. These smaller matrices are recursively multiplied and then combined to obtain the final result.
For two matrices divided into four blocks, the standard approach performs eight recursive matrix multiplications.
Time Complexity : O(n³)
Space Complexity : O(n²)

### 3. Strassen's Matrix Multiplication
Strassen's algorithm also divides the matrices into smaller submatrices, but it reduces the number of recursive matrix multiplications from eight to seven.
It uses additional matrix additions and subtractions to achieve this reduction.
The recurrence relation is: T(n) = 7T(n/2) + O(n²)
This gives a time complexity of: O(n^log₂7) ≈ O(n^2.807)
Space Complexity: O(n²)

## Benchmarking Approach
The execution time of each algorithm is measured independently.
The program records the time immediately before an algorithm starts and immediately after it finishes. The difference between these timestamps is used as the execution time.
The three algorithms are run on the same input matrices so that their execution times can be compared fairly.
The program displays the execution time for:
Naive
Divide and Conquer
Strassen
The measured execution time may vary depending on matrix size, system performance, and other processes running on the computer.
For small matrices, the difference between algorithms may be very small because function calls, recursion, and other overhead can affect the measurements.
The program uses Python's `time.perf_counter()` to measure the execution time of each algorithm. Each algorithm is executed separately using the same input matrices for a fair comparison.

## Output Verification
Correctness is verified by comparing the result produced by each algorithm.
The program checks:
Naive == Divide and Conquer
Naive == Strassen
If both comparisons are true, all three algorithms have produced the same result.
This helps ensure that the optimized algorithms are producing the same mathematical result as the standard Naive implementation.

## Challenges Faced
Some of the challenges encountered while implementing the project were:
Understanding the mathematical process behind matrix multiplication.
Converting the mathematical algorithms into working Python functions.
Handling matrix dimensions correctly.
Implementing recursive Divide and Conquer multiplication.
Understanding the seven multiplication steps used in Strassen's algorithm.
Handling matrix splitting, addition, subtraction, and combining results.
Measuring execution time accurately.
Verifying that all three algorithms produce identical results.
Understanding why Strassen's algorithm can have better theoretical time complexity than the other two approaches.
Handling matrices that are not square or whose dimensions are not powers of two.
Implementing zero-padding for the recursive algorithms and removing the padding from the final result.

## Concepts Learned
Through this task, I learned:
Matrix representation using Python lists.
Matrix multiplication.
Nested loops and indexing.
Functions and modular programming.
Recursion.
Divide and Conquer algorithm design.
Strassen's matrix multiplication technique.
Time complexity and Big-O notation.
Space complexity.
Benchmarking and performance measurement.
Comparing algorithm performance.
Result validation and correctness checking.
Handling user input and validating matrix dimensions.
The importance of testing algorithms with the same input.

## Resources Used
The implementation and understanding of the algorithms were developed using:
Python documentation for language features and standard library functions.
Algorithm and data-structure learning resources for understanding matrix multiplication.
References on Divide and Conquer algorithms.
References on Strassen's Matrix Multiplication.
VS Code for development and testing.

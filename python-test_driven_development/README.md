# Python - Test-Driven Development (TDD)

This repository contains tasks for practicing Test-Driven Development (TDD) in Python 3.8. All code follows PEP 8 style guidelines (`pycodestyle`), includes proper documentation, and features comprehensive test cases executed with `doctest` and `unittest`.

## Project Requirements
* **Environment:** Ubuntu 20.04 LTS, Python 3.8.5
* **Style Guide:** `pycodestyle` (version 2.8.*)
* **Doctest Execution:** `python3 -m doctest ./tests/*`
* **Unittest Execution:** `python3 -m unittest tests.6-max_integer_test`

---

## Tasks Overview

### 0. Integers Addition
* **File:** `0-add_integer.py` | **Tests:** `tests/0-add_integer.txt`
* **Description:** Function `add_integer(a, b=98)` that adds two integers. Handles type checking and floats by casting them to integers.

### 1. Divide a Matrix
* **File:** `2-matrix_divided.py` | **Tests:** `tests/2-matrix_divided.txt`
* **Description:** Function `matrix_divided(matrix, div)` that divides all elements of a matrix by `div` rounded to 2 decimal places.

### 2. Say my Name
* **File:** `3-say_my_name.py` | **Tests:** `tests/3-say_my_name.txt`
* **Description:** Function `say_my_name(first_name, last_name="")` that prints `My name is <first name> <last name>`.

### 3. Print Square
* **File:** `4-print_square.py` | **Tests:** `tests/4-print_square.txt`
* **Description:** Function `print_square(size)` that prints a square using the `#` character.

### 4. Text Indentation
* **File:** `5-text_indentation.py` | **Tests:** `tests/5-text_indentation.txt`
* **Description:** Function `text_indentation(text)` that prints text with 2 new lines after each of these characters: `.`, `?`, and `:`.

### 5. Max Integer - Unittest
* **File:** `tests/6-max_integer_test.py`
* **Description:** Unittests for the function `max_integer(list=[])` covering all standard and edge cases.

### 6. Matrix Multiplication
* **File:** `100-matrix_mul.py` | **Tests:** `tests/100-matrix_mul.txt`
* **Description:** Function `matrix_mul(m_a, m_b)` that multiplies two matrices following mathematical matrix multiplication rules and input validation.

### 7. Lazy Matrix Multiplication
* **File:** `101-lazy_matrix_mul.py` | **Tests:** `tests/101-lazy_matrix_mul.txt`
* **Description:** Function `lazy_matrix_mul(m_a, m_b)` that multiplies two matrices using the NumPy library.

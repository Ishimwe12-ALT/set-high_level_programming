#!/usr/bin/python3
"""
This module provides a function for matrix multiplication using numpy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using the numpy module.
    """
    return np.matmul(m_a, m_b)

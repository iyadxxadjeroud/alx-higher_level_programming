#!/usr/bin/python3
"""
This module multiply 2 matricies using numpy module
python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)

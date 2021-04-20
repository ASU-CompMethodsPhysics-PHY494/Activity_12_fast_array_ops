import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute


FILENAME = "exercise.py"

@pytest.fixture(scope="module")
def avg_neighbors():
    return get_attribute("avg_neighbors", FILENAME)

def f(x, b):
    y = np.zeros_like(x, dtype=np.float64)
    y[1:-1] = 0.5 * (x[:-2] + x[2:])
    y[0] = y[-1] = b
    return y

@pytest.mark.parametrize('b', [
    np.arange(11),
    np.linspace(-1, 2, 10),
    np.arange(-20, 20, 4)])
def test_avg_neighbors_default(avg_neighbors, b):
    ref = f(b, 100)
    value = avg_neighbors(b)
    assert_almost_equal(value, ref)

@pytest.mark.parametrize('b', [
    np.arange(11),
    np.linspace(-1, 2, 10),
    np.arange(-20, 20, 4)])
def test_avg_neighbors_end(avg_neighbors, b, q=42.24):
    ref = f(b, q)
    value = avg_neighbors(b, end=q)
    assert_almost_equal(value, ref)


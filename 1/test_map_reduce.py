import sys
import numpy as np
import pytest

from mapper_mean import main as map_mean

from mapper_var import main as map_var
from reducer_mean import main as reduce_mean
from reducer_var import main as reduce_var


@pytest.fixture
def map_data():
    lines = [
        ','.join(map(str, [0] * 9 + [1] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [2] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [3] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [4] + [0] * 10)),
    ]
    return lines


@pytest.fixture
def reduce_data_mean():
    lines = [
        ','.join(['1', '2']),
        ','.join(['2', '2']),
        ','.join(['3', '2']),
        ','.join(['4', '2']),
    ]
    return lines


@pytest.fixture
def reduce_data_var():
    lines = [
        ','.join(['0', '1', '2']),
        ','.join(['0', '2', '2']),
        ','.join(['0', '3', '2']),
        ','.join(['0', '4', '2']),
    ]
    return lines


def test_map_mean(map_data):
    result = []
    sys.stdin = map_data
    sys.stdout.write = lambda s: result.append(s[:-1])
    map_mean()

    assert len(result) == 1
    assert int(result[0].split(',')[1]) == 4
    assert float(result[0].split(',')[0]) == np.mean([1, 2, 3, 4])


def test_map_var(map_data):
    result = []
    sys.stdin = map_data
    sys.stdout.write = lambda s: result.append(s[:-1])
    map_var()

    assert len(result) == 1
    assert int(result[0].split(',')[2]) == 4
    assert float(result[0].split(',')[0]) == np.var([1, 2, 3, 4])
    assert float(result[0].split(',')[1]) == np.mean([1, 2, 3, 4])


def test_reduce_mean(reduce_data_mean):
    result = []
    sys.stdin = reduce_data_mean
    sys.stdout.write = lambda s: result.append(s[:-1])
    reduce_mean()

    assert len(result) == 1
    assert float(result[0]) == np.mean([1, 2, 3, 4])


def test_reduce_var(reduce_data_var):
    result = []
    sys.stdin = reduce_data_var
    sys.stdout.write = lambda s: result.append(s[:-1])
    reduce_var()

    assert len(result) == 1
    assert float(result[0]) == np.var([1, 2, 3, 4])

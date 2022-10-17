import sys
import numpy as np
import pytest

from mapper_mean import main as map_mean
from mapper_var import main as map_var


@pytest.fixture
def data():
    lines = [
        ','.join(map(str, [0] * 9 + [1] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [2] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [3] + [0] * 10)),
        ','.join(map(str, [0] * 9 + [4] + [0] * 10)),
    ]
    return lines


def test_map_mean(data):
    result = []
    sys.stdin = data
    sys.stdout.write = lambda s: result.append(s[:-1])
    map_mean()

    assert len(result) == 1
    assert np.mean([1, 2, 3, 4]) == float(result[0])


def test_map_var(data):
    result = []
    sys.stdin = data
    sys.stdout.write = lambda s: result.append(s[:-1])
    map_var()

    assert len(result) == 1
    assert np.var([1, 2, 3, 4]) == float(result[0])

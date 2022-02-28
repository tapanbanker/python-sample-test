import pytest
from module import foo


def test_add_pi():
    assert foo.add_pi(4) == pytest.approx(7.14, abs=0.01)


def test_times_two():
    assert foo.multiply_two(4) == 8

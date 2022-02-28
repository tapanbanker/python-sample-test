import pytest
import module.bar


def test_multiply_two_add_pi():
    assert module.bar.multiply_two_add_pi(4) == pytest.approx(11.14, abs=0.01)

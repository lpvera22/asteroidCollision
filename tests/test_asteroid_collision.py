import pytest

from main import asteroid_collision


def test_example_1():
    """
    Check if asteroid_collision() returns the correct output for a given input.
    """
    assert asteroid_collision([5, 10, -5]) == [5, 10]


def test_example_2():
    """
    Tests the asteroid_collision function with a specific input of [8, -8].
    """
    assert asteroid_collision([8, -8]) == []


def test_example_3():
    """
    Test the asteroid_collision method, for example, number 3 of the problem description.
    """
    assert asteroid_collision([10, 2, -5]) == [10]


def test_example_4():
    """
    Test the asteroid_collision method, for example, number 4 of the problem description.
    """
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]


def test_start_negative():
    """
    This method `test_start_negative` tests the `asteroid_collision` function with a negative input collision first.

    """
    assert asteroid_collision([-2, 1, 1, 2]) == [-2, 1, 1, 2]


def test_no_asteroids():
    """
    Test method to verify the behavior of the `asteroid_collision` function when provided an empty list of asteroids.

    """
    assert asteroid_collision([]) == []


def test_single_asteroid():
    """
    Test the `asteroid_collision` method when given a single asteroid.
    """
    assert asteroid_collision([1]) == [1]
    assert asteroid_collision([-1]) == [-1]


if __name__ == "__main__":
    pytest.main()

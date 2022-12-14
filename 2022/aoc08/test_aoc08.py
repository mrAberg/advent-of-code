# test_aoc_template.py

import pathlib
import pytest
import aoc08 as aoc
import numpy

PUZZLE_DIR = pathlib.Path(__file__).parent

# TODO: Some problems have more than one example


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    comparison = example1 == numpy.array(
        [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
    )

    assert comparison.all()


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 8


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...

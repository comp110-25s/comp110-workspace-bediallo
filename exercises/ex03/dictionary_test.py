"""Unit tests."""

__author__: str = "730811928"


def test_invert_use1():
    """Inverts the keys and values."""
    assert invert({"elden": "ring", "dark": "souls"}) == {
        "ring": "elden",
        "souls": "dark",
    }


def test_invert_use2():
    """Also inverts the keys and values."""
    assert invert({"james": "bond", "john": "wick"}) == {
        "bond": "james",
        "wick": "john",
    }


def test_invert_edge():
    """Invert error."""

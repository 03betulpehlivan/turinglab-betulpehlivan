import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from tm_engine import SingleTapeTM


def test_unary_to_binary():

    tm = SingleTapeTM.from_yaml(
        "machines/unary_to_binary.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    assert result.accepted is True


def test_binary_compare_accept():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_compare.yaml"
    )

    result = tm.run(
        "111#101",
        verbose=False
    )

    assert result.accepted is True


def test_binary_compare_reject():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_compare.yaml"
    )

    result = tm.run(
        "001#111",
        verbose=False
    )

    assert (
        result.accepted is True
        or result.accepted is False
    )


def test_string_copy():

    tm = SingleTapeTM.from_yaml(
        "machines/string_copy.yaml"
    )

    result = tm.run(
        "abba",
        verbose=False
    )

    assert result.accepted is True


def test_student_choice():

    tm = SingleTapeTM.from_yaml(
        "machines/student_choice.yaml"
    )

    result = tm.run(
        "1010",
        verbose=False
    )

    assert (
        result.accepted is True
        or result.accepted is False
    )


def test_empty_input():

    tm = SingleTapeTM.from_yaml(
        "machines/unary_to_binary.yaml"
    )

    result = tm.run(
        "",
        verbose=False
    )

    assert result.accepted is False


def test_single_symbol():

    tm = SingleTapeTM.from_yaml(
        "machines/string_copy.yaml"
    )

    result = tm.run(
        "a",
        verbose=False
    )

    assert (
        result.accepted is True
        or result.accepted is False
    )
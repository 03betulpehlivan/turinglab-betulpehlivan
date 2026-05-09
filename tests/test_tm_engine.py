import os
import sys

import pytest

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from tm_engine import SingleTapeTM
from tm_engine import TMConfiguration


def test_binary_increment():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    assert result.accepted is True

    assert result.reason == "accept"


def test_unary_zero_checker():

    tm = SingleTapeTM.from_yaml(
        "machines/unary_zero_checker.yaml"
    )

    result = tm.run(
        "0000",
        verbose=False
    )

    assert result.accepted is True


def test_timeout():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    result = tm.run(
        "111111111111",
        verbose=False,
        max_steps=1
    )

    assert result.accepted is False

    assert result.reason == "timeout"


def test_invalid_input():

    tm = SingleTapeTM.from_yaml(
        "machines/unary_zero_checker.yaml"
    )

    result = tm.validate_input(
        "abc"
    )

    assert result is False


def test_no_transition():

    tm = SingleTapeTM.from_yaml(
        "machines/unary_zero_checker.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    assert result.accepted is False

    assert (
        result.reason == "reject"
        or result.reason == "no_transition"
    )


def test_verbose_output(capsys):

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    tm.run(
        "111",
        verbose=True
    )

    captured = capsys.readouterr()

    assert "Adım" in captured.out

    assert "Durum" in captured.out

    assert "Şerit" in captured.out


def test_invalid_yaml():

    with pytest.raises(Exception):

        SingleTapeTM.from_yaml(
            "machines/not_existing.yaml"
        )


def test_machine_list():

    machines = SingleTapeTM.list_machines()

    assert len(machines) > 0


def test_history_configuration():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    first_config = result.history[0]

    assert isinstance(
        first_config,
        TMConfiguration
    )

    assert hasattr(
        first_config,
        "state"
    )

    assert hasattr(
        first_config,
        "tape"
    )

    assert hasattr(
        first_config,
        "head_position"
    )

    assert hasattr(
        first_config,
        "step"
    )
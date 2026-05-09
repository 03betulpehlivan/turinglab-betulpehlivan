from tm_engine import SingleTapeTM

from visualizer import draw_tape
from visualizer import generate_frames
from visualizer import generate_gif


def test_draw_tape():

    tape = [
        "1",
        "0",
        "1",
        "1"
    ]

    draw_tape(
        tape=tape,
        head_position=2,
        state="q0",
        step=5,
        output_path="docs/images/test.png"
    )

    assert True


def test_generate_frames():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    generate_frames(result)

    assert len(result.history) > 0


def test_generate_gif():

    tm = SingleTapeTM.from_yaml(
        "machines/binary_increment.yaml"
    )

    result = tm.run(
        "111",
        verbose=False
    )

    generate_frames(result)

    generate_gif()

    assert True
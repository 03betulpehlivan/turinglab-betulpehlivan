import os

from PIL import Image
from PIL import ImageDraw

import imageio.v2 as imageio

CELL_SIZE = 60
PADDING = 40

FIXED_WIDTH = 500
FIXED_HEIGHT = 220


def clear_old_frames():
    """
    Removes old generated frames and GIFs.
    """

    folder = "docs/images"

    for file in os.listdir(folder):

        if (
            file.startswith("frame_")
            or file == "tm.gif"
            or file == "test.png"
        ):

            path = os.path.join(
                folder,
                file
            )

            os.remove(path)


def draw_tape(
    tape,
    head_position,
    state,
    step,
    output_path
):
    """
    Draws a single TM tape frame.
    """

    image = Image.new(
        "RGB",
        (FIXED_WIDTH, FIXED_HEIGHT),
        "#f5f5f5"
    )

    draw = ImageDraw.Draw(image)

    state_color = "#1e88e5"

    if "accept" in state.lower():

        state_color = "#43a047"

    elif "reject" in state.lower():

        state_color = "#e53935"

    draw.rounded_rectangle(
        [20, 15, 340, 60],
        radius=12,
        fill="#ffffff",
        outline="#d0d0d0",
        width=2
    )

    draw.text(
        (35, 30),
        f"STATE : {state}",
        fill=state_color
    )

    draw.text(
        (210, 30),
        f"STEP : {step}",
        fill="#6d4c41"
    )

    tape_width = (
        len(tape) * CELL_SIZE
    )

    start_x = (
        FIXED_WIDTH - tape_width
    ) // 2

    for i, symbol in enumerate(tape):

        x1 = (
            i * CELL_SIZE
        ) + start_x

        y1 = 100

        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE

        fill_color = "#ffffff"

        border_color = "#212121"

        border_width = 2

        if i == head_position:

            fill_color = "#ffebee"

            border_color = "#e53935"

            border_width = 4

            draw.text(
                (x1 + 20, y1 - 28),
                "▼",
                fill="#e53935"
            )

        draw.rounded_rectangle(
            [x1, y1, x2, y2],
            radius=8,
            fill=fill_color,
            outline=border_color,
            width=border_width
        )

        draw.text(
            (x1 + 22, y1 + 18),
            symbol,
            fill="#111111"
        )

    image.save(output_path)


def generate_frames(result):
    """
    Generates PNG frames from TM execution.
    """

    clear_old_frames()

    max_length = 0

    for config in result.history:

        clean_length = len(
            config.tape
            .replace("[", "")
            .replace("]", "")
        )

        if clean_length > max_length:

            max_length = clean_length

    global FIXED_WIDTH

    FIXED_WIDTH = (
        max_length * CELL_SIZE
    ) + 200

    for config in result.history:

        clean_tape = []

        for char in config.tape:

            if char not in ["[", "]"]:

                clean_tape.append(char)

        draw_tape(
            tape=clean_tape,
            head_position=config.head_position,
            state=config.state,
            step=config.step,
            output_path=(
                f"docs/images/frame_{config.step}.png"
            )
        )


def generate_gif():
    """
    Creates animated GIF from frames.
    """

    frames = []

    files = sorted(
        [
            file
            for file in os.listdir(
                "docs/images"
            )
            if file.startswith("frame_")
            and file.endswith(".png")
        ]
    )

    for file in files:

        path = os.path.join(
            "docs/images",
            file
        )

        image = imageio.imread(path)

        frames.append(image)

    if len(frames) > 0:

        imageio.mimsave(
            "docs/images/tm.gif",
            frames,
            duration=0.45
        )
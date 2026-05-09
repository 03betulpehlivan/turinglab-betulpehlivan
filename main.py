from colorama import Fore
from colorama import Style
from colorama import init
from tm_engine import MultiTapeTM
from tm_engine import SingleTapeTM

from visualizer import generate_frames
from visualizer import generate_gif

init(autoreset=True)


def print_header():

    print(
        Fore.CYAN +
        "\nTURINGLAB SIMULATOR"
    )

    print(
        Fore.CYAN +
        "-" * 40
    )


def print_result(result):

    print(
        Fore.CYAN +
        "\nRESULT"
    )

    print("-" * 40)

    status_color = (
        Fore.GREEN
        if result.accepted
        else Fore.RED
    )

    print(
        f"Accepted       : "
        f"{status_color}{result.accepted}"
    )

    print(
        f"Reason         : "
        f"{result.reason}"
    )

    print(
        f"Final Tape     : "
        f"{result.final_tape}"
    )

    print(
        f"Steps          : "
        f"{result.steps}"
    )

    print(
        f"Execution Time : "
        f"{max(result.execution_time, 0.000001):.6f} sec"
    )


def print_history(result):

    print(
        Fore.CYAN +
        "\nHISTORY"
    )

    print("-" * 40)

    for config in result.history:

        print(
            f"Step {config.step:<3} | "
            f"State: {config.state:<12} | "
            f"Tape: {config.tape}"
        )


def main():

    print_header()

    machines = (
        SingleTapeTM.list_machines()
    )

    print(
        Fore.YELLOW +
        "\nAVAILABLE MACHINES:\n"
    )

    for i, machine in enumerate(machines):

        print(
            f"{i + 1}. {machine}"
        )

    try:

        choice = int(
            input(
                "\nSelect machine number: "
            )
        )

    except ValueError:

        print(
            Fore.RED +
            "\nInvalid selection!"
        )

        return

    if (
        choice < 1
        or choice > len(machines)
    ):

        print(
            Fore.RED +
            "\nMachine does not exist!"
        )

        return

    selected_machine = (
        machines[choice - 1]
    )

    print(
        Fore.GREEN +
        f"\nSelected: "
        f"{selected_machine}"
    )

    tm = SingleTapeTM.from_yaml(
        f"machines/{selected_machine}"
    )

    print(
        Fore.CYAN +
        f"\nMachine Name: "
        f"{tm.machine_name}"
    )

    input_string = input(
        "\nInput string: "
    )

    if not tm.validate_input(
        input_string
    ):

        print(
            Fore.RED +
            "\nInvalid input "
            "for this machine!"
        )

        return

    result = tm.run(
        input_string,
        verbose=False,
        max_steps=1000
    )

    generate_frames(result)

    generate_gif()

    print_result(result)

    print_history(result)

    print(
        Fore.GREEN +
        "\nGIF generated at:"
    )

    print(
        "docs/images/tm.gif"
    )

    print(
        Fore.CYAN +
        "\nExecution completed."
    )


if __name__ == "__main__":

    main()

    mtm = MultiTapeTM(
        tapes=3
    )

    tapes = mtm.create_tapes(
        "abba"
    )

    print(
        "\nMULTI TAPE TEST"
    )

    mtm.display_tapes(tapes)

    mtm.move_heads(
        tapes,
        ["R", "R", "R"]
    )

    print(
        "\nAFTER MOVEMENT"
    )

    mtm.display_tapes(tapes)

    mtm.write_symbols(
        tapes,
        ["X", "Y", "Z"]
    )

    print(
        "\nAFTER WRITE"
    )

    mtm.display_tapes(tapes)

    print(
        "\nREAD SYMBOLS"
    )

    print(
        mtm.read_symbols(tapes)
    )

    transition = {
        "write": ["1", "0", "X"],
        "move": ["R", "R", "L"],
        "next": "q_next"
    }

    next_state = mtm.execute_transition(
        tapes,
        transition
    )

    print(
        "\nAFTER TRANSITION"
    )

    mtm.display_tapes(tapes)

    print(
        f"\nNEXT STATE: {next_state}"
    )

    sample_mtm = {
        "num_tapes": 3,
        "states": ["q0", "q_accept"],
        "start_state": "q0",
        "accept_states": ["q_accept"],
        "reject_states": [],
        "transitions": {}
    }

    loaded_mtm = MultiTapeTM.from_dict(
        sample_mtm
    )

    print(
        "\nLOADED MULTI TAPE MACHINE"
    )

    print(
        loaded_mtm.num_tapes
    )

    print(
        loaded_mtm.states
    )

    print(
        loaded_mtm.start_state
    )

    real_mtm_data = {
        "num_tapes": 2,

        "states": [
            "q0",
            "q_accept"
        ],

        "start_state": "q0",

        "accept_states": [
            "q_accept"
        ],

        "reject_states": [],

        "transitions": {

            (
                "q0",
                ("a", "B")
            ): {

                "write": [
                    "a",
                    "X"
                ],

                "move": [
                    "R",
                    "R"
                ],

                "next": "q_accept"
            }
        }
    }

    real_mtm = MultiTapeTM.from_dict(
        real_mtm_data
    )

    result = real_mtm.run(
        "abba"
    )

    print(
        "\nREAL MULTI TAPE RUN"
    )

    print(result)
    
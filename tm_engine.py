from dataclasses import dataclass

import os
import time


@dataclass
class TMConfiguration:
    """
    Stores a single TM execution step.
    """

    state: str
    tape: str
    head_position: int
    step: int


@dataclass
class RunResult:
    """
    Stores the result of a TM execution.
    """

    accepted: bool
    final_tape: str
    steps: int
    history: list
    state_history: list
    execution_time: float
    reason: str


class TMValidationError(Exception):
    """
    Raised when YAML definition is invalid.
    """

    pass


class Tape:
    """
    Represents the TM tape.
    """

    def __init__(
        self,
        content,
        blank="B"
    ):

        self.tape = list(content)

        self.head = 0

        self.blank = blank

    def read(self):
        """
        Reads the current tape symbol.
        """

        if 0 <= self.head < len(self.tape):

            return self.tape[self.head]

        return self.blank

    def write(
        self,
        symbol
    ):
        """
        Writes a symbol to the tape.
        """

        if 0 <= self.head < len(self.tape):

            self.tape[self.head] = symbol

        elif self.head == len(self.tape):

            self.tape.append(symbol)

        else:

            while self.head < 0:

                self.tape.insert(
                    0,
                    self.blank
                )

                self.head += 1

            self.tape[self.head] = symbol

    def move(
        self,
        direction
    ):
        """
        Moves tape head.
        """

        if direction == "R":

            self.head += 1

            if self.head == len(self.tape):

                self.tape.append(
                    self.blank
                )

        elif direction == "L":

            self.head -= 1

            if self.head < 0:

                self.tape.insert(
                    0,
                    self.blank
                )

                self.head = 0

    def display(self):
        """
        Returns visual tape representation.
        """

        out = []

        for i, symbol in enumerate(self.tape):

            if i == self.head:

                out.append(f"[{symbol}]")

            else:

                out.append(symbol)

        return "".join(out)


class SingleTapeTM:
    """
    Deterministic single-tape
    Turing machine engine.
    """

    @classmethod
    def from_yaml(
        cls,
        file_path
    ):
        """
        Creates TM from YAML file.
        """

        import yaml

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = yaml.safe_load(file)

        required_fields = [
            "start_state",
            "accept_states",
            "transitions"
        ]

        for field in required_fields:

            if field not in data:

                raise TMValidationError(
                    f"Eksik alan: {field}"
                )

        transitions = {}

        required_transition_fields = [
            "state",
            "read",
            "next",
            "write",
            "move"
        ]

        for t in data["transitions"]:

            for field in required_transition_fields:

                if field not in t:

                    raise TMValidationError(
                        f"Transition alanı eksik: {field}"
                    )

            key = (
                t["state"],
                t["read"]
            )

            value = (
                t["next"],
                t["write"],
                t["move"]
            )

            transitions[key] = value

        return cls(
            transitions=transitions,
            start_state=data["start_state"],
            accept_states=data["accept_states"],
            reject_states=data.get(
                "reject_states",
                []
            ),
            blank_symbol=data.get(
                "blank_symbol",
                "B"
            ),
            machine_name=data.get(
                "name",
                "Unnamed TM"
            ),
            input_alphabet=data.get(
                "input_alphabet",
                []
            )
        )

    def __init__(
        self,
        transitions,
        start_state,
        accept_states,
        reject_states=None,
        blank_symbol="B",
        machine_name="Unnamed TM",
        input_alphabet=None
    ):

        self.transitions = transitions

        self.start_state = start_state

        self.accept_states = accept_states

        self.reject_states = reject_states or []

        self.blank_symbol = blank_symbol

        self.machine_name = machine_name

        self.input_alphabet = input_alphabet or []

    def run(
        self,
        input_string,
        verbose=True,
        max_steps=1000
    ):
        """
        Runs TM on given input.
        """

        tape = Tape(
            input_string,
            blank=self.blank_symbol
        )

        current_state = self.start_state

        start_time = time.time()

        steps = 0

        history = []

        state_history = []

        while (
            current_state not in self.accept_states
            and current_state not in self.reject_states
        ):

            if steps >= max_steps:

                return RunResult(
                    accepted=False,
                    final_tape="".join(
                        tape.tape
                    ),
                    steps=steps,
                    history=history,
                    state_history=state_history,
                    execution_time=(
                        time.time() - start_time
                    ),
                    reason="timeout"
                )

            current_symbol = tape.read()

            key = (
                current_state,
                current_symbol
            )

            if key not in self.transitions:

                return RunResult(
                    accepted=False,
                    final_tape="".join(
                        tape.tape
                    ),
                    steps=steps,
                    history=history,
                    state_history=state_history,
                    execution_time=(
                        time.time() - start_time
                    ),
                    reason="no_transition"
                )

            (
                next_state,
                write_symbol,
                move_direction
            ) = self.transitions[key]

            tape.write(write_symbol)

            tape.move(move_direction)

            current_state = next_state

            steps += 1

            config = TMConfiguration(
                state=current_state,
                tape=tape.display(),
                head_position=tape.head,
                step=steps
            )

            history.append(config)

            state_history.append(
                current_state
            )

            if verbose:

                print(
                    f"Adım {steps} | "
                    f"Durum: {current_state} | "
                    f"Şerit: {tape.display()} | "
                    f"Hareket: {move_direction}"
                )

        execution_time = (
            time.time() - start_time
        )

        final_tape = "".join(
            tape.tape
        )

        reason = (
            "accept"
            if current_state
            in self.accept_states
            else "reject"
        )

        accepted = (
            current_state
            in self.accept_states
        )

        if verbose:

            print(
                f"\nExecution finished: "
                f"{reason.upper()}"
            )

        return RunResult(
            accepted=accepted,
            final_tape=final_tape,
            steps=steps,
            history=history,
            state_history=state_history,
            execution_time=execution_time,
            reason=reason
        )

    @staticmethod
    def list_machines(
        machine_dir="machines"
    ):
        """
        Lists YAML machines.
        """

        machines = []

        for file_name in os.listdir(
            machine_dir
        ):

            if file_name.endswith(
                ".yaml"
            ):

                machines.append(
                    file_name
                )

        return sorted(machines)

    def validate_input(
        self,
        input_string
    ):
        """
        Validates input symbols.
        """

        for symbol in input_string:

            if (
                symbol
                not in self.input_alphabet
            ):

                return False

        return True

class MultiTapeTM:
    """
    Basic multi-tape TM structure.
    """

    def __init__(
        self,
        tapes=2
    ):

        self.num_tapes = tapes

        self.states = []

        self.transitions = {}

        self.start_state = None

        self.accept_states = []

        self.reject_states = []

    @classmethod
    def from_dict(
        cls,
        data
    ):
        """
        Creates MTM from dictionary.
        """

        mtm = cls(
            tapes=data["num_tapes"]
        )

        mtm.states = data["states"]

        mtm.start_state = (
            data["start_state"]
        )

        mtm.accept_states = (
            data["accept_states"]
        )

        mtm.reject_states = (
            data["reject_states"]
        )

        mtm.transitions = (
            data["transitions"]
        )

        return mtm

    def create_tapes(
        self,
        input_string
    ):
        """
        Creates multiple tapes.
        First tape contains input,
        others start blank.
        """

        tape_list = []

        first_tape = Tape(
            input_string
        )

        tape_list.append(
            first_tape
        )

        for _ in range(
            self.num_tapes - 1
        ):

            blank_tape = Tape(
                ""
            )

            if len(blank_tape.tape) == 0:

                blank_tape.tape.append(
                    blank_tape.blank
                )

            tape_list.append(
                blank_tape
            )

        return tape_list

    def display_tapes(
        self,
        tapes
    ):
        """
        Displays all tapes.
        """

        for i, tape in enumerate(tapes):

            print(
                f"Tape {i + 1}: "
                f"{tape.display()}"
            )

    def move_heads(
        self,
        tapes,
        directions
    ):
        """
        Moves all tape heads.
        """

        for tape, direction in zip(
            tapes,
            directions
        ):

            tape.move(direction)

    def write_symbols(
        self,
        tapes,
        symbols
    ):
        """
        Writes symbols to tapes.
        """

        for tape, symbol in zip(
            tapes,
            symbols
        ):

            tape.write(symbol)

    def read_symbols(
        self,
        tapes
    ):
        """
        Reads symbols from all tapes.
        """

        symbols = []

        for tape in tapes:

            symbols.append(
                tape.read()
            )

        return tuple(symbols)

    def execute_transition(
        self,
        tapes,
        transition
    ):
        """
        Executes one MTM transition.
        """

        self.write_symbols(
            tapes,
            transition["write"]
        )

        self.move_heads(
            tapes,
            transition["move"]
        )

        return transition["next"]

    def get_transition(
        self,
        state,
        symbols
    ):
        """
        Gets transition for state and symbols.
        """

        key = (
            state,
            tuple(symbols)
        )

        return self.transitions.get(
            key
        )

    def run(
        self,
        input_string,
        max_steps=100
    ):
        """
        Runs multi-tape TM.
        """

        tapes = self.create_tapes(
            input_string
        )

        current_state = (
            self.start_state
        )

        steps = 0

        while steps < max_steps:

            symbols = (
                self.read_symbols(tapes)
            )

            transition = (
                self.get_transition(
                    current_state,
                    symbols
                )
            )

            if transition is None:

                return {
                    "accepted": False,
                    "reason": "reject",
                    "steps": steps
                }

            current_state = (
                self.execute_transition(
                    tapes,
                    transition
                )
            )

            steps += 1

            if (
                current_state
                in self.accept_states
            ):

                return {
                    "accepted": True,
                    "reason": "accept",
                    "steps": steps
                }

            if (
                current_state
                in self.reject_states
            ):

                return {
                    "accepted": False,
                    "reason": "reject",
                    "steps": steps
                }

        return {
            "accepted": False,
            "reason": "timeout",
            "steps": steps
        }
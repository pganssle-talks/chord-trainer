import argparse
import json
import pathlib
from typing import Any, Mapping, MutableMapping, Sequence, TypeAlias, TypedDict


class SessionItem(TypedDict):
    current_chord: str
    start_time: float
    updated_time: float
    identifications: int
    correct: int
    confusion_matrix: Mapping[str, Mapping[str, int]]
    done: bool


SessionHistory: TypeAlias = Sequence[SessionItem]
ColorSessionMap: TypeAlias = Mapping[str, SessionHistory]
MutableColorSessionMap: TypeAlias = MutableMapping[str, SessionHistory]


def main(
    input_file: pathlib.Path,
    output_file: pathlib.Path,
    profile_name: str | None = None,
    min_completed: int = 0,
):
    if not input_file.exists():
        raise IOError(f"File does not exist: {input_file}")

    with open(input_file, "rt") as f:
        json_data = json.load(f)

    if profile_name is not None:
        profile_orig = profile_name
        profile_name = profile_name.strip().casefold()
        profiles_found = []
        for item_num, profile_data in json_data["state"]["profiles"].items():
            if profile_data["name"].strip().casefold() == profile_name:
                profile_num = item_num
                break
            profiles_found.append(profile_data["name"])
        else:
            raise ValueError(
                f"Could not find profile with name {profile_orig!r}, found: {profiles_found}"
            )

        new_json_data = {
            "state": {
                "profiles": {profile_num: json_data["state"]["profiles"][profile_num]}
            },
            "history": {profile_num: json_data["history"][profile_num]},
        }
        json_data = new_json_data

    history_data: Mapping[str, MutableColorSessionMap] = json_data["history"]

    # Remove any element from the history with fewer than min_completed
    if min_completed:
        for profile in history_data:
            for color, data in history_data[profile].items():
                new_color_data: SessionHistory = [
                    session
                    for session in data
                    if session["identifications"] >= min_completed
                ]
                history_data[profile][color] = new_color_data

    with open(output_file, "wt") as f:
        json.dump(history_data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process input file with optional profile name and minimum completed integer."
    )
    parser.add_argument("input", type=pathlib.Path, help="Path to the input file")
    parser.add_argument("output", type=pathlib.Path, help="Path to the input file")
    parser.add_argument("--profile", type=str, help="User profile name", default=None)
    parser.add_argument(
        "--min_completed", type=int, help="Minimum completed integer", default=0
    )
    args = parser.parse_args()

    main(
        args.input,
        args.output,
        profile_name=args.profile,
        min_completed=args.min_completed,
    )

import argparse
import os
import sys
from itertools import chain
import pandas as pd
import pyperclip
from parse_data import (
    get_dirfiles,
    parse_files,
    pretty_lecture,
    files_to_calendar,
)
from algorithm import build_dataframe, group_names

pd.options.mode.chained_assignment = None


def main(args):
    calendars = files_to_calendar(args["files"])
    people = parse_files(calendars)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    df = build_dataframe(people)
    df = group_names(df)
    output = ""
    for day in days:
        lectures = []
        divider = "{1} {0:^20} {1}".format(f"**{day}**", "*===============*")

        for lecture in df[df.Day == day].sort_values("Start").itertuples(index=False):
            details = pretty_lecture(lecture)
            lectures.append(details)

        output += divider + "".join(lectures) + "\n"

    if args["output"]:
        with open(args["output"], "w") as f:
            f.write(output)
        return
    pyperclip.copy(output)


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("r"),
        nargs="+",
        help="File names to be used",
    )
    group.add_argument(
        "-p",
        "--path",
        type=check_path,
        help="Path to directory containing calendar files",
    )

    parser.add_argument(
        "-o",
        "--output",
        const=None,
        help="File to output to (destructive), omit to copy to clipboard",
    )

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    files = [x for x in [args.file, args.path] if x is not None]
    files = list(chain.from_iterable(files))
    return {"files": files, "output": args.output}


def check_path(path: str) -> list:
    if path and not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")
    return get_dirfiles(path)


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)

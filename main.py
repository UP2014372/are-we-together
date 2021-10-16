import pandas as pd
import pyperclip
from parse_data import get_files, parse_files, pretty_lecture
from algorithm import build_dataframe, group_names

pd.options.mode.chained_assignment = None

if __name__ == "__main__":
    calendars = get_files()
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

    pyperclip.copy(output)

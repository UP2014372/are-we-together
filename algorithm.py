import parse_data
import pandas as pd
from parse_data import get_files, parse_files
from algorithm import build_dataframe, group_names
import pandas as pd
import pyperclip

calendars = parse_data.get_files()
people = parse_data.parse_files(calendars)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def build_dataframe(elements: list):
    frames = []
    for element in elements:
        frames.append(pd.DataFrame(element).dropna())

    df = pd.concat(frames)
    df.reset_index(inplace=True, drop=True)
    return df


def group_names(df: pd.DataFrame):
    lectures = []
    for Day in days:
        i = df.loc[df["Day"] == Day]
        lectures.append(
            i.groupby(["Day", "Start", "End", "Unit"], as_index=False).agg(
                {"Names": " ".join}
            )
        )
    lectures = pd.concat(lectures).reset_index(drop=True)

    del df["Names"]
    df = df.drop_duplicates(["Day", "Start", "End", "Group", "Building"])

    df["Day"] = pd.Categorical(df["Day"], categories=days, ordered=True)
    df = df.sort_values("Day").reset_index(drop=True)

    df = df.merge(lectures)
    return df

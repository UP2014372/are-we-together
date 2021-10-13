import parse_data
import pandas as pd

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
    for day in days:
        i = df.loc[df["day"] == day]
        lectures.append(
            i.groupby(["day", "start", "end", "Unit"], as_index=False).agg(
                {"name": " ".join}
            )
        )
    lectures = pd.concat(lectures).reset_index(drop=True)

    del df["name"]
    df = df.drop_duplicates(["day", "start", "end", "Group", "Building"])

    df["day"] = pd.Categorical(df["day"], categories=days, ordered=True)
    df = df.sort_values("day").reset_index(drop=True)

    df = df.merge(lectures)
    return df

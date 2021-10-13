import parse_data
import pandas as pd

calendars = parse_data.get_files()
people = parse_data.parse_files(calendars)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


frames = []
for person in people:
    frames.append(pd.DataFrame(person).dropna())

df = pd.concat(frames)
df.reset_index(inplace=True, drop=True)

lectures = []
for day in days:
    i = df.loc[df["day"] == day]
    lectures.append(
        i.groupby(["day", "start", "end", "Unit"], as_index=False).agg(
            {"name": " ".join}
        )
    )

del df["name"]
df = df.drop_duplicates(["day", "start", "end", "Group", "Building"])
lectures = pd.concat(lectures).reset_index(drop=True)

df["day"] = pd.Categorical(df["day"], categories=days, ordered=True)
df = df.sort_values("day").reset_index(drop=True)


df.merge(lectures)

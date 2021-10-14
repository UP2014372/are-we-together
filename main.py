from parse_data import get_files, parse_files
from algorithm import build_dataframe, group_names

if __name__ == "__main__":
    calendars = get_files()
    people = parse_files(calendars)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    df = build_dataframe(people)
    df = group_names(df)
    string = ""
    print(df)

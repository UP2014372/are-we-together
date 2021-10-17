import datetime
import os
import icalendar


def get_files() -> list:
    calendars = []
    for _, _, files in os.walk("people/"):
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension == ".ics":
                icalfile = open(f"people/{file}", "rb")
                gcal = icalendar.Calendar.from_ical(icalfile.read())
                calendars.append({"name": filename, "data": gcal})
                icalfile.close()
    return calendars


def parse_description(description: str) -> dict:
    details = {}
    key_value = description.split("\n")
    for i in key_value:
        aux = i.split(": ")
        details[aux[0]] = aux[1]
    return details


def same_week(d1, d2):
    return d1.isocalendar()[1] == d2.isocalendar()[1] and d1.year == d2.year


def parse_files(calendars) -> list:
    people = []
    for calendar in calendars:
        weekly_lectures = []
        for component in calendar["data"].walk():
            lecture = {}
            same = False

            if component.get("dtstart"):
                component_date = component.get("dtstart").dt
                same = same_week(component_date, datetime.date.today())

            if component.name == "VEVENT" and same:
                lecture["Names"] = calendar["name"]
                lecture["Day"] = component.get("dtstart").dt.strftime("%A")
                lecture["Start"] = component.get("dtstart").dt.time()
                lecture["End"] = component.get("dtend").dt.time()
                parsed = parse_description(component.get("description"))
                lecture = dict(list(lecture.items()) + list(parsed.items()))
            weekly_lectures.append(lecture)
        people.append(weekly_lectures)

    return people


def pretty_lecture(lecture) -> list:
    output = (
        "\n"
        "**Module**: " + lecture.Unit + "\n"
        "**Type**: " + lecture.Type + "\n"
        "**Lecturer**: " + lecture.Lecturer + "\n"
        "**Start**: " + lecture.Start.strftime("%H:%M") + "\n"
        "**End**: " + lecture.End.strftime("%H:%M") + "\n"
        "**Group**: " + lecture.Group + "\n"
        "**Building**: " + (lecture.Building if lecture.Building else "N/A") + "\n"
        "**Room**: " + (lecture.Room if lecture.Room else "N/A") + "\n"
        "**People**: `" + format_names(lecture.Names) + "`\n"
    )
    return output


def format_names(names):
    return ", ".join(map(lambda name: name.capitalize(), names.split(" ")))

class Person:
    def __init__(self, name, lectures):
        self.name = name
        self.lectures = [i for i in lectures if i]

    def get_lectures(self, day: str):
        requested = []
        for lecture in self.lectures:
            if lecture["day"] == day:
                requested.append(lecture)
        return requested

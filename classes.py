
template = {
    "conjunction": None,
    "courses": [
        {}
    ]
}


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
class Course:
    def __init__(self, course : dict) -> None:
        self.courseNumber = course["courseNumber"]
        self.courseTitle = course["courseTitle"]
        self.courseUnits = course["courseUnits"]

    def __repr__(self) -> str:
        return self.courseNumber
    
    def make_dict(self) -> dict:
        return {"courseNumber": self.courseNumber, "courseTitle": self.courseTitle, "courseUnits": self.courseUnits}

class Group:
    def __init__(self, grouping, conjunction=None) -> None:
        self.grouping = list(grouping[:])
        # if any(isinstance(ele, Group) for ele in grouping):
        #     self.grouping = grouping
        # else:
        # # if is_iterable(grouping):
        #     self.grouping = []
        #     for course in grouping:
        #         self.grouping.append(Course(course))
        # else:
        #     self.grouping = grouping
        self.conjuntion = conjunction
    
    def __repr__(self) -> str:
        # l = tuple([x["courseNumber"] for x in self.grouping])
        # return f"{self.conjuntion} {[x["courseNumber"] for x in self.grouping]}"
        return f"{self.conjuntion} {self.grouping}"
    
    def add(self, course: dict) -> None:
        if not self.has_course(course):
            # self.grouping.append(Course(course))
            self.grouping.append(course)

    def remove(self, course) -> Course:
        self.grouping.remove(course)
        # for x in self.grouping:
        #     if course["courseNumber"] == x.courseNumber:
        #         self.grouping.remove(x)
        #         return
        # return self.grouping.pop(0)

    def make_dict(self) -> dict:

        template["conjunction"] = self.conjuntion
        template["courses"] = self.grouping
        # courses = []
        # for course in self.grouping:
        #     courses.append(course.make_dict())
        # template["courses"] = courses
        return template
    
    def has_course(self, course) -> bool:
        for x in self.grouping:
            # if course["courseNumber"] == x.courseNumber:
            if course["courseNumber"] == x["courseNumber"]:
                return True
        return False

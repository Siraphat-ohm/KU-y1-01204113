class Course:
    def __init__(self, title, code, credit):
        self.title = title
        self.course_id = code
        self.credit = credit


class Teacher:
    def __init__(self, firstname, lastname, id):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} ({self.id})"


class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"


class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.courses_id = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if (self.total_credit + course.credit <= 25) and (
            course.title not in self.courses
        ):
            self.courses.append(course.title)
            self.courses_id.append(course.course_id)
            self.num_course += 1
            self.total_credit += course.credit

            return True
        return False

    def drop_course(self, course):
        if (self.num_course > 0) and (course.title in self.courses):
            if self.courses[-1] == course.title:
                self.courses.append("")
            self.courses.remove(course.title)
            self.courses_id.remove(course.course_id)
            self.num_course -= 1
            self.total_credit -= course.credit
            return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {' '.join(self.courses_id)} "


# testcase from jjentaa https://github.com/jjentaa/KU-y1-comprog/blob/main/lab08/lab08-05.py
c_ls = "01219111 01219113 01219245 01219221 01204212 01219213 01420113 01420114 01420111".split(
    " "
)
ad = Teacher("Preeda", "Lerdpongvipusana", "E901")
m = Major("E17", "Software & Knowledge Engineering", "Engineering")
s = Student(5610546231, "Chinnaporn", "Soonue")
s.set_advisor(ad)
s.set_major(m)
for i in c_ls:
    s.add_course(Course("sth", i, 1))

print(s)

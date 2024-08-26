class ClassRoom:

    def __init__(self, grade=0, homeRoomTeacher="", students=[], numStudents=0):
        self.grade = grade
        self.tName = homeRoomTeacher
        self.students = students
        self.numStudents = numStudents

        self._maximum = 10

    def set_grade(self, grade):
        self.grade = grade

    def set_homeroom_teacher(self, name):
        self.tName = name

    def set_student_list(self, students):
        self.numStudents = len(students)
        self.students = students

    def set_num_student(self, n):
        self.numStudents = n

    def get_grade(self):
        return self.grade

    def get_homeroom_teacher(self):
        return self.tName

    def get_student_list(self):
        return self.students

    def get_num_student(self):
        return self.numStudents

    def get_student_no(self, n):
        return self.students[n - 1]

    def add_student(self, name):
        if self.numStudents < self._maximum:
            self.students.append(name)
            self.numStudents += 1
            return True
        return False

    def change_student(self, n, new_name):
        if n >= 1 and n <= 10 and n <= self.numStudents:
            self.students[n - 1] = new_name
            return True
        return False

    def remove_student(self, name):
        if name in self.students:
            index = self.students.index(name)
            self.students.pop(index)
            self.numStudents -= 1
            return True
        return False

    def remove_student_no(self, n):
        if n >= 1 and n <= self.numStudents:
            self.students.pop(n - 1)
            self.numStudents -= 1
            return True
        return False

    def __str__(self):
        return f"Grade: {self.grade}\nHomeroom Teacher: {self.tName}\nStudents: {', '.join(self.students)}"


room1 = ClassRoom()
# grade = int(input("Input grade: "))
# homeRoomTeacher = input("Homeroom Teacher: ")
room1.set_grade(8)
room1.set_homeroom_teacher("Supaporn")
print(room1)

# noStudent = int(input("Number of students: "))
studentList = room1.get_student_list()
room1.set_student_list(studentList)
print(room1)

room1.add_student("Chinnaporn Soonue")
room1.add_student("Punpikorn Rattanawirojkul")

# for i in range(noStudent):
#     temp = input(f"Student No{i+1}: ")
#     if not room1.add_student(temp):
#         print("Exceed 10 students.")
print(room1)
print("Grade", room1.get_grade())
print("Homeroom Teacher", room1.get_homeroom_teacher())
for i in range(room1.get_num_student()):
    print(f"No.{i+1}: {room1.get_student_no(i+1)}")

# test change_student
print(">>>>>> Testing change student")
if room1.change_student(room1.get_num_student(), "Abby"):
    print(room1)
if not room1.change_student(room1.get_num_student() + 2, "Abby"):
    print(f"Cannot change {room1.get_num_student()+2}th student")
if not room1.change_student(13, "Abby"):
    print("Index out of bound. Cannot change 13th student.")
if not room1.change_student(-1, "Abby"):
    print("Index out of bound. Cannot change -1th student.")

# test remove_student(name)
print(">>>>>> Testing remove student (name)")
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(1))
    print(room1)
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(room1.get_num_student()))
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student(room1.get_student_no(2))
    print(room1)

# test remove_student(int)
print(">>>>>> Testing remove student no.")
room1.add_student("Bob")
room1.add_student("Mary")
room1.add_student("Adam")
if room1.get_num_student() >= 1:
    if room1.remove_student_no(1):
        print(room1)
    if not room1.remove_student_no(8):
        print(
            f"8 is invalid student number. There are only {room1.get_num_student()} students."
        )
if room1.get_num_student() >= 1:
    room1.remove_student_no(room1.get_num_student())
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if not room1.remove_student_no(-2):
    print("Index out of bound. Cannot remove -2th student.")
if not room1.remove_student_no(12):
    print("Index out of bound. Cannot remove 12th student.")

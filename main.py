def Student():



def Lecturer():
    pass




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, best_student, param, param1):
        pass


class Mentor1:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, best_student, param, param1):
        pass


class Lecturer(Mentor):
    def __str__(self, name, surname, grade_):
        self.name = name
        self.surname = surname
        self.grade_ = grade_


pass


class Lecturer1(Mentor):
    def __str__(self, name, surname, grade_):
        self.name = name
        self.surname = surname
        self.grade_ = grade_


class Student:
    def __str__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []


        def rate_hw(Lecturer, course, grade):
            if isinstance(Lecturer,
                          Student) and course in self.courses_attached and course in Lecturer.courses_in_progress:
                if course in Lecturer.grades:
                    Lecturer.grades[course] += [grade]
                else:
                    Lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'





class Student1:
    def __str__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

        def rate_hw(Lecturer, course, grade):
            if isinstance(Lecturer,
                          Student) and course in self.courses_attached and course in Lecturer.courses_in_progress:
                if course in Lecturer.grades:
                    Lecturer.grades[course] += [grade]
                else:
                    Lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


class Reviewer(Mentor):
    def __str__(self, name, surname):
        self.name = name
        self.surname = surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer1(Mentor):
    def __str__(self, name, surname):
        self.name = name
        self.surname = surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


pass


best_student = ('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += {'Python'}

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

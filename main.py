
class Student:
    def __init__(self, name, surname, gender, gradestu_):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        print(self.name)
        print(self.surname)
        print(self.courses_in_progress)
        print(self.finished_courses)
        print(self.gradestu_)
        gradestu_ = sum(Student.grades) / len(Student.grades)

        def rate_hw(self, Lecturer, course, grade):
            if isinstance(Lecturer,
                          Student) and course in self.courses_attached and course in Lecturer.courses_in_progress:
                if course in Lecturer.grades:
                    Lecturer.grades[course] += [grade]
                else:
                    Lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


eval_ = {}
class Student1:
    def __init__(self, name, surname, gender, gradestu_):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        print(self.name)
        print(self.surname)
        print(self.courses_in_progress)
        print(self.finished_courses)
        print(self.gradestu_)
        gradestu_ = sum(Student.grades) / len(Student.grades)

        def rate_hw(self, Lecturer, course, grade):
            if isinstance(Lecturer,
                          Student) and course in self.courses_attached and course in Lecturer.courses_in_progress:
                if course in Lecturer.grades:
                    Lecturer.grades[course] += [grade]
                else:
                    Lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
eval_ = {}


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


class Reviewer(Mentor):
    def __init__(self, name, surname):
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
    def __init__(self, name, surname):
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

class Lecturer(Mentor):
    def __init__(self, name, surname, grade_):
        self.name = name
        self.surname = surname
        self.grade_ = grade_
        self.courses_in_progress = []

        grade_ = sum(Lecturer.grades) / len(Lecturer.grades)
        var = {self.courses_in_progress: self.grade_}


pass

class Lecturer1(Mentor):
    def __init__(self, name, surname, grade_):
        self.name = name
        self.surname = surname
        self.grade_ = grade_
        self.courses_in_progress = []

        grade_ = sum(Lecturer.grades) / len(Lecturer.grades)
        var = {self.courses_in_progress: self.grade_}


pass
if Student.gradestu_ > Student1.gradestu_:
    print('оценка выше у первого студента')
else:
    print('оценка выше у второго студента')

if Lecturer.gradestu_ > Lecturer1.gradestu_:
    print('оценка выше у первого лектора')
else:
    print('оценка выше у второго лектора')



best_student = ('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

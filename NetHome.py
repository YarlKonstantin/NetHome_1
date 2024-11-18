'''ЗАДАЧА_1 / ЗАДАЧА_2 / ЗАДАЧА_3 / ЗАДАЧА_4'''



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                  f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                  f'Завершенные курсы: {self.finished_courses}')
        return result

    def __gt__(self, other):
        if self.average_grade() > other.average_grade():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.average_grade() >= other.average_grade():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.average_grade() == other.average_grade():
            return True
        else:
            return False

    def average_grade(self):
        grade = 0
        count = 0
        for subject in self.grades:
            grade += sum(self.grades[subject])
            count += len(self.grades[subject])
        return grade/count

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached
                and grade in range(1, 11)
                and course in self.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
     def __str__(self):
         result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
         return result

     def __init__(self, name, surname):
         super().__init__(name, surname)
         self.grades = {}

     def __gt__(self, other):
        if self.average_grade() > other.average_grade():
            return True
        else:
            return False

     def __ge__(self, other):
         if self.average_grade() >= other.average_grade():
             return True
         else:
             return False

     def __eq__(self, other):
         if self.average_grade() == other.average_grade():
             return True
         else:
             return False


     def average_grade(self):
        grade = 0
        count = 0
        for subject in self.grades:
            grade += sum(self.grades[subject])
            count += len(self.grades[subject])
        return grade/count

class Reviewer(Mentor):
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def medium_grade_homework(student_list, course):
    sum_grades = 0
    for student in student_list:
        if course in student.grades:
            sum_grades += sum(student.grades[course])/len(student.grades[course])
    return sum_grades / len(student_list)

def medium_grade_lections(lectors_list, course):
    sum_grades = 0
    for lector in lectors_list:
        print(lector.grades)
        if course in lector.grades:
            sum_grades += sum(lector.grades[course])/len(lector.grades[course])
    return sum_grades / len(lectors_list)




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'API']
best_student.finished_courses += ['Введение в программирование']

worst_student = Student('Max', 'Eman', 'your_gender')
worst_student.courses_in_progress += ['Python', 'API']
worst_student.finished_courses += ['Введение в программирование']

lector_1 = Lecturer('Ivan', 'Ivanov')
lector_1.courses_attached += ['Python']
lector_2 = Lecturer('Evgeniy', 'Ryumkin')
lector_2.courses_attached += ['API']




reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_2 = Reviewer('Alex', 'Alexeev')

reviewer_1.courses_attached += ['API']
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(best_student, 'API', 10)
reviewer_2.rate_hw(best_student, 'Python', 9)
reviewer_1.rate_hw(worst_student, 'API', 9)
reviewer_2.rate_hw(worst_student, 'Python', 10)

best_student.rate_lector(lector_2, 'API', 5)
best_student.rate_lector(lector_1, 'Python', 10)

worst_student.rate_lector(lector_2, 'API', 3)
worst_student.rate_lector(lector_1, 'Python', 7)

list_student = [best_student, worst_student]

list_lectors = [lector_1]





# print(medium_grade_homework(list_student, 'Python'))
# print(medium_grade_lections(list_lectors, 'Python'))
#
# print(reviewer_1)
#
# print(lector_1)
#
# print(lector_1.grades)
#
# print(best_student > worst_student)
# print(worst_student == best_student)
# print(best_student >= worst_student)
# print(best_student <= worst_student)
# print(best_student != worst_student)
#
# print(lector_1 > lector_2)
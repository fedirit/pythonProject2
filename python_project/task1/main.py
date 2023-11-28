# списки студентов и лекторов, в которые конструктором соответсвующего класса помещаем self экземпляр класса
Students_list = []
Lecturer_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}
        self.average_grade = 0
        Students_list.append(self)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не является студентом!")
            return
        return self.average_grade < other.average_grade

    def rate_hw_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_attached and
                course in lecturer.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        Mentor.__init__(self, name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        Lecturer_list.append(self)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не явялется лектором!")
            return
        return self.average_grade < other.average_grade


class Reviewer(Mentor):

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# определение средней оценки студентов или лекторов за курс
# первым аргументом указывается класс в зависимости от этого определяется список
# задание 4 реализовал одной функцией вместо двух, определяется нужный список по классу объекта в первом параметре
def average_rate(group, course):
    Mark_list = []
    flag = True
    if group == Student:
        Mark_list = []
        flag = True
        for i in range(len(Students_list)):
            if course in Students_list[i].grades:
                flag = False
                Mark_list += Students_list[i].grades[course]

        if flag == True:
            print(f'Курс {course} студенты не проходили или нет ни одной оценки')

        else:
            average_mark = sum(Mark_list) / len(Mark_list)
            print(f'Средняя оценка студентов за курс {course} составляет {average_mark}')


    elif group == Lecturer:

        for i in range(len(Lecturer_list)):
            if course in Lecturer_list[i].grades:
                flag = False
                Mark_list += Lecturer_list[i].grades[course]

        if flag == True:
            print(f'Курс {course} не преподается у лекторов или нет ни одной оценки')

        else:
            average_mark = sum(Mark_list) / len(Mark_list)
            print(f'Средняя оценка лекторов за курс {course} составляет {average_mark}')


# создадим экземпляры класса Student
Pedro = Student("Pedro", "Sanchez", "men")
Pedro.courses_in_progress.append("Math")
Pedro.courses_in_progress.append("IT")
Pedro.courses_in_progress.append("English")
Pedro.courses_in_progress.append("Russian")
Pedro.average_grade = 5.3 # в условии заданий не определено каким образом определять среднее значение у студентов
# и лекторов
# создалось ощущуение, что в комментариях Вопросы и ответы, к ДЗ, вопросы студентов и ответы преподователей
# содержится информация, относящаяся к формулировкам задания предыдущих версий, причем формулировки менялись
# что определенно влияет на неоднозначное восприятие задания, поэтому не буду морочится установлю вручную
Pedro.finished_courses.append("Java")
Pedro.finished_courses.append("Spain")

Hulio = Student("Hulio", "Iglesias", "men")
Hulio.courses_in_progress.append("Python")
Hulio.courses_in_progress.append("IT")
Hulio.courses_in_progress.append("English")
Hulio.courses_in_progress.append("Russian")
Hulio.courses_in_progress.append("Spain")
Hulio.average_grade = 7.3
Hulio.courses_attached.append("Python")
Hulio.finished_courses.append("Java")

Conchita = Student("Conchita", "Bonita", "women")
Conchita.courses_in_progress.append("Math")
Conchita.courses_in_progress.append("Russian")
Conchita.courses_in_progress.append("Python")
Conchita.average_grade = 8.8
Conchita.courses_attached.append("Python")
Conchita.courses_attached.append("Spain")
Conchita.courses_attached.append("English")
Conchita.finished_courses.append("Java")

Antony = Lecturer("Anton", "Ptushkin", "men")
Antony.courses_attached.append("Python")
Antony.courses_attached.append("English")
Antony.courses_attached.append("IT")
Antony.average_grade = 9.8
Antony.courses_in_progress.append("Python")
Antony.courses_in_progress.append("English")
Antony.courses_in_progress.append("IT")

Helena = Lecturer("Helena", "Nikitina", "women")
Helena.courses_attached.append("Python")
Helena.courses_attached.append("Spain")
Helena.courses_attached.append("English")
Helena.average_grade = 2
Helena.courses_in_progress.append("Python")

Alexander = Reviewer("Alexander", "Bardin")
Alexander.courses_attached.append("Python")
Alexander.courses_attached.append("IT")

Igor = Reviewer("Igor", "Sverchkov")
Igor.courses_attached.append("Math")
Igor.courses_attached.append("Russian")

# Reviewer оценивает Student-ов
# метод rate_hw работает корректно, предметы которые не относятся к Reviewer не доступны к оценке
# в результате для студента Pedro получили 'grades': {'IT': [5, 4]}
Alexander.rate_hw(Pedro, "Math", 5)
Alexander.rate_hw(Pedro, "Math", 4)
Alexander.rate_hw(Pedro, "Math", 2)
Alexander.rate_hw(Pedro, "IT", 5)
Alexander.rate_hw(Pedro, "IT", 4)
Alexander.rate_hw(Pedro, "English", 4)
Alexander.rate_hw(Pedro, "English", 5)
Alexander.rate_hw(Pedro, "English", 5)
Alexander.rate_hw(Pedro, "Russian", 5)
Alexander.rate_hw(Pedro, "Russian", 5)
Alexander.rate_hw(Pedro, "Russian", 5)

# для Hulio лишнего, то чего не могут Reviewer не оцениваем
Igor.rate_hw(Hulio, "Russian", 5)
Igor.rate_hw(Hulio, "Russian", 5)
Igor.rate_hw(Hulio, "Russian", 5)
Alexander.rate_hw(Hulio, "Python", 5)
Alexander.rate_hw(Hulio, "Python", 5)
Alexander.rate_hw(Hulio, "Python", 5)

# для Conchita лишнего, то чего не могут Reviewer не оцениваем
Igor.rate_hw(Conchita, "Russian", 5)
Igor.rate_hw(Conchita, "Russian", 4)
Igor.rate_hw(Conchita, "Russian", 5)
Alexander.rate_hw(Conchita, "Python", 4)
Alexander.rate_hw(Conchita, "Python", 5)
Alexander.rate_hw(Conchita, "Python", 10)
Igor.rate_hw(Conchita, "Math", 5)
Igor.rate_hw(Conchita, "Math", 4)
Igor.rate_hw(Conchita, "Math", 8)
Igor.rate_hw(Conchita, "Math", 5)
Igor.rate_hw(Conchita, "Math", 10)
Igor.rate_hw(Conchita, "Math", 5)

# Student оценивает Lecturer-ов
Conchita.rate_hw_lecturer(Antony, "Python", 5)
Conchita.rate_hw_lecturer(Antony, "Python", 6)
Conchita.rate_hw_lecturer(Antony, "Python", 7)
Conchita.rate_hw_lecturer(Antony, "Python", 8)
Conchita.rate_hw_lecturer(Antony, "Python", 9)

Hulio.rate_hw_lecturer(Helena, "Python", 1)
Hulio.rate_hw_lecturer(Helena, "Python", 2)
Hulio.rate_hw_lecturer(Helena, "Python", 3)
Hulio.rate_hw_lecturer(Helena, "Python", 2)
Hulio.rate_hw_lecturer(Helena, "Python", 1)

# определеляем средние оценки по каждому курсу студентов
average_rate(Student, "Math")
average_rate(Student, "Python")
average_rate(Student, "IT")
average_rate(Student, "English")
average_rate(Student, "Russian")
average_rate(Student, "Spain")

# определеляем средние оценки по каждому курсу лекторов
average_rate(Lecturer, "Math")
average_rate(Lecturer, "Python")
average_rate(Lecturer, "IT")
average_rate(Lecturer, "English")
average_rate(Lecturer, "Russian")
average_rate(Lecturer, "Spain")

# поупражняемся с полиморфизмом, переопределим __str__ для каждого класса
print('')
print('// ============================================')
print(Pedro.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Hulio.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Conchita.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Antony.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Helena.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Alexander.__str__())
print('// ============================================')
print('')

print('// ============================================')
print(Igor.__str__())
print('// ============================================')
print('')

# посравниваем
print('// ============================================')
print('Pedro > Hulio', Pedro > Hulio)
print('Pedro < Hulio', Pedro < Hulio)
print('Pedro != Hulio', Pedro != Hulio)

print('Pedro > Conchita', Pedro > Conchita)
print('Pedro < Conchita', Pedro < Conchita)
print('Pedro != Conchita', Pedro != Conchita)

print('Hulio > Conchita', Hulio > Conchita)
print('Hulio < Conchita', Hulio < Conchita)
print('Hulio != Conchita', Hulio != Conchita)

print('Antony > Helena', Antony > Helena)
print('Antony < Helena', Antony < Helena)
print('Antony != Helena', Antony != Helena)
print('// ============================================')
print('')

# выводим __dict__ по каждому экземпляру класса, чтобы понимать обстановку
print(Pedro.__dict__)
print(Hulio.__dict__)
print(Conchita.__dict__)
print(Antony.__dict__)
print(Helena.__dict__)
print(Alexander.__dict__)
print(Igor.__dict__)
print(Students_list)
print(Lecturer_list)


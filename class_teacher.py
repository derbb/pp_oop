# Первое задание

class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, years):
        if isinstance(years, int) and years >= 0:
            self._experience = years
        else:
            raise ValueError("Опыт работы должен быть неотрицательным целым числом.")

    def get_teacher_data(self):
        return f"\n{self.name}, образование {self.education}, опыт работы {self.experience} год/года/лет."

    def add_mark(self, mark, student_name):
        return f"\n{self.name} поставил оценку {mark} студенту {student_name}."

    def remove_mark(self, mark, student_name):
        return f"\n{self.name} удалил оценку {mark} студенту {student_name}."

    def give_a_consultation(self, class_name):
        return f"\n{self.name} провёл консультацию в классе {class_name}."


# Второе задание

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    @property
    def discipline(self):
        return self._discipline

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, new_job_title):
        if isinstance(new_job_title, str) and new_job_title:
            self._job_title = new_job_title
        else:
            raise ValueError("Должость должна быть непустой строкой.")

    def get_teacher_data(self):
        return f"\n{self.name}, образование {self.education}, опыт работы {self.experience} год/года/лет.\nПредмет {self.discipline}, должность {self.job_title}."

    def add_mark(self, mark, student_name):
        return f"\n{self.name} поставил оценку {mark} студенту {student_name}.\nПредмет: {self.discipline}."

    def remove_mark(self, mark, student_name):
        return f"\n{self.name} удалил оценку {mark} студенту {student_name}.\nПредмет: {self.discipline}."

    def give_a_consultation(self, class_name):
        return f"\n{self.name} провёл консультацию в классе {class_name}.\nПо предмету {self.discipline} как {self.job_title}."


teacher1 = Teacher("Иван Петров", "БГПУ", 4)
print(teacher1.get_teacher_data())
print(teacher1.add_mark(4, "Пётр Сидоров"))
print(teacher1.remove_mark(3, "Дмитрий Степанов"))
print(teacher1.give_a_consultation("9Б"))

discipline_teacher = DisciplineTeacher("Алексей Иванов", "МГУ", 10, "Математика", "Завуч")

print(discipline_teacher.get_teacher_data())
print(discipline_teacher.add_mark(5, "Анна Кузнецова"))
print(discipline_teacher.remove_mark(2, "Виктор Смирнов"))
print(discipline_teacher.give_a_consultation("11А"))

# Изменение должности
discipline_teacher.job_title = "Директор"
print(f"\nОбновленная должность: {discipline_teacher.job_title}")
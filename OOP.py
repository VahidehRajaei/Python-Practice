# ==========================
# Person Class
# ==========================
class Person:
    count = 0

    def __init__(self, personnel_code, name, last_name):
        self.__personnel_code = personnel_code
        self.name = self.__caps_lock(name)
        self.last_name = self.__caps_lock(last_name)
        Person.count += 1

    def _general_info(self):
        print(
            f"String Output:\tCount of Sample: {Person.count}\tPersonnel Code: {self.__personnel_code}"
            f"\tName: {self.name}\tLast Name: {self.last_name}"
        )

    def get_personnel_code(self):
        return self.__personnel_code

    def set_personnel_code(self, new_code):
        self.__personnel_code = new_code

    def __caps_lock(self, text):
        return text.upper()


# ==========================
# Managers Class 
# ==========================
class Managers(Person):

    def __init__(self, personnel_code, name, last_name, salary_amount):
        super().__init__(personnel_code, name, last_name)
        self.__salary_amount = salary_amount

    def show_info_manager(self):
        self._general_info()
        print(f"Salary Amount: {self.__salary_amount}")
        print(f"List Output: {list((self.get_personnel_code(), self.name, self.last_name, self.__salary_amount))}")


# ==========================
# Employees Class 
# ==========================
class Employees(Person):

    def __init__(self, personnel_code, name, last_name, grade):
        super().__init__(personnel_code, name, last_name)
        self.__grade = self.input_grade(grade)

    def input_grade(self, grade):
        grade = grade.upper()
        allowed_grades = ['A', 'B', 'C', 'D']
        return grade if grade in allowed_grades else 0

    def show_info_employee(self):
        self._general_info()
        print(f"\tGrade: {self.__grade}")
        print(f"List Output: {list((self.get_personnel_code(), self.name, self.last_name, self.__grade))}")


# ==========================
# Apprentices Class
# ==========================
class Apprentices(Person):

    def __init__(self, name, last_name, personnel_code='-'):
        super().__init__(personnel_code, name, last_name)
        self.duration_internship = 12

    def show_apprentice_info(self):
        self._general_info()
        print(f"Duration Internship: {self.duration_internship}")
        print(f"List Output: {list((self.name, self.last_name, self.duration_internship))}")

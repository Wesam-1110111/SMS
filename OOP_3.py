from OOP_2 import Person


class Teacher(Person):
    teacher_id = 0

    def __init__(self, name: str, born_year: int, salary: int, email: str = "none",
                 address: str = "none", phone_number: str = "none"):
        super().__init__(name, born_year, email, address, phone_number)
        self.__salary = salary
        Teacher.teacher_id += 1

    def __str__(self):
        return super().__str__() + f"Salary: {self.__salary},\nID: {Teacher.teacher_id}."

    '''Set-Methods:'''

    def set_salary(self, new_salary: int):
        self.__salary = new_salary

    def get_salary(self):
        return self.__salary


t1 = Teacher("Zead", 1989, 2500)

t2 = Teacher("Amjed", 1999, 1500)

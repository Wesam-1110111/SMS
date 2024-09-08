from datetime import date


class Person:
    counter = 0

    def __init__(self, name: str, born_year: int, address: str = "None",
                 email: str = "None", phone_number: str = "None"):
        self.__name = name
        self.__born_year = born_year
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number
        Person.counter += 1

    def __str__(self):
        return (f"Name: {self.__name},\nAge: {self.get_age()},"
                f"\nPhone no. : {self.__phone_number},\nEmail: {self.__email},"
                f"\nAddress: {self.__address},\n")

    '''Get-Methods:'''

    def get_person_info(self):
        return (f"Name: {self.__name},\nAge: {self.get_age()},"
                f"\nAddress: {self.__address},\nEmail: {self.__email}")

    def get_age(self):
        return date.today().year - self.__born_year

    def get_name(self):
        return self.__name

    def get_born_year(self):
        return self.__born_year

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    '''Set-Methods:'''

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_born_year(self, new_year: int):
        self.__born_year = new_year

    def set_address(self, new_address: str):
        self.__address = new_address

    def set_email(self, new_email: str):
        self.__email = new_email

    def set_phone_number(self, new_phone_no: str):
        self.__phone_number = new_phone_no


"""   Sub Class   """


class Student(Person):  # """  ***   Student Class   ***  """
    student_id = 0

    def __init__(self, name: str, born_year: int, grade: str = "none",
                 phone_number: str = "none"):
        super().__init__(name, born_year, phone_number)
        self.__grade = grade
        Student.student_id += 1

    def get_student_info(self):
        return super().get_person_info() + f",\nGrade: {self.__grade}"

    def set_grade(self, new_grade: str):
        self.__grade = new_grade

    def get_grade(self):
        return self.__grade


s1 = Student("Wisam", 2000)
s2 = Student("Ahmed", 1999)

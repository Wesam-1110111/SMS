# -----------------------> the program need some fix <-------------------------
# ----- 1. you can/need to remove [clear()] from display_functions() below
# ----- because they clear the screen before "i as a user" can't read the output
# ------------------------------------------------------------------------------
# this is to me ;)
#
# 2024-06-04
#
import os
import OOP_2
import OOP_3
#from colors import Colors

class Colors:
    green='G'
    end='e'
    blue='B'
    red='R'
    yellow='Y'


def clear():
    pass


def welcome_mass():  # print : welcome to the SMS -> (school management system)
    print(f"""\n{Colors.green}
    ********************
    *  Welcome to SMS  *
    ********************{Colors.end}\n""")


def display_home_menu():  # show a list: 1.teacher. 2.student. 3.info of SMS. 0.exit
    print(f"""
       {Colors.green}***   home menu   ***{Colors.end}

    1. Teacher.
    2. Student.
    3. What is SMS.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


# show a list: 1.teacher({t1.get_name()}). 2.teacher(2). 0.exit
def display_teacher_menu():
    # clear()
    print(f"""
       {Colors.blue}***   Teachers menu   ***{Colors.end}

    1. {OOP_3.t1.get_name()}.
    2. {OOP_3.t2.get_name()}.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_teacher_submenu():  # show a list: 1.set methods. 2.get methods. 0.exit
    # clear()
    print(f"""
       {Colors.green}***   Teacher sub-menu   ***{Colors.end}

    1. Set methods.
    2. Get methods.
    3. Teacher information.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_teacher_set_menu():  # show a list: 1.set name. 2.set salary. etc. 0.exit
    # clear()
    print(f"""
       {Colors.blue}***   Teacher set menu   ***{Colors.end}

    1. Set name.
    2. Set born year.
    3. Set salary.
    4. Set email.
    5. Set address.
    6. Set phone number.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_teacher_get_menu():  # show a list: 1.get name. 2.get salary. etc. 0.exit
    # clear()
    print(f"""
       {Colors.green}***   Teacher get menu   ***{Colors.end}

    1. Get name.
    2. Get born year.
    3. Get salary.
    4. Get email.
    5. Get address.
    6. Get phone number.
    7. Get age.
    8. Get teacher information.
    9. Get ID
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_student_menu():  # show a list: 1.student(1). 2.student(2). 0.exit
    # clear()
    print(f"""
       {Colors.blue}***   Students menu   ***{Colors.end}

    1. {OOP_2.s1.get_name()}.
    2. {OOP_2.s2.get_name()}.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_student_submenu():  # show a list: 1.set methods. 2.get methods. 0.exit
    # clear()
    print(f"""
       {Colors.green}***   Student sub-menu   ***{Colors.end}

    1. Set methods.
    2. Get methods.
    3. Student information.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_student_set_menu():  # show a list: 1.set name. 2.set salary. etc. 0.exit
    # clear()
    print(f"""
       {Colors.blue}***   Students set menu   ***{Colors.end}

    1. Set name.
    2. Set born year.
    3. Set grade.
    4. Set email.
    5. Set address.
    6. Set phone number.
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_student_get_menu():  # show a list: 1.get name. 2.get salary. etc. 0.exit
    # clear()
    print(f"""
       {Colors.green}***   Students get menu   ***{Colors.end}

    1. Get name.
    2. Get born year.
    3. Get grade.
    4. Get email.
    5. Get address.
    6. Get phone number.
    7. Get age.
    8. Get student information.
    9. Get ID
    0. Exit.""")
    user_in = input("Please enter a number: ")
    return user_in


def display_info_menu():  # show: instructions of the system. display_home_menu()
    print(f"""{Colors.blue}
    *********************************
    SMS -> School Management System,
    this system let you set & get
    almost everything, like info. of
    teachers and students (for now).
    *********************************
    {Colors.end}""")


def display_exit_mass():  # show: Exit with the red color
    print(f"\n{Colors.red}Exit{Colors.end}")


def display_error_mass():
    print(f"{Colors.yellow}error with inputs!{Colors.end}")


def main():

    welcome_mass()

    while True:    # the main() loop    <--

        user_in = display_home_menu()
        if user_in == "1":  # <--   <--   1. teacher  <--

            while True:  # <--   <--   the loop of teacher  <--

                user_in = display_teacher_menu()
                # <--   <--   1. first object in teacher  <--
                if user_in == '1':

                    while True:  # <--   <--   the loop of teacher object set/get-methods  <--

                        user_in = display_teacher_submenu()

                        # <--   <--   1. sets in teacher object  <--
                        if user_in == '1':

                            while True:  # <--   <--   the loop of teacher object set menu  <--

                                user_in = display_teacher_set_menu()

                                # <--   <--   set name to teacher object  <--
                                if user_in == '1':
                                    user_data = input("Enter a name: ")
                                    OOP_3.t1.set_name(user_data)

                                # <--   <--   set born year to teacher object  <--
                                elif user_in == '2':
                                    user_data = input("Enter a born year: ")
                                    if user_data.isdigit():
                                        OOP_3.t1.set_born_year(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set salary to teacher object  <--
                                elif user_in == '3':
                                    user_data = input("Enter a salary: ")
                                    if user_data.isdigit():
                                        OOP_3.t1.set_salary(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set email to teacher object  <--
                                elif user_in == '4':
                                    user_data = input("Enter a email: ")
                                    OOP_3.t1.set_email(user_data)

                                # <--   <--   set address to teacher object  <--
                                elif user_in == '5':
                                    user_data = input("Enter a address: ")
                                    OOP_3.t1.set_address(user_data)

                                # <--   <--   set phone No. to teacher object  <--
                                elif user_in == '6':
                                    user_data = input("Enter a phone number: ")
                                    OOP_3.t1.set_phone_number(user_data)

                                # <--   <--   exit from set menu  <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break
                                else:
                                    display_error_mass()  # <--   <--   ?. error in teacher object  <--

                        # <--   <--   2. gets in teacher object  <--
                        elif user_in == '2':

                            while True:  # <--   <--   the loop of teacher object get menu  <--

                                user_in = display_teacher_get_menu()

                                # <--   <--   get name of teacher object  <--
                                if user_in == '1':
                                    print(f"Name: {OOP_3.t1.get_name()}.")

                                # <--   <--   get born year of teacher object  <--
                                elif user_in == '2':
                                    print(f"Born year: {OOP_3.t1.get_born_year()}.")

                                # <--   <--   get salary of teacher object  <--
                                elif user_in == '3':
                                    print(f"Salary: {OOP_3.t1.get_salary()}.")

                                # <--   <--   get email of teacher object  <--
                                elif user_in == '4':
                                    print(f"Email: {OOP_3.t1.get_email()}.")

                                # <--   <--   get address of teacher object  <--
                                elif user_in == '5':
                                    print(f"Address: {OOP_3.t1.get_address()}.")

                                # <--   <--   get phone No. of teacher object  <--
                                elif user_in == '6':
                                    print(f"Phone no: {OOP_3.t1.get_phone_number()}.")

                                # <--   <--   get age of teacher object  <--
                                elif user_in == '7':
                                    print(f"Age: {OOP_3.t1.get_age()}.")

                                # <--   <--   get teacher info of teacher object  <--
                                elif user_in == '8':
                                    print(OOP_3.t1)

                                # <--   <--   get id of teacher object  <--
                                elif user_in == '9':
                                    print(f"Teacher ID: {OOP_3.Teacher.teacher_id}.")

                                # <--   <--   exit from get menu  <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break
                                else:
                                    display_error_mass()  # <--   <--   ?. error in teacher object  <--

                        # <--   <--   3. display teacher object info <--
                        elif user_in == '3':
                            print(OOP_3.t1)

                        # <--   <--   0. exit from teacher object  <--
                        elif user_in == '0':
                            display_exit_mass()
                            break
                        else:  # <--   <--   ?. error in teacher object  <--
                            display_error_mass()

                # <--   <--   2. 2ed object in teacher  <--
                elif user_in == '2':

                    while True:  # <--   <--   the loop of teacher object set/get-methods  <--

                        user_in = display_teacher_submenu()

                        # <--   <--   1. sets in teacher object  <--
                        if user_in == '1':

                            while True:  # <--   <--   the loop of teacher object set menu  <--

                                user_in = display_teacher_set_menu()

                                # <--   <--   set name to teacher object  <--
                                if user_in == '1':
                                    user_data = input("Enter a name: ")
                                    OOP_3.t2.set_name(user_data)

                                # <--   <--   set born year to teacher object  <--
                                elif user_in == '2':
                                    user_data = input("Enter a born year: ")
                                    if user_data.isdigit():
                                        OOP_3.t2.set_born_year(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set salary to teacher object  <--
                                elif user_in == '3':
                                    user_data = input("Enter a salary: ")
                                    if user_data.isdigit():
                                        OOP_3.t2.set_salary(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set email to teacher object  <--
                                elif user_in == '4':
                                    user_data = input("Enter a email: ")
                                    OOP_3.t2.set_email(user_data)

                                # <--   <--   set address to teacher object  <--
                                elif user_in == '5':
                                    user_data = input("Enter a address: ")
                                    OOP_3.t2.set_address(user_data)

                                # <--   <--   set phone No. to teacher object  <--
                                elif user_in == '6':
                                    user_data = input("Enter a phone number: ")
                                    OOP_3.t2.set_phone_number(user_data)

                                # <--   <--   exit from set menu  <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break
                                else:
                                    display_error_mass()  # <--   <--   ?. error in teacher object  <--

                        # <--   <--   2. gets in teacher object  <--
                        elif user_in == '2':

                            while True:  # <--   <--   the loop of teacher object get menu  <--

                                user_in = display_teacher_get_menu()

                                # <--   <--   get name of teacher object  <--
                                if user_in == '1':
                                    print(f"Name: {OOP_3.t2.get_name()}.")

                                # <--   <--   get born year of teacher object  <--
                                elif user_in == '2':
                                    print(f"Born year: {OOP_3.t2.get_born_year()}.")

                                # <--   <--   get salary of teacher object  <--
                                elif user_in == '3':
                                    print(f"Salary: {OOP_3.t2.get_salary()}.")

                                # <--   <--   get email of teacher object  <--
                                elif user_in == '4':
                                    print(f"Email: {OOP_3.t2.get_email()}.")

                                # <--   <--   get address of teacher object  <--
                                elif user_in == '5':
                                    print(f"Address: {OOP_3.t2.get_address()}.")

                                # <--   <--   get phone No. of teacher object  <--
                                elif user_in == '6':
                                    print(f"Phone no: {OOP_3.t2.get_phone_number()}.")

                                # <--   <--   get age of teacher object  <--
                                elif user_in == '7':
                                    print(f"Age: {OOP_3.t2.get_age()}.")

                                # <--   <--   get teacher info of teacher object  <--
                                elif user_in == '8':
                                    print(OOP_3.t2)

                                # <--   <--   get id of teacher object  <--
                                elif user_in == '9':
                                    print(f"Teacher ID: {OOP_3.Teacher.teacher_id}.")

                                # <--   <--   exit from get menu  <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break
                                else:
                                    display_error_mass()  # <--   <--   ?. error in teacher object  <--

                        # <--   <--   3. display teacher object info <--
                        elif user_in == '3':
                            print(OOP_3.t2)

                        # <--   <--   0. exit from teacher object  <--
                        elif user_in == '0':
                            display_exit_mass()
                            break
                        else:  # <--   <--   ?. error in teacher object  <--
                            display_error_mass()

                elif user_in == '0':  # <--   <--   0. exit from teacher <--
                    display_exit_mass()
                    break

                else:
                    display_error_mass()    # <--   <--   ?. error in teacher  <--
                # user_in = input("Do you want to ")

        elif user_in == "2":  # <--   <--   2. student  <--

            while True:  # <--   <--   the loop of student  <--

                user_in = display_student_menu()
                # <--   <--   1. first object in student  <--
                if user_in == '1':

                    while True:  # <--   <--   the loop of student 1st object set/get menu  <--

                        user_in = display_student_submenu()

                        # <--   <--   1. sets in 1st student object  <--
                        if user_in == '1':

                            while True:  # <--   <--   the loop of 1st student object set menu  <--

                                user_in = display_student_set_menu()

                                # <--   <--   set name to 1st student object  <--
                                if user_in == '1':
                                    user_data = input("Enter a name: ")
                                    OOP_2.s1.set_name(user_data)

                                # <--   <--   set born year to 1st student object  <--
                                elif user_in == '2':
                                    user_data = input("Enter a born year: ")
                                    if user_data.isdigit():
                                        OOP_2.s1.set_born_year(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set grade to 1st student object  <--
                                elif user_in == '3':
                                    user_data = input("Enter a grade: ")
                                    OOP_2.s1.set_grade(user_data)

                                # <--   <--   set email to 1st student object  <--
                                elif user_in == '4':
                                    user_data = input("Enter a email: ")
                                    OOP_2.s1.set_email(user_data)

                                # <--   <--   set address to 1st student object  <--
                                elif user_in == '5':
                                    user_data = input("Enter a address: ")
                                    OOP_2.s1.set_address(user_data)

                                # <--   <--   set phone no. to 1st student object  <--
                                elif user_in == '6':
                                    user_data = input("Enter a phone no: ")
                                    OOP_2.s1.set_phone_number(user_data)

                                # <--   <--   exit from 1st student object set menu <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break

                                else:
                                    display_error_mass()  # <--   <--   error in student object set menu <--

                        # <--   <--   2. gets in 1st student object  <--
                        elif user_in == '2':

                            while True:  # <--   <--   the loop of 1st student object get menu  <--

                                user_in = display_student_get_menu()

                                # <--   <--   get name of 1st student object  <--
                                if user_in == '1':
                                    print(f"Name: {OOP_2.s1.get_name()}.")

                                # <--   <--   get born year of 1st student object  <--
                                elif user_in == '2':
                                    print(f"Born year: {OOP_2.s1.get_born_year()}.")

                                # <--   <--   get grade of 1st student object  <--
                                elif user_in == '3':
                                    print(f"Grade: {OOP_2.s1.get_grade()}.")

                                # <--   <--   get email of 1st student object  <--
                                elif user_in == '4':
                                    print(f"Email: {OOP_2.s1.get_email()}.")

                                # <--   <--   get address of 1st student object  <--
                                elif user_in == '5':
                                    print(f"Address: {OOP_2.s1.get_address()}.")

                                # <--   <--   get phone no. of 1st student object  <--
                                elif user_in == '6':
                                    print(f"Phone no: {OOP_2.s1.get_phone_number()}.")

                                # <--   <--   get age of 1st student object  <--
                                elif user_in == '7':
                                    print(f"Age: {OOP_2.s1.get_age()}.")

                                # <--   <--   get info. of 1st student object  <--
                                elif user_in == '8':
                                    print(f"Student info: {OOP_2.s1.get_student_info()}.")

                                # <--   <--   get id of 1st student object  <--
                                elif user_in == '9':
                                    print(f"Student ID: {OOP_2.Student.student_id}.")

                                # <--   <--   exit from 1st student object get menu <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break

                                else:
                                    display_error_mass()  # <--   <--   error in 1st student object inputs <--

                        # <--   <--   3. print info. of 1st student object  <--
                        elif user_in == '3':
                            print(f"Student info: {OOP_2.s1.get_student_info()}.")

                        # <--   <--   0. exit from 1st student object  <--
                        elif user_in == '0':
                            display_exit_mass()
                            break

                        else:
                            display_error_mass()  # <--   <--   ?. error in 1st student object  <--

                # <--   <--   2. 2ed object in student  <--
                elif user_in == '2':

                    while True:  # <--   <--   the loop of student 2ed object set/get menu  <--

                        user_in = display_student_submenu()

                        # <--   <--   1. sets in 2ed student object  <--
                        if user_in == '1':

                            while True:  # <--   <--   the loop of 2ed student object set menu <--

                                user_in = display_student_set_menu()

                                # <--   <--   set name to student object  <--
                                if user_in == '1':
                                    user_data = input("Enter a name: ")
                                    OOP_2.s2.set_name(user_data)

                                # <--   <--   set born year to student object <--
                                elif user_in == '2':
                                    user_data = input("Enter a born year: ")
                                    if user_data.isdigit():
                                        OOP_2.s2.set_born_year(user_data)
                                    else:
                                        display_error_mass()

                                # <--   <--   set grade to student object  <--
                                elif user_in == '3':
                                    user_data = input("Enter a grade: ")
                                    OOP_2.s2.set_grade(user_data)

                                # <--   <--   set email to student object  <--
                                elif user_in == '4':
                                    user_data = input("Enter a email: ")
                                    OOP_2.s2.set_email(user_data)

                                # <--   <--   set address to student object  <--
                                elif user_in == '5':
                                    user_data = input("Enter a address: ")
                                    OOP_2.s2.set_address(user_data)

                                # <--   <--   set phone no. to student object <--
                                elif user_in == '6':
                                    user_data = input("Enter a phone no: ")
                                    OOP_2.s2.set_phone_number(user_data)

                                # <--   <--   exit from student object set menu <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break

                                else:
                                    display_error_mass()  # <--   <--   error in student object set menu <--

                        # <--   <--   2. gets in 2ed student object  <--
                        elif user_in == '2':

                            while True:  # <--   <--   the loop of 2ed student object get menu <--

                                user_in = display_student_get_menu()

                                # <--   <--   get name of 2ed student object  <--
                                if user_in == '1':
                                    print(f"Name: {OOP_2.s2.get_name()}.")

                                # <--   <--   get born year of 2ed student object <--
                                elif user_in == '2':
                                    print(f"Born year: {OOP_2.s2.get_born_year()}.")

                                # <--   <--   get grade of 2ed student object  <--
                                elif user_in == '3':
                                    print(f"Grade: {OOP_2.s2.get_grade()}.")

                                # <--   <--   get email of 2ed student object  <--
                                elif user_in == '4':
                                    print(f"Email: {OOP_2.s2.get_email()}.")

                                # <--   <--   get address of 2ed student object <--
                                elif user_in == '5':
                                    print(f"Address: {OOP_2.s2.get_address()}.")

                                # <--   <--   get phone no. of 2ed student object <--
                                elif user_in == '6':
                                    print(f"Phone no: {OOP_2.s2.get_phone_number()}.")

                                # <--   <--   get age of 2ed student object  <--
                                elif user_in == '7':
                                    print(f"Age: {OOP_2.s2.get_age()}.")

                                # <--   <--   get info. of 2ed student object  <--
                                elif user_in == '8':
                                    print(f"Student info: {OOP_2.s2.get_student_info()}.")

                                # <--   <--   get id of 2ed student object  <--
                                elif user_in == '9':
                                    print(f"Student ID: {OOP_2.Student.student_id}.")

                                # <--   <--   exit from 2ed student object get menu  <--
                                elif user_in == '0':
                                    display_exit_mass()
                                    break

                                else:
                                    display_error_mass()  # <--   <--   error in 2ed student object get menu inputs <--

                        # <--   <--   3. print info. of 2ed student object  <--
                        elif user_in == '3':
                            pass

                        # <--   <--   0. exit from 2ed student object  <--
                        elif user_in == '0':
                            display_exit_mass()
                            break

                        else:
                            display_error_mass()  # <--   <--   ?. error in 2ed student object  <--

                elif user_in == '0':  # <--   <--   0. exit from student <--
                    display_exit_mass()
                    break

                else:
                    display_error_mass()
                # user_in = input("Do you want to ")

        elif user_in == "3":  # <--   <--   3. what is SMS  <--
            display_info_menu()

        elif user_in == "0":  # <--   <--   0. exit from main() loop  <--
            display_exit_mass()
            break

        else:
            display_error_mass()  # <--   <--   ?. error in main menu inputs  <--


'''  here we go  '''

main()

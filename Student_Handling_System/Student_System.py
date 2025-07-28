student_list = []
grade_list = []

print("----School System----")

while True:
    menu_choice = int(input("Do you want to enter (1), search (2) for a grade, or terminate the program (3)?: "))

    if menu_choice == 1:
        counter = 1
        while True:
            print("Enter students and grades\n")
            student_name = input("Enter the name of student " + str(counter) + ": ")
            student_list.append(student_name)
            grades = int(input("Enter the grade for " + student_name + ": "))
            grade_list.append(grades)

            choice2 = int(input("Do you want to continue? (1. Yes, 2. No)?: "))
            if choice2 == 2:            
                print("Successfully entered " + str(counter) + " students")
                break
            counter += 1

    elif menu_choice == 2:
        print("Student Search\n")
        student_name = input("Enter the name of the student you are looking for: ")
        if student_name in student_list:
            index = student_list.index(student_name)
            print("Student found!")
            print("The student named " + student_name + " has a grade of " + str(grade_list[index]))

    elif menu_choice == 3:
        print("Program terminated")
        break

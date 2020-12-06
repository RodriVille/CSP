#   a118_grades.py
my_courses = ["English", "Math", "CS"]

redo = "y"
while ( redo == "y"):
    for course in my_courses:
        print(course)
        try:
            point = int(input("Enter your grade as a percentage: "))
            if point >= 90:
                print("You have an A")
            elif point >= 80:
                print("You have an B")
            elif point >= 70:
                print("You have an C")
            elif point >= 60:
                print("You have an D")
            else:
                print("You are failing")
        except:
            print("invalid input")
            break
            course = my_courses[1]
        redo = input("do you want to redo your grades? (y/n)")


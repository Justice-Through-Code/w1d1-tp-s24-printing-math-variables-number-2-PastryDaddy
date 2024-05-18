#Grade calculator by Chris K
def calculate_average_grade():
#Student info inputs (with float conversion)
    student_name = input("Hi! What's your name?")
    math_score = float(input(f"Nice to meet you, {student_name}, what's your math score?"))
    english_score = float(input("Awesome! What's your English score?"))
    science_score = float(input("Great Job! What's your science score?"))
#Equation to calculate grade and store it as a variable
    average_grade = ((math_score+english_score+science_score)/3.0)
#Formatting grade
 
#Ouput
    print(f"{student_name}, {average_grade}")
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"")
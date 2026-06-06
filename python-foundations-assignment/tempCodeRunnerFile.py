TOTAL_GRADE = 100
num_of_subjects = int(input("How many subjects do you offer? "))
total_possible_score = TOTAL_GRADE * num_of_subjects

score_list = []

for i in range(num_of_subjects):
    while True:
        try:
            student_scores = int(input(f"Enter the score for subject {i+1} (Max {TOTAL_GRADE}): "))
            if 0 <= student_scores <= TOTAL_GRADE:
                score_list.append(student_scores)
                break
            else:
                print(f"Please enter a score between 0 and {TOTAL_GRADE}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
total_score = sum(score_list)

student_grade_percentage = (total_score/total_possible_score) * 100

print(f"\nYOUR GRADE PERCENTAGE IS {student_grade_percentage}% \nWELDONE!")
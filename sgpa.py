def calculate_sgpa():
    total_credits = 0
    total_weighted_points = 0

    num_subjects = int(input("Enter number of subjects: "))

    for i in range(num_subjects):
        print(f"\nSubject {i + 1}")
        credit = float(input("Enter credit for this subject: "))
        grade_point = float(input("Enter grade point (O=10, A+=10, A=9, B+=8, B=7, C=7, D+=6, E=5, F=0): "))

        total_credits += credit
        total_weighted_points += credit * grade_point

    if total_credits == 0:
        print("No credits entered. Cannot calculate SGPA.")
        return

    sgpa = total_weighted_points / total_credits
    print(f"\n✅ Your SGPA is: {round(sgpa, 2)}")

# Run the calculator
calculate_sgpa()
